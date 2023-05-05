# node_data
A node data store

# Use case
Puppet external facts often get used as a way of storing data in the PuppetDB that isn't necessarily for use by Puppet when compiling a catalog. 
This can cause the collection of facts to to take a long time, it can fill the PuppetDB and the things that need the data end up running queries on the PuppetDB that drains yet more resources.
All this can adversly affect the performance of Puppet.
The purpose of this is to create a simple data store where data for a node can be stored and retrieved. 


# Design
1. Create a backend database to store the data.
2. Create some code that can updated the database.
3. An end point that can recieve the data.




