"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = []
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    def add_member(self, member):
        # fill this method and update the return
        if "id" not in member:
            new_person = {
            "id":self._generateId(),
            "first_name":member["first_name"],
            "last_name":self.last_name,
            "age":member["age"],
            "lucky_numbers":member["lucky_numbers"]
        }
        else:
            new_person = {
                "id":member["id"],
                "first_name":member["first_name"],
                "last_name":self.last_name,
                "age":member["age"],
                "lucky_numbers":member["lucky_numbers"]
            }
        self._members.append(new_person)
        return new_person
# Ten en cuenta que el diccionario que envía la solicitud POST puede contener una propiedad y un valor para el id del miembro a crear.
# Si no lo incluye, tu API debe generar un id aleatorio al agregarlo a la familia.
# Si lo incluye, entonces este es el valor que deberás usar como id al agregarlo.
    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False
    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                return member
        return None
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members