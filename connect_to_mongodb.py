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
print("11111111111111 Success here 111111111111111")


myclient = mongo_client
print(myclient.list_database_names())

dblist = myclient.list_database_names()
db = "mydatabase"
if db in dblist:
    print(db," database exists.")
else:
    print(db, " database does not exist")
print("222222222222222 Success here 22222222222222")

CONNECTION_STRING = 'mongodb://localhost:27017'
mongo_client = MongoClient(CONNECTION_STRING)
db = mongo_client["schools"]
#db.create_collection("students")
print(mongo_client.list_database_names())
print("333333333333 Success here 33333333333333333")
