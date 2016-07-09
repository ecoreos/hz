ecore.define('web_kanban.compatibility', function (require) {
"use strict";

var kanban_widgets = require('web_kanban.widgets');
var KanbanRecord = require('web_kanban.Record');
var KanbanColumn = require('web_kanban.Column');
var KanbanView = require('web_kanban.KanbanView');

return;
ecore = window.ecore || {};
ecore.web_kanban = ecore.web_kanban || {};
ecore.web_kanban.AbstractField = kanban_widgets.AbstractField;
ecore.web_kanban.KanbanGroup = KanbanColumn;
ecore.web_kanban.KanbanRecord = KanbanRecord;
ecore.web_kanban.KanbanView = KanbanView;

});
