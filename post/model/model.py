from post.controller.routes import db
class Person(db.Model):
    unique_id = db.Column(db.Text,primary_key=True)
    person_name = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    
    def __init__(self, person_name, email,password,unique_id):
        self.person_name = person_name
        self.email = email
        self.password = password
        self.unique_id = unique_id
        # self.doors = doors