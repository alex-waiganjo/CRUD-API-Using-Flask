from collections import OrderedDict
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# Instantiating the flask app
app = Flask(__name__)

# Database configurations
app.config['SECRET_KEY'] = 'users api'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# passing the app to the database marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)



# Database Instance
class User_details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    residence = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.id

class details(ma.Schema):
    class Meta:
        fields = ("id", "username", "age", "email", "residence")
details_schema = details(many=False)
detailss_schema = details(many=True)


# Post Route
@app.route("/information", methods=["POST"])
def post_route():
    try:
        username = request.json["username"]
        age = request.json["age"]
        email = request.json["email"]
        residence = request.json["residence"]
        response = User_details(
            username=username, age=age, email=email, residence=residence)
        db.session.add(response)
        db.session.commit()
        return details_schema.jsonify(response)
    except Exception as e:
        return jsonify({"ERROR_OCCURED": " SORRY,INVALID REQUEST!!!!"})


# Get Route
@app.route("/information", methods=["GET"])
def get_routes():
    todos = User_details.query.all()
    result = detailss_schema.dump(todos)
    if result == [] or result == None or result == 0:
        return {"Message": " Nothing Found"}
    else:
        return jsonify(result)


# Get route by id
@app.route("/information/<int:id>", methods=["GET"])
def get_route(id):
    todo = User_details.query.get_or_404(int(id))
    return details_schema.jsonify(todo)


# Update Route by id
@app.route("/information/<int:id>", methods=["PUT"])
def update_route(id):
    todo = User_details.query.get_or_404(int(id))
    username = request.json["username"]
    age = request.json["age"]
    email = request.json["email"]
    residence = request.json["residence"]
    todo.username = username
    todo.age = age
    todo.email = email
    todo.residence = residence
    db.session.commit()
    return details_schema.jsonify(todo)


# Delete Route by id
@app.route("/information/<int:id>", methods=["DELETE"])
def delete_route(id):
    todo = User_details.query.get_or_404(int(id))
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"HTTP 200 Success": "Record Deleted Successfully!!!"})


# Run app
if __name__ == '__main__':
    app.run(debug=True)
