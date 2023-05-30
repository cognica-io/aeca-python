# Cognica Python Client

A Python client for Cognica database server.

## Installation

```bash
$ pip install cognica
```

## Current Status

The current version is fully functional and stable for the production environment. However, the API is still subject to change and may break backward compatibility in the next release.

### Current Version

```python
import cognica

# Establish connection to a local database server.
channel = cognica.Channel("localhost", 10080)

# List collections.
db = cognica.DocumentDB(channel)
collections = db.list_collections()
for collection in collections:
    print(collection)

# Find a specific document in the Wikipedia collection.
collection = cognica.find_collection("Wikipedia")
df = collection.find({
    "page_id": 42
}, to_pandas=True)
print(df)
```

### Next Version (Work in progress)

```python
import cognica

# Establish connection to a local database server.
channel = cognica.Channel("localhost", 10080)

# Login to the database.
ws = cognica.Workspaces(channel, "user_id", "password")

# List workspaces.
workspaces = ws.list_workspaces()
for workspace in workspaces:
    print(workspace)

# Open the workspace and list the collections.
workspace = ws.find_workspace("test")
db = cognica.DocumentDB(workspace)
collections = db.list_collections()
for collection in collections:
    print(collection)

# Find a specific document in the Wikipedia collection.
collection = cognica.find_collection("Wikipedia")
df = collection.find({
    "page_id": 42
}, to_pandas=True)
print(df)
```
