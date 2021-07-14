from connectionDB import Database
from flask import Flask, request, jsonify
 
class EmployeeRepository:

    _db=''
    def __init__(self):
        self._db = Database 

    def getEmployeesAll(self):
        cur = self._db.getDB().cursor()
        cur.execute(" SELECT * FROM employees")  
        return cur


    def getEmployeesPagination(self,skip, limit):
        cur = self._db.getDB().cursor()
        cur.execute('''EmployeesPagination ?,?''',skip,limit)  
        return cur

    def deleteEmployee(self,id):
        cur = self._db.getDB().cursor()
        cur.execute('''DELETE FROM employees WHERE id =?''',format(id))
        cur.commit() 
        return cur

    def insert(self):
        name =request.json['name']  
        lastname =request.json['lastname']
        type_document =request.json['type_document']
        doc =request.json['document']
        id_area =request.json['idArea']
        id_subarea =request.json['idSubarea']        
        cur = self._db.getDB().cursor()
        cur.execute('''insertEmployee ?,?,?,?,?,? ''',type_document,doc,name,lastname,id_area,id_subarea)
        cur.commit() 
        return cur

    def update(self,id):
        id =format(id);
        name =request.json['name']
        lastname =request.json['lastname']
        type_document =request.json['type_document']
        doc =request.json['document']
        id_area =request.json['idArea']
        id_subarea =request.json['idSubarea']
        
        cur = self._db.getDB().cursor()
        cur.execute('''updateEmployee ?,?,?,?,?,?,?''',(id,type_document,doc,name,lastname,id_area,id_subarea))
        cur.commit() 
        return cur  


    