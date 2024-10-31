import mitmproxy.http
from mitmproxy import ctx


class MHW:
    def __init__(self):
        self.num = 0

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.url.endswith("/systems/EAR-B-WW/00001/system.json"):
            # modify the test time and working_state
            flow.response.text = """{
    "api_timeout": 30000,
    "custom_property": "eyJvYnRfaW5mbyI6eyJlbnYiOjEsInN0YXJ0X3RpbWUiOjE1Nzc4MDgwMDAsImVuZF90aW1lIjoxODkzNDI3MjAwfSwicWEzIjp7ImFwaSI6Imh0dHBzOi8vYXBpLndpbGRzLm1vbnN0ZXJodW50ZXIuY29tIiwibm90aWZ5Ijoid3NzOi8vbm90aWZ5LndpbGRzLm1vbnN0ZXJodW50ZXIuY29tIn19",
    "json_ver": "1.0.2",
    "mmr": "https://mmr.rebe.capcom.com",
    "mtm": "https://mtm.rebe.capcom.com",
    "mtms": "https://mtms.rebe.capcom.com",
    "nkm": "https://nkm.rebe.capcom.com",
    "revision": "00001",
    "selector": "https://selector.gs.capcom.com",
    "title": "EAR-B-WW",
    "tmr": "https://pubsub.googleapis.com/v1/projects/earth-analysis-obt/topics/analysis-client-log:publish",
    "wlt": "https://wlt.rebe.capcom.com",
    "working_state": "alive"
}"""
            ctx.log.info("Replaced response")

addons = [
    MHW()
]
