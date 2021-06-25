from connectionDB import Database
from flask import Flask, request, jsonify
 
class AreaRepository:
    _db=''
    def __init__(self):
        self._db = Database

    def getArea(self):
        cur = self._db.getDB().cursor()
        cur.execute(" SELECT * FROM areas")  
        return cur