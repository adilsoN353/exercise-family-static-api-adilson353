"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person
app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)
# create the jackson family object
jackson_family = FamilyStructure("Jackson")
John={"first_name":"John",
      "last_name":jackson_family.last_name,
      "age":33,
      "lucky_numbers":[7, 13, 22]}
Jane = {
    "first_name": "Jane",
    "last_name": jackson_family.last_name,
    "age": 35,
    "lucky_numbers": [10, 14, 3]
}
Jimmy = {
    "first_name": "Jimmy",
    "last_name": jackson_family.last_name,
    "age": 5,
    "lucky_numbers": [1]
}
Tommy = {
    "first_name": "Tommy",
    "id": 3443,
    "age": 23,
    "lucky_numbers": [34,65,23,4,6]
}
jackson_family.add_member(John)
jackson_family.add_member(Jane)
jackson_family.add_member(Jimmy)
# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code
# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)
@app.route('/members', methods=['GET'])
def get_all_members():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200
@app.route('/member/<int:id>', methods=['GET'])
def get_member_by_id(id):
        member = jackson_family.get_member(id)
        if member:
            return jsonify(member), 200
        else:
            return jsonify({"error" : "Member not found"}), 404
@app.route('/member', methods=['POST'])
def create_member():
    member=request.get_json()
    if member:
        jackson_family.add_member(member)
        return jsonify(member), 200
    else:
        return jsonify({"error" : "Invalid member"}), 400
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_single_member(id):
    done = jackson_family.delete_member(id)
    return jsonify({"done":done}), 200
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)