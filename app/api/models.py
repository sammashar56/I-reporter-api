incidents = []

from datetime import datetime as dt

class Models():
    def __init__(self):
        self.db = incidents

    def add_record(self, data):
        id = len(self.db)+1
        data['id'] = id
        data['creation date'] = dt.now().strftime(
                '%Y-%m-%d %H:%M:%S')
        data['status'] = None
        incidents.append(data)