# node_data

A node data store

## Use case

Puppet external facts often get used as a way of storing data in the PuppetDB that isn't necessarily for use by Puppet when compiling a catalog.
This can cause the collection of facts to to take a long time, it can fill the PuppetDB and the things that need the data end up running queries on the PuppetDB that drains yet more resources.
All this can adversely affect the performance of Puppet.
The purpose of this is to create a simple data store where data for a node can be stored and retrieved.

## Design

1. Create a backend database to store the data.
2. Create some code that can push data into the database and then retrieve it.

## Setting up the database

```bash

brew install postgresql@14
brew services start postgresql@14

createdb nodedata
psql nodedata
nodedata=# psql -U postgres -c "createuser flaskuser"
nodedata-# psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE mydatabase TO flaskuser;"

psql -h localhost -U flaskuser -d nodedata

CREATE TABLE mytable (
    server_name TEXT PRIMARY KEY,
    data1 JSONB,
    data2 JSONB,
    data3 JSONB
);
```
