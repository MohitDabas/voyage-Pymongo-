from flask import Flask,jsonify
from bson import json_util
import json
app=Flask(__name__)
from pymongo import MongoClient
client=MongoClient()
db=client['products']


@app.route('/getproduct/data/<product_name>')
def getproduct_data(product_name):
    prod_info=db['products'].find_one({"product_name":"tea"},{'_id':0})
    print(dict(prod_info))
    return json.dumps(dict(prod_info))
  
    
if __name__=="__main__":
    app.run(debug=True)



