"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
                ## Append the member to the list of _members
        

    def delete_member(self, id):
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        pass

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
        
                ## You have to implement this method
        ## Loop all the members and return the one with the given id
        

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members