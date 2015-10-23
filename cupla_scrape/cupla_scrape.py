import subprocess as subp
from threading import Timer, Event
from lxml import html

def scrape_http(url):
    cmd = [
        'phantomjs',
        '--ssl-protocol=tlsv1',
        '--ignore-ssl-errors=true',
        'phantom.js',
        str(15000),
        url,
        "return {};"
    ]
    proc = subp.Popen(cmd, stdout=subp.PIPE, stderr=subp.PIPE)
    timer = Timer(15000, lambda p: p.kill(), [proc])
    timer.start()
    out, err = proc.communicate()
    timer.cancel()
    rtc = proc.returncode
    return rtc, out

done_http = Event()
obj = dict()
data = None
obj['link'] = "http://culpa.info/courses/6079"
while not done_http.is_set():
    rtc, out = scrape_http(obj['link'])
    if rtc == 0:
        data = dict(url=obj['link'], html=out)
        done_http.set()
    elif rtc == 1:
        raise RuntimeError()
    else:
        print "TIMEDOUT"

print html.fromstring(data['html'])
