import yaml
import time
import threading
from openapi3 import OpenAPI

class Feed(threading.Thread):
    def __init__(self, q):
        self.q = q
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        self.load_api_spec()
        while(True):
            self.fetch(2019020737)
            current_play_time_remaining = self.data.liveData.plays.currentPlay['about']['periodTimeRemaining']
            current_play_period_ordinal = self.data.liveData.plays.currentPlay['about']['ordinalNum']
            current_play_event = self.data.liveData.plays.currentPlay['result']['event']

            status = '{} — {}\n{}'
            self.q.put(status.format(current_play_period_ordinal, current_play_time_remaining, current_play_event))

            time.sleep(2)


    def load_api_spec(self, path='src/openapi.yaml'):
        with open(path) as f:
            spec = yaml.safe_load(f.read())
        self.api = OpenAPI(spec)
        return

    def fetch(self, id):
        self.data = self.api.call_getGame(parameters={"id": id})
        return
