var page = require('webpage').create();
var sys = require('system');
if (sys.args.length === 1) {
    phantom.exit(1);
}

var timeout = sys.args[1];
var url = sys.args[2];
var jscode = sys.args[3];
addDebugEvents(page,sys);

page.viewportSize = {
    width: 1366,
    height: 768
};
page.settings.resourceTimeout = timeout;
page.onResourceTimeout = function () {
    phantom.exit(2);
};
page.open(url, function (status) {
    if (status === 'success') {
        var content = page.content;
        console.log(content);
        phantom.exit(0);
    } else {
        phantom.exit(1);
    }
});
function addDebugEvents(page, sys) {

    page.onResourceError = function (resourceError) {
        page.reason = resourceError.errorString;
        page.reason_url = resourceError.url;
    };

    page.onResourceRequested = function (request) {
        sys.stderr.writeLine('= onResourceRequested()');
        sys.stderr.writeLine('  request: ' + JSON.stringify(request, undefined, 4));
    };

    page.onResourceReceived = function (response) {
        sys.stderr.writeLine('= onResourceReceived()');
        sys.stderr.writeLine('  id: ' + response.id + ', stage: "' + response.stage + '", response: ' + JSON.stringify(response));
    };

    page.onLoadStarted = function () {
        sys.stderr.writeLine('= onLoadStarted()');
        var currentUrl = page.evaluate(function () {
            return window.location.href;
        });
        sys.stderr.writeLine('  leaving url: ' + currentUrl);
    };

    page.onLoadFinished = function (status) {
        sys.stderr.writeLine('= onLoadFinished()');
        sys.stderr.writeLine('  status: ' + status);
    };

    page.onNavigationRequested = function (url, type, willNavigate, main) {
        sys.stderr.writeLine('= onNavigationRequested');
        sys.stderr.writeLine('  destination_url: ' + url);
        sys.stderr.writeLine('  type (cause): ' + type);
        sys.stderr.writeLine('  will navigate: ' + willNavigate);
        sys.stderr.writeLine('  from page\'s main frame: ' + main);
    };

    page.onResourceError = function (resourceError) {
        sys.stderr.writeLine('= onResourceError()');
        sys.stderr.writeLine('  - unable to load url: "' + resourceError.url + '"');
        sys.stderr.writeLine('  - error code: ' + resourceError.errorCode + ', description: ' + resourceError.errorString);
    };

    page.onError = function (msg, trace) {
        sys.stderr.writeLine('= onError()');
        var msgStack = ['  ERROR: ' + msg];
        if (trace) {
            msgStack.push('  TRACE:');
            trace.forEach(function (t) {
                msgStack.push('    -> ' + t.file + ': ' + t.line + (t.function ? ' (in function "' + t.function + '")' : ''));
            });
        }
        sys.stderr.writeLine(msgStack.join('\n'));
    };

}