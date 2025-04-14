# Test Planet API
Project to test Django REST Framework for ASW

# Commands to create the schema file
py manage.py spectacular --color --file schema.yaml

# Commands to test API
schemathesis run schema.yaml --base-url=http://localhost:8000 -H "Authorization: Api-Key <api-key>"