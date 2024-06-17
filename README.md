This is a learning project consisting of a deep sequence keras model converted into a REST API using fastapi framework.
The project uses Astra DB for the storage of results of model on queries from an endpoint.
Currently to see the working of the endpoint a few pre-requisites are required-\
-> Make an account on Datastax which hosts the nosql database Astra DB.\
-> Create a non-vector database and generate tokens.\
-> Download the secure connection bundle.\
-> Create environment variables for the tokens and the path to the secure connection bundle. Be sure to name the variables as ASTRA_DB_CLIENT_ID and ASTRA_DB_CLIENT_SECRET. Also make sure that the path to the secure connection bundle is given properly\
-> Run the server on local host.
