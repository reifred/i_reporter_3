from app.helpers.database import Database

db = Database()


class Incident:

    def __init__(self, **kwargs):
        self.createdBy = kwargs.get("createdBy")
        self.createdOn = kwargs.get("createdOn")
        self._type = kwargs.get("_type")
        self.location = kwargs.get("location")
        self.status = kwargs.get("status")
        self.images = kwargs.get("images", [])
        self.videos = kwargs.get("videos", [])
        self.comment = kwargs.get("comment")

    @staticmethod
    def get_records(_type):
        return db.get_incidents(_type)

    @staticmethod
    def add_incident(**incident_details):
        return db.add_incident(**incident_details)

    @staticmethod
    def incident_exists(comment, location):
        return db.red_flag_exists(comment, location)

    @staticmethod
    def get_specific_record(incident_id):
        return db.get_red_flag_of_id(incident_id)

    @staticmethod
    def update_incident(incident_id, attribute, value):
        if attribute == "status":
            return db.admin_update_status(incident_id, attribute, value)
        return db.update_user_incident(incident_id, attribute, value)

    @staticmethod
    def incident_editable(incident_id):
        return db.is_red_flag_editable(incident_id)

    @staticmethod
    def delete_incident(incident_id):
        return db.delete_user_incident(incident_id)

    def convert_to_dict(self):
        return dict(createdBy=self.createdBy,
                    createdOn=self.createdOn, _type=self._type,
                    location=self.location, status=self.status,
                    images=self.images, videos=self.videos,
                    comment=self.comment)
