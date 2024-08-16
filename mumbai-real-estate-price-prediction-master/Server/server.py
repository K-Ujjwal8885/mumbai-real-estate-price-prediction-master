from flask import Flask, request, jsonify
from flask_cors import cross_origin,CORS
import utility
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': utility.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['GET','POST'])
@cross_origin()
def predict_home_price():
    Area = float(request.form['Area'])
    Location = request.form['Location']
    bhk = int(request.form['bhk'])
    New_or_Resale = int(request.form['New_or_Resale'])
    Gymnasium = int(request.form['Gymnasium'])
    Lift_Available = int(request.form['Lift_Available'])
    Car_Parking = int(request.form['Car_Parking'])
    Clubhouse = int(request.form['Clubhouse'])
    Gas_Connection = int(request.form['Gas_Connection'])
    Jogging_Track = int(request.form['Jogging_Track'])
    Swimming_Pool = int(request.form['Swimming_Pool'])
    print(request.form['Area'])

    response = jsonify({
        'estimated_price': utility.get_estimated_price(Location,Area,New_or_Resale,Gymnasium,Lift_Available,Car_Parking,Clubhouse,Gas_Connection,Jogging_Track,Swimming_Pool,bhk)
    })
    # response.headers.add("Access-Control-Allow-Origin", "")
    # response.headers.add("Access-Control-Allow-Headers", "")
    # response.headers.add("Access-Control-Allow-Methods", "*")
    return response

if __name__ == "__main__":
    print("Start Python Flask Server for Real Estate Price Prediction")
    utility.load_saved_artifacts()
    cors = CORS(app)
    # print(utility.get_location_names())
    # print(utility.get_estimated_price('Vashi',10000,0,1,0,1,1,0,1,1,2))
    app.run(debug=True)


