from pymongo import MongoClient
client=MongoClient()
db=client['products']
prod_info=db['products'].find_one({"product_name":"tea"})
print(prod_info,type(prod_info))
print(dict(prod_info))