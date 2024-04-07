from pymongo.mongo_client import MongoClient
mongo_client = MongoClient()

host_info = mongo_client['HOST']
print ("host:", host_info)

#########################################
# one URI string passed as a parameter:
mongo_client = MongoClient('mongodb://localhost:27017')

# the string domain and integer port passed:
mongo_client = MongoClient('localhost', 27017)
print("################################### Success here###################")

myclient = mongo_client
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:  print("The database exists.")