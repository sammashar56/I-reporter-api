from datetime import datetime as dt

user = []
incident = []

class UsersModel():
    def __init__(self):
        self.user = user

    def add_user(self, data):
        id = len(self.user) +1
        data['id'] = id
        self.user.append(data)

        
class IncidentModel():
    def __init__(self):
        self.incident = incident

    def add_incident(self, data):
        id = len(self.incident) +1
        data['id'] = id
        data['created_by'] = data['id'] 
        data['creation date'] = dt.now().strftime(
                '%Y-%m-%d %H:%M:%S')
        data['status'] = None      
        self.incident.append(data)

    def get_specif_incident(self, id):
        ident = [incident for incident in self.incident if incident['id'] == id]
        return ident
        
    def delete_incident(self, id):
        for i in self.incident:
            if i['id'] == id:
                self.incident.remove(i)

    def get_all_incidents(self):
        return self.incident
                
