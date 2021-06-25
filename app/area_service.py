import connectionDB 
from flask import Flask, request, jsonify,redirect
from area_repository import AreaRepository
from model import area

class Area:
    @staticmethod
    def getAreas():
    
        cur = AreaRepository().getArea()
        
        dataArray = []
        for row in cur:#cursor
            myArea =area.Area()
            myArea.id = row[0]
            myArea.areaName = row[1]
            dataArray.append(myArea.__dict__)
        
        # return jsonify(mysugerencia.__dict__)
        return jsonify(dataArray)