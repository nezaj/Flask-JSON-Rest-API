## Flask JSON REST-API Example
Simple example showing a simple JSON REST-API implemention using Flask.

### Quickstart
```
# Clone Repo
git clone https://github.com/nezaj/Flask-JSON-Rest-API.git flask-json-api
cd flask-json-api

# Create/Active virtualenv
make virtualenv
source ~/.virtualenvs/flask-json-api/bin/activate

# Run it
./manage.py runserver
```

### Routes
To see the full list run `./manage.py list_routes` from the root directory
```
service.bad_request                                HEAD,OPTIONS,GET     /400
service.bad_route                                  HEAD,OPTIONS,GET     /404
service.health                                     HEAD,OPTIONS,GET     /health
service.internal_error                             HEAD,OPTIONS,GET     /500
static                                             HEAD,OPTIONS,GET     /static/[filename]
units.create                                       POST,OPTIONS         /units
units.delete                                       OPTIONS,DELETE       /units/[unit_id]
units.index                                        HEAD,OPTIONS,GET     /units
units.show                                         HEAD,OPTIONS,GET     /units/[unit_id]
units.update                                       PUT,OPTIONS          /units/[unit_id]
```

### Testing
```
# Static analysis + Tests
make check

# Static analysis
make pylint
make pep8

# Tests
make test
```
