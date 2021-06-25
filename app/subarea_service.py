from re import sub
from connectionDB import Database
from flask import Flask, request, jsonify,redirect
from subarea_repository  import SubareaRepository
from model import subarea

class Subarea:
    _subareaRepository = ''
    def __init__(self):
        self._subareaRepository = SubareaRepository()

    def getSubAreas(self):
        
        cur = self._subareaRepository.getSubArea()
        
        dataArray = []
        for row in cur:#cursor
            mySubarea =subarea.SubArea()
            mySubarea.id = row[0]
            mySubarea.subarea_name = row[1]
            dataArray.append(mySubarea.__dict__)
        
        # return jsonify(mysugerencia.__dict__)
        return jsonify(dataArray)


        
    def getSubAreaById(self,id): 
        
        cur = self._subareaRepository.getSubAreaById(id)
        
        dataArray = []
        for row in cur:#cursor
            mySubarea =subarea.SubArea()
            mySubarea.id = row[0]
            mySubarea.subarea_name = row[1]
            dataArray.append(mySubarea.__dict__)
        
        # return jsonify(mysugerencia.__dict__)
        return jsonify(dataArray)