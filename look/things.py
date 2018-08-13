# things.py

# Let's get this party started!
import falcon
# from .app import result
import couchdb

s = couchdb.Server('http://admin:qwerty@localhost:5984')
db = s['jovit_db']
view = db.view('jovit_d/jovit_v')
for r in view:
	result = r.value

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource:
    def on_get(self, req, resp):
    	things = result
    	print things
    	resp.media = things

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
# things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', ThingsResource())