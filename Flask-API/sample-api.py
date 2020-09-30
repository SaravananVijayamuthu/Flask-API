# imports
from flask import Flask
from flask_restful import  Resource,Api

# creating the class object 
app = Flask(__name__)

# wrapping the application using api call
api = Api(app)

# create a resource 
class Testing(Resource):
    def get(self):
        return{'Name':'Saravanan Vijayamuthu'}


api.add_resource(Testing,'/')

if __name__ =='__main__':  
    app.run(debug = True)  