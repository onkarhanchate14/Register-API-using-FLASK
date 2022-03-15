from post.controller import *

db = SQLAlchemy(app)
# db.create_all()

@app.route('/')
def start():
    return render_template('homepage.html')


from post.model.model import Person
from post.services.register import registerNewUser


@app.route('/user',methods=["POST","GET"])
def newUser():
    if(request.method=="POST"):
        return registerNewUser()
    else:
        return {"error":"empty data passed"}
            
    
@app.route('/users')
def allUserData():
    cars = Person.query.all()
    final = {}
    final["results"] = [
        {
            "name": car.person_name,
            "email": car.email,
            "id": car.unique_id
        } for car in cars]
    return final
    
    
from post.controller.__init__ import check
@app.route('/users/<email_id>') 
def userdata(email_id):
    if(check(email_id)):
        cars = Person.query.all()
        final = {}
        for ele in cars:
            if(str(ele.email)==str(email_id)):
                return {"name":ele.person_name,"email":ele.email,"id":ele.unique_id}
        
        return "no user found with "+str(email_id)+" this email id."
    else:
        return "please give proper email address"
    
    

'''

{"data":{"name":"onkar",
           "email":"onk@gmail.com"
        }
}
        
        
'''
