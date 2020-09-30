# imports
from flask import Flask
from flask_restful import  Resource,Api
from secure import authenticate,identity
from flask_jwt import JWT,jwt_required

# creating the class object 
app = Flask(__name__)

app.config['SECERT_KEY'] = 'hihellohowareyou'

# wrapping the application using api,jwt call
api = Api(app)
jwt = JWT(app,authenticate,identity)

#memory database which is just a list
languages = []

"""remember all mutations have to take same parameters as arguments say here(self).
returning specific name/search 
"""
class Languages(Resource):
    def get(self,name):
        for lang in languages:
            if lang['name'] == name:
                return lang

        return{'Search Value': None},404 #set status 404 so tat it'll send response 404 instead of success(202).
    
    @jwt_required()
    def post(self,name):
        lang = {'name':name}
        languages.append(lang)
        return lang
    
    @jwt_required()
    def delete(self, name):
        for ind,lang in enumerate(languages):
            if lang['name'] == name:
                deleted_lang = languages.pop(ind)
                return{'note':'delete success'}

# getting all values
class GetAll(Resource):
    def get(self):
        return{'languages':languages}

api.add_resource(Languages,"/language/<string:name>")
api.add_resource(GetAll,"/languages")

if __name__ =='__main__':  
    app.run(debug = True)  