from flask import Flask, request, jsonify,redirect
from employees_repository import EmployeeRepository
from model import employee
from custom_exceptions import Error
class EmployeeService:
     
    _employeeRepository = ''

    def __init__(self):
        self._employeeRepository = EmployeeRepository()


    def getEmployees(self,skip,limit,):
        try:
            data = self._employeeRepository.getEmployeesPagination(skip,limit)
            
            dataArray = []
            for row in data:#cursor
                myemployee =employee.Employee()
                myemployee.id = row[0]
                myemployee.name = row[1]
                myemployee.last_name = row[2]
                myemployee.doc = row[3]
                myemployee.type_document = row[4]
                myemployee.area_name = row[5]
                myemployee.subarea_name = row[6]
                myemployee.id_area= row[7]
                myemployee.id_subarea = row[8]
                dataArray.append(myemployee.__dict__)
            
            return jsonify(dataArray)
        except:Error
        
    def deleteEmployee(self,id):
        try:
             data = self._employeeRepository.deleteEmployee(id)
             if data == None:
                return jsonify({"status":"bad request"})

             else:
                 return jsonify({"status":200})
        except: 
            return jsonify({"status":"bad request"})
            
    def insert(self):
        return self._employeeRepository.insert()

    def getEmployeesAll(self):
        data = self._employeeRepository.getEmployeesAll()
        dataArray = []

        for row in data:
            myemployee =employee.Employee()
            myemployee.id = row[0]
            myemployee.name = row[1]
            myemployee.last_name = row[2]
            myemployee.doc = row[3]
            myemployee.type_document = row[4]
            myemployee.area_name = row[5]
            myemployee.sub_area_name = row[6]
            dataArray.append(myemployee.__dict__)
        
        return jsonify(dataArray)

    def update(self,id):
        return self._employeeRepository.update(id)

EmployeeRepository().deleteEmployee(112)