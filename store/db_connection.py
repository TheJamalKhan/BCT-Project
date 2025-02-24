import pymongo
import pymongo.mongo_client

url ="mongodb+srv://mdjamalk50:RLaeXvgGGdcirkfJ@cluster0.3238v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client =pymongo.MongoClient(url)

db = client["store"]