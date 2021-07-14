from flask import Flask, request, jsonify, make_response,redirect
import os

from werkzeug.wrappers import response
from employees_repository import EmployeeRepository 
import json
from employees_service import EmployeeService
from area_service import Area
from subarea_service import Subarea
from flask_cors import CORS

class App:
   
    app = Flask(__name__)
    CORS(app)


    @app.route('/')
    def getEmployees():
        skip=request.args.get('skip')
        limit=request.args.get('limit')
        data = EmployeeService().getEmployees(skip,limit)
        return (data)


    @app.route('/getall',methods=['GET'])
    def getAll():
        data = EmployeeService().getEmployeesAll()
        return(data)


    @app.route('/insert',methods=['POST'])
    def insert():
        EmployeeService().insert()
        return jsonify({"status":200})

        
    @app.route('/delete/<int:id>',methods=['DELETE'])
    def deleteEmployee(id):
        data =EmployeeService().deleteEmployee(id)
        return (data)


    @app.route('/update/<int:id>',methods=['POST'])
    def update(id):
        EmployeeService().update(id)
        return jsonify({"status":200})


    @app.route('/get_areas',methods=['GET'])
    def getAreas():
        data = Area.getAreas()
        return(data)


    @app.route('/get_subareas',methods=['GET'])
    def getSubAreas():
        data = Subarea().getSubAreas()
        return(data)

   
    @app.route('/get_subarea/<int:id>',methods=['GET'])
    def getSubAreaById(id):
        data = Subarea().getSubAreaById(id)
        return(data)


    if __name__ == '__main__':
        app.run( port=3000,debug=True)
