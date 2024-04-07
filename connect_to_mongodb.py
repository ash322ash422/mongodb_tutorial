from pymongo.mongo_client import MongoClient
mongo_client = MongoClient()

host_info = mongo_client['HOST']
print ("host:", host_info)

#########################################
# one URI string passed as a parameter:
CONNECTION_STRING = 'mongodb://localhost:27017'
mongo_client = MongoClient(CONNECTION_STRING)

# the string domain and integer port passed:
mongo_client = MongoClient('localhost', 27017)
print("################################### Success here###################")


myclient = mongo_client
print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "mydatabase" in dblist:  print("The database exists.")
print("###########################")

CONNECTION_STRING = 'mongodb://localhost:27017'
mongo_client = MongoClient(CONNECTION_STRING)
db = mongo_client["schools"]
#db.create_collection("students")
print(mongo_client.list_database_names())
