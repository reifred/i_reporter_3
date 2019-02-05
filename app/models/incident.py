from app.helpers.database import Database

db = Database()


class Incident:
    """ Model for the Incident Record """

    def __init__(self, **kwargs):
        """ Initializing the Incident Model """
        self.title = kwargs.get("title")
        self.createdBy = kwargs.get("createdBy")
        self.createdOn = kwargs.get("createdOn")
        self._type = kwargs.get("_type")
        self.location = kwargs.get("location")
        self.status = kwargs.get("status")
        self.images = kwargs.get("images")
        self.videos = kwargs.get("videos")
        self.comment = kwargs.get("comment")

    @staticmethod
    def get_records(_type):
        """ Get all available records """
        return db.get_incidents(_type)

    @staticmethod
    def add_incident(**incident_details):
        """ Add records to the database """
        return db.add_incident(**incident_details)

    @staticmethod
    def incident_exists(comment, location):
        """ Check whether the record exists """
        return db.incident_exists(comment, location)

    @staticmethod
    def get_specific_record(incident_id, incident_type):
        """ Get the specific record of ID(incident_id) """
        return db.get_red_flag_of_id(incident_id, incident_type)

    @staticmethod
    def update_incident(attribute, value, incident_id, _type):
        """ Update the attribute record of ID(incident id) """
        if attribute == "status":
            return db.admin_update_status(attribute, value, incident_id, _type)
        return db.update_user_incident(attribute, value, incident_id, _type)

    @staticmethod
    def incident_editable(incident_id, incident_type):
        """ Check whether the record can be edited """
        return db.is_record_editable(incident_id, incident_type)

    @staticmethod
    def delete_incident(incident_id, incident_type):
        """ Delete the record from the database """
        return db.delete_user_incident(incident_id, incident_type)

    def convert_to_dict(self):
        return dict(title=self.title, createdBy=self.createdBy,
                    createdOn=self.createdOn, _type=self._type,
                    location=self.location, status=self.status,
                    images=self.images, videos=self.videos,
                    comment=self.comment)
