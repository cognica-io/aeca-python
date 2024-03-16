# Aeca Python Client

A Python client for Aeca database server.

## Installation

```bash
$ pip install aeca
```

## Current Status

The current version is fully functional and stable for the production environment. However, the API is still subject to change and may break backward compatibility in the next release.

### Current Version

```python
import aeca

# Establish connection to a local database server.
channel = aeca.Channel("localhost", 10080)

# List collections.
db = aeca.DocumentDB(channel)
collections = db.list_collections()
for collection in collections:
    print(collection)

# Find a specific document in the Wikipedia collection.
collection = aeca.find_collection("Wikipedia")
df = collection.find({
    "page_id": 42
}, to_pandas=True)
print(df)
```

### Next Version (Work in progress)

```python
import aeca

# Establish connection to a local database server.
channel = aeca.Channel("localhost", 10080)

# Login to the database.
ws = aeca.Workspaces(channel, "user_id", "password")

# List workspaces.
workspaces = ws.list_workspaces()
for workspace in workspaces:
    print(workspace)

# Open the workspace and list the collections.
workspace = ws.find_workspace("test")
db = aeca.DocumentDB(workspace)
collections = db.list_collections()
for collection in collections:
    print(collection)

# Find a specific document in the Wikipedia collection.
collection = aeca.find_collection("Wikipedia")
df = collection.find({
    "page_id": 42
}, to_pandas=True)
print(df)
```
