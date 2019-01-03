from datetime import datetime as dt

#local imports
from app.api.db import Database

class IncidentModel(Database):
    """Incident model database"""
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
        created_at = dt.now().strftime(
                '%Y-%m-%d %H:%M:%S')
        status = 'draft'        
        #print("\n",data,"\n")
        self.cursor.execute("""INSERT INTO incidents (user_id, type_of_incident, 
        comment, status, location, created_at)
        VALUES (%s, %s, %s, %s, %s, %s)""", (1,data['type_of_incident'], 
        data['comment'], status, data['location'], created_at))
        #result = self.cursor.fetchall()
        self.commiting()
       # return result


    def update_specific_incident(self, incident_id):
        """fetch specific incident"""
        self.cursor.execute("""UPDATE incidents WHERE
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

    def update_incident_status(self,status):
        """updating incident status"""
        self.cursor.execute("""UPDATE incidents WHERE
        status='%s' """ %(status))
        incident = self.cursor.fetchone()
        self.commiting()
        return incident

    def check_status_draft(self):
        """checking if the status is draft"""
        self.cursor.execute(
            "SELECT * FROM incidents WHERE status=draft")
        result = self.cursor.fetchone()
        return result
        