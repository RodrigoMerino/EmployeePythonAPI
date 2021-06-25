from flask import Flask, request, jsonify,redirect
from employees_repository import EmployeeRepository
from model import employee

class EmployeeService:
     
    _employeeRepository = ''

    def __init__(self):
        self._employeeRepository = EmployeeRepository()


    def getEmployees(self,skip,limit,):
        
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
        
    def deleteEmployee(self,id):
        return self._employeeRepository.deleteEmployee(id)

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
