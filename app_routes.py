# app_routes.py

from flask import jsonify
from data_functions import get_data
from response_handler import CustomResponse

def index():
    dfk = get_data()
    
    # Creating a CustomResponse with dynamic data
    response = CustomResponse(data=dfk.to_dict(orient='records'))

    # Converting the response to JSON format
    json_response = response.to_json()
    return jsonify(json_response)
