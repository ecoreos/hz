// ------------------------------------------------------------------------------
// Compatibility with eCore v8.  
// 
// With the new module system, no global variable can (and should) be accessed
// in ecore.  This file exports everything, to mimic the previous global 
// namespace structure.  This is only supposed to be used by 3rd parties to 
// facilitate migration.  eCore addons should not use the 'ecore' variable at 
// all.
// ------------------------------------------------------------------------------
ecore.define('web.compatibility', function (require) {
"use strict";

var ActionManager = require('web.ActionManager');
var core = require('web.core');
var data = require('web.data');
var Dialog = require('web.Dialog');
var FavoriteMenu = require('web.FavoriteMenu');
var form_common = require('web.form_common');
var formats = require('web.formats');
var FormView = require('web.FormView');
var form_relational = require('web.form_relational'); // necessary
var form_widgets = require('web.form_widgets'); // necessary
var framework = require('web.framework');
var ListView = require('web.ListView');
var Menu = require('web.Menu');
var Model = require('web.DataModel');
var pyeval = require('web.pyeval');
var Registry = require('web.Registry');
var SearchView = require('web.SearchView');
var session = require('web.session');
var Sidebar = require('web.Sidebar');
var SystrayMenu = require('web.SystrayMenu');
var time = require('web.time');
var UserMenu = require('web.UserMenu');
var utils = require('web.utils');
var View = require('web.View');
var ViewManager = require('web.ViewManager');
var WebClient = require('web.WebClient');
var Widget = require('web.Widget');

var client_started = $.Deferred();

var OldRegistry = Registry.extend({
    add: function (key, path) {
    },
    get_object: function (key) {
        return get_object(this.map[key]);
    },
});

window.ecore = window.ecore || {};

$.Mutex = utils.Mutex;
ecore._session_id = "instance0";
ecore._t = core._t;
ecore.get_cookie = utils.get_cookie;

ecore.qweb = core.qweb;
ecore.session = session;

ecore.web = ecore.web || {};
ecore.web._t = core._t;
ecore.web._lt = core._lt;

ecore.web.ActionManager = ActionManager;
ecore.web.auto_str_to_date = time.auto_str_to_date;
ecore.web.blockUI = framework.blockUI;
ecore.web.BufferedDataSet = data.BufferedDataSet;
ecore.web.bus = core.bus;
ecore.web.Class = core.Class;
ecore.web.client_actions = make_old_registry(core.action_registry);
ecore.web.CompoundContext = data.CompoundContext;
ecore.web.CompoundDomain = data.CompoundDomain;
ecore.web.DataSetSearch = data.DataSetSearch;
ecore.web.DataSet = data.DataSet;
ecore.web.date_to_str = time.date_to_str;
ecore.web.Dialog = Dialog;
ecore.web.DropMisordered = utils.DropMisordered;

ecore.web.form = ecore.web.form || {};
ecore.web.form.AbstractField = form_common.AbstractField;
ecore.web.form.compute_domain = data.compute_domain;
ecore.web.form.DefaultFieldManager = form_common.DefaultFieldManager;
ecore.web.form.FieldChar = core.form_widget_registry.get('char');
ecore.web.form.FieldFloat = core.form_widget_registry.get('float');
ecore.web.form.FieldStatus = core.form_widget_registry.get('statusbar');
ecore.web.form.FieldMany2ManyTags = core.form_widget_registry.get('many2many_tags');
ecore.web.form.FieldMany2One = core.form_widget_registry.get('many2one');
ecore.web.form.FormWidget = form_common.FormWidget;
ecore.web.form.tags = make_old_registry(core.form_tag_registry);
ecore.web.form.widgets = make_old_registry(core.form_widget_registry);

ecore.web.format_value = formats.format_value;
ecore.web.FormView = FormView;

ecore.web.json_node_to_xml = utils.json_node_to_xml;

ecore.web.ListView = ListView;
ecore.web.Menu = Menu;
ecore.web.Model = Model;
ecore.web.normalize_format = time.strftime_to_moment_format;
ecore.web.py_eval = pyeval.py_eval;
ecore.web.pyeval = pyeval;
ecore.web.qweb = core.qweb;

ecore.web.Registry = OldRegistry;

ecore.web.search = {};
ecore.web.search.FavoriteMenu = FavoriteMenu;
ecore.web.SearchView = SearchView;
ecore.web.Sidebar = Sidebar;
ecore.web.str_to_date = time.str_to_date;
ecore.web.str_to_datetime = time.str_to_datetime;
ecore.web.SystrayItems = SystrayMenu.Items;
ecore.web.unblockUI = framework.unblockUI;
ecore.web.UserMenu = UserMenu;
ecore.web.View = View;
ecore.web.ViewManager = ViewManager;
ecore.web.views = make_old_registry(core.view_registry);
ecore.web.WebClient = WebClient;
ecore.web.Widget = Widget;

ecore.Widget = ecore.web.Widget;
ecore.Widget.prototype.session = session;


WebClient.include({
    init: function () {
        ecore.client = this;
        ecore.webclient = this;
        start_modules();
        client_started.resolve();
        this._super.apply(this, arguments);
    },
});


function make_old_registry(registry) {
    return {
        add: function (key, path) {
            client_started.done(function () {
                registry.add(key, get_object(path));
            });
        },
    };
}
function get_object(path) {
    var object_match = ecore;
    path = path.split('.');
    // ignore first section
    for(var i=1; i<path.length; ++i) {
        object_match = object_match[path[i]];
    }
    return object_match;
}

/**
 * eCore instance constructor
 *
 * @param {Array|String} modules list of modules to initialize
 */
var inited = false;
function start_modules (modules) {
    if (modules === undefined) {
        modules = ecore._modules;
    }
    modules = _.without(modules, "web");
    if (inited) {
        throw new Error("eCore was already inited");
    }
    inited = true;
    for(var i=0; i < modules.length; i++) {
        var fct = ecore[modules[i]];
        if (typeof(fct) === "function") {
            ecore[modules[i]] = {};
            for (var k in fct) {
                ecore[modules[i]][k] = fct[k];
            }
            fct(ecore, ecore[modules[i]]);
        }
    }
    ecore._modules = ['web'].concat(modules);
    return ecore;
};

// Monkey-patching of the ListView for backward compatibiliy of the colors and
// fonts row's attributes, as they are deprecated in 9.0.
ListView.include({
    view_loading: function(fvg) {
        this._super(fvg);

        if (this.fields_view.arch.attrs.colors) {
            this.colors = _(this.fields_view.arch.attrs.colors.split(';')).chain()
                .compact()
                .map(function(color_pair) {
                    var pair = color_pair.split(':'),
                        color = pair[0],
                        expr = pair[1];
                    return [color, py.parse(py.tokenize(expr)), expr];
                }).value();
        }

        if (this.fields_view.arch.attrs.fonts) {
            this.fonts = _(this.fields_view.arch.attrs.fonts.split(';')).chain().compact()
                .map(function(font_pair) {
                    var pair = font_pair.split(':'),
                        font = pair[0],
                        expr = pair[1];
                    return [font, py.parse(py.tokenize(expr)), expr];
                }).value();
        }
    },
    /**
     * Returns the style for the provided record in the current view (from the
     * ``@colors`` and ``@fonts`` attributes)
     *
     * @param {Record} record record for the current row
     * @returns {String} CSS style declaration
     */
    style_for: function (record) {
        var len, style= '';

        var context = _.extend({}, record.attributes, {
            uid: session.uid,
            current_date: moment().format('YYYY-MM-DD')
            // TODO: time, datetime, relativedelta
        });
        var i;
        var pair;
        var expression;
        if (this.fonts) {
            for(i=0, len=this.fonts.length; i<len; ++i) {
                pair = this.fonts[i];
                var font = pair[0];
                expression = pair[1];
                if (py.PY_isTrue(py.evaluate(expression, context))) {
                    switch(font) {
                    case 'bold':
                        style += 'font-weight: bold;';
                        break;
                    case 'italic':
                        style += 'font-style: italic;';
                        break;
                    case 'underline':
                        style += 'text-decoration: underline;';
                        break;
                    }
                }
            }
        }
 
        if (!this.colors) { return style; }
        for(i=0, len=this.colors.length; i<len; ++i) {
            pair = this.colors[i];
            var color = pair[0];
            expression = pair[1];
            if (py.PY_isTrue(py.evaluate(expression, context))) {
                return style += 'color: ' + color + ';';
            }
        }
        return style;
     },
});


});
