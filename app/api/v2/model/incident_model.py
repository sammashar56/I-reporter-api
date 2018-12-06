from app.api.v2.db import Database

class IncidentModel(Database):
    """Incident model database"""
    def __init__(self):
        super().__init__()
    
    def get_all_incidents(self):
        """fetch all incidents"""
        self.cursor.execute("SELECT * FROM incidents"
        )
        result = self.cursor.fetchall()
        return result

    def get_specific_incident(self, incident_id):
        """fetch specific incident"""
        self.cursor.execute("""SELECT * FROM incidents WHERE
        incident_id='%s' """ %(incident_id))
        incident = self.cursor.fetchone()
        return incident

    def add_incident(self, data):
        """create an incident"""
        self.cursor.execute("""INSERT INTO incidents(incident_id, 
        type_of_incident, comment, status, location, created_at)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""")%(data['incident_id'], data['type_of_incident'], 
        data['comment'], data['status'], data['location'], data['created_at'])
        self.commiting()
        return data


    def update_specific_incident(self, incident_id):
        """fetch specific incident"""
        self.cursor.execute("""UPDATE  incidents WHERE
        incident_id='%s' """ %(incident_id))
        incident = self.cursor.fetchone()
        self.commiting()
        return incident
    
    def delete_specific_incident(self, incident_id):
        """delete a specific incident"""
        self.cursor.execute("""DELETE FROM incidents WHERE incident_id ='%s'
        """ %(incident_id))
        incident = self.cursor.fetchone()
        self.commiting()
        return incident
