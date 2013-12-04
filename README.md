OpenJC ckan site
================

Meant to be deployed on Heroku, but you can run it locally:

```
# Install the python dependencies
pip install -r requirements.txt

# Initialize the postgres data directory
initdb pgdata

# Start postgres in the background
postgres -D pgdata &

# Create the ckan_default postgres db
createdb -O ckan_default ckan_default -E utf-8

# Create the ckan_default postgres user
createuser -S -D -R -P ckan_default

# Set the postgres url
export CKAN_DB=postgresql://ckan_default:ckan@localhost/ckan_default

# Initialize the application database tables
paster --plugin=ckan db init -c heroku.ini

# Run the web app
./run
```

Then you can open the app at [http://localhost:5000/](http://localhost:5000/)
