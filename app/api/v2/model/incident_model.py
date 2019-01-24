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
        self.cursor.execute("""INSERT INTO incidents (user_id, type_of_incident,title, 
        comment, status, location, created_at)
        VALUES (%s, '%s', '%s', '%s', '%s', '%s', '%s')"""%(data['user_id'], data['type_of_incident'], data['title'],
        data['comment'], status, data['location'], created_at))
        #result = self.cursor.fetchall()
        self.commiting()
       # return result
    
    def update_incident_status(self, status, incident_id):
        """update incident status"""
        self.cursor.execute("""UPDATE incidents SET
        status='%s' WHERE incident_id='%s'  """ %(status, incident_id))
        
        self.commiting()
         
    def update_location_only(self, location, incident_id):
        """update location of an incident"""
        self.cursor.execute("""UPDATE incidents SET location='%s' WHERE incident_id='%s'"""%(location,incident_id))
        self.commiting()

    def update_comment_only(self, comment, incident_id):
        """update comment of an incident"""
        self.cursor.execute("""UPDATE incidents SET comment='%s' WHERE incident_id='%s'"""%(comment ,incident_id))
        self.commiting()
    
    def update_title_only(self, title, incident_id):
        """update title of an incident"""
        self.cursor.execute("""UPDATE incidents SET title='%s' WHERE incident_id='%s'"""%(title, incident_id))
        self.commiting()

    
    def delete_specific_incident(self, incident_id):
        """delete a specific incident"""
        self.cursor.execute("""DELETE FROM incidents WHERE incident_id ='%s' AND status='draft'
        """ %(incident_id))
        self.commiting()
        return incident_id
        

    # def update_incident_status(self,status):
    #     """updating incident status"""
    #     self.cursor.execute("""UPDATE incidents WHERE
    #     status='%s' """ %(status))
    #     incident = self.cursor.fetchone()
    #     self.commiting()
    #     return incident

 
        