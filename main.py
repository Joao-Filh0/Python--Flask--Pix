from flask import Flask,request,jsonify
from flask_cors import CORS
import os
from pix import *

app = Flask(__name__)

CORS(app)

dataResponses = []

#Rota usada para testes do webhook
@app.route("/",methods = ['GET'])
def get_data():

    if len(dataResponses) == 0:
        return jsonify({"message" : "Nada no momento "}), 200
    return jsonify(dataResponses),200

@app.route("/cob",methods = ["POST"])
def web_hooks():
     pix = PixModel()
     result = request.get_json()
     cob = pix.cob(uid = result.get("uid"), data = result.get("data"))
     dataResponses.append(cob)
     

    
     return jsonify({
            "message" : "sucess" ,"payload" : cob }),201

if __name__== '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True,host="0.0.0.0",port=port,threaded=True)
    #,host="0.0.0.0"
