import json
import leveldb
from abci.application import BaseApplication
from abci.server import ABCIServer, DefaultABCIPort

# Open (or create) a LevelDB database in the "./state" folder.
db = leveldb.LevelDB('./state', create_if_missing=True)

class ValidationApp(BaseApplication):
    def deliver_tx(self, raw_tx):
        try:
            tx = json.loads(raw_tx.decode())
            required = {'tweet_id', 'zone_id', 'hazard', 'status', 'timestamp'}
            if not required.issubset(tx):
                return self._response(code=1, log="Bad TX schema")
        except Exception as e:
            return self._response(code=1, log=f"Bad TX: {e}")
        
        db.Put(tx['tweet_id'].encode(), raw_tx)
        return self._response(code=0)

    def query(self, req):
        key = req.data.decode()
        try:
            value = db.Get(key.encode())
            return self._response(code=0, value=value)
        except Exception as e:
            return self._response(code=1, log=f"Not found: {e}")

if __name__ == "__main__":
    app = ValidationApp()
    server = ABCIServer(app, port=DefaultABCIPort)
    print(f"Starting ABCI App on port {DefaultABCIPort}...")
    server.run()
