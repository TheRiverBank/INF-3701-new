# 17.01
## DBMS
* DBMS, applications sees the logical view of the databases. Complexity handled by the DBMS (multiple data stores, relations..).

## Relational model
* Relational model, designed for structured data. Added features for objects, XML/JSON, etc. Flat structrure of tuples where each tuple is identified by a primary key. Contains atomic values (indivisible values).

## Microservices
* ACID transactions in microservices creates tighter coupling.
* Locking is slow and complex in a distributed system.
* Data dependecies between microservices
* Replica consistency between microservices

## Object-oriented data model
* Tuple (*object id*, *object type*, *value*)
* Objects might have state that needs to be stored.
* Comapred to the relation model, separate languages for queries and application is not required. In a relation model, an application written in Python requries conversion to SQL for querying. 

transaction vs data server

# 20.01
## Parallel vs distributed
Difference between parallel and distributed system is that distributes sytems are geo distributed. Also, there are data/schema heterogenity in distriuted systems. Must be more resilient? 

## Improvements of parallelism
Look into speedup and scaleup


# 24.01
* Replication for resilience 
    * Locating data where they are most frequently used
* Partition for performance
    * Round-robin, hash paratition, range partition
    * Partitioning tables to find nodes that store the requested value
    * Parallelize requests


# 10.02 Big Data and Data Mining
## Motivation
* Much larger amounts of data from varied sources. (Volume, velocity, Variety).

## Sources
* Web servers needs to know how to engage users and give them relevant ads
* Find out how to better deliver their services by monetoring user patterns
* How much stock needs to be ordered bases on user interest

## Sharding
* Paritioning data across multiple databases or machines.
* Partiotioned on partition attributes, partition keys or shard keys. 
    * Range partition
    * Hash partition
    * Round robin
* Is a form of horizzontal partition where the rows of a table is distributed to different nodes (vertical is to split the attributes, or columns, at different nodes).
* Used as a way to scale blockchain
* Limitations:
    * Track how data are partitioned
    * Mage database when they are overloaded
    * Replication for accessibility

## Parallel databases
* Data replicated across machines
* Improces accesability
* Advatages
    * Speed
    * Performance
    * Reliability of data
    * Availability of data
* Limitations
    * High prob of failure
    * Challenger for long running queries.
        * Run for a long time
        * Restarting the query is expensive

## Distributed file sytstems
* Blocks of files are partitioned across machines

## Hadoop
* Machines under one switch is called a **rack*.
* Has a master, **nameNode** at the top of the rack with the rest of machines in the rack beeing **datNodes**.
* A write requests is sent by the user to the name node who returns which block in which node the data item should be wwritten to. If the dat item is to big it will split it up and give the different data nodes to store the data.

# Data Mining
* Finding patterns in data