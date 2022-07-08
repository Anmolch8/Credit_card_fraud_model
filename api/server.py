import numpy as np
from flask import Flask,request,jsonify
import pickle
import bz2

app=Flask(__name__)
ifile = bz2.BZ2File("ML_PIPELINE/model/fraud-detector.pkl",'rb')
data=pickle.load(ifile)
ifile.close()
@app.route('/')
def test():
    return 'heyeye'
@app.route('/pre')
def predict():
    distance_from_home= float(request.args["home_distance"])
    distance_from_last_transaction=float(request.args["last_transaction"])
    repeat_retailer=int(request.args["retailer"])
    used_card=int(request.args["card"])
    used_pin=int(request.args["pin"])
    online_order=int(request.argsml ["order"])
    perdiction=data.predict([[distance_from_home,distance_from_last_transaction,repeat_retailer,
    used_card,used_pin,online_order]])
    out=perdiction[0]
    return {'prediction':int(out)}  