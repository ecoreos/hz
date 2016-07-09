ecore.define('web.session', function (require) {
    var Session = require('web.Session');
    var modules = ecore._modules;
    return new Session(undefined, undefined, {modules:modules, use_cors: false});
});
