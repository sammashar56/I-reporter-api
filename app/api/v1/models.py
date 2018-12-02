incidents = []
users = []

from datetime import datetime as dt

class Models():
    def __init__(self):
        self.users = users
        self.db = incidents
        
    def add_record(self, data):
        id = len(self.db)+1
        data['id'] = id
        data['created_by'] = data['id'] = id
        data['creation date'] = dt.now().strftime(
                '%Y-%m-%d %H:%M:%S')
        data['status'] = None
        
        self.db.append(data)

    def add_user(self, data):
        id = len(self.users)+1
        data['id'] = id
        self.users.append(data)

    def get_specif_record(self, id):
        ident = [incident for incident in self.db if incident['id'] == id]
        return ident
        
    def delete_incident(self, id):
        for i in incidents:
            if i['id'] == id:
                incidents.remove(i)
                
        
    def get_all_incidents(self):
        return self.db