# import falcon

# from .images import Resource

# api = application = falcon.API()

# images = Resource()
# api.add_route('/images', images)

import falcon
import couchdb

s = couchdb.Server('http://admin:qwerty@localhost:5984')
db = s['jovit_db']
view = db.view('jovit_d/jovit_v')
for r in view:
	result = r.value
print(result)
app = application = falcon.API()