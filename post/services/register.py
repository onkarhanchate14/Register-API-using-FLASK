from post.controller.routes import db
from post.controller.__init__ import *

from post.controller.__init__ import isPresent
from post.model.model import Person
def registerNewUser():
    request_data = request.get_json()
    if(request_data):   
        name1 = request_data["data"]["name"]
        email1 = request_data["data"]["email"]
        password1 = request_data["data"]["password"]
        unique_id = uuid.uuid5(uuid.NAMESPACE_DNS, email1)
        call = isPresent(unique_id)
        if(not call):
            per_1 = Person(person_name=name1,email=email1,password=password1,unique_id=unique_id)
            db.session.add(per_1)
            db.session.commit()
            dic = {"name : ":name1,"email : ":email1,"id : ":unique_id}
            return dic
        else:
            return {"AlreadyRegistered":"this email is already registered , try with different email"}
    else:
        return {"error":"empty data passed"}