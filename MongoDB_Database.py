import json
import pymongo

class Database:

    def __init__(self, connectionstring):
        """
        @connectionstring : string : see https://docs.atlas.mongodb.com/driver-connection/
        """
        client = pymongo.MongoClient(connectionstring)
        database = client.MyDatabase
        self.collection = database.SubmissionHistory

    def AddSubmissionRecord(self, data):
        """
        @data : dict
        - Adds dict to database/collection as object
        """
        self.collection.insert_one(data)

    def GetSubmissionRecords(self):
        """
        @output : list of dictionaries
        - Returns database/collection as list of dict
        """
        return [ x for x in self.collection.find() ]

    def ClearSubmissionRecords(self):
        """
        - Deletes databse/collection
        """
        self.collection.drop()

### Test Portion | Run MongoDB_Database.py to test ###

if __name__ == "__main__":

    # (secret)
    with open('secret.json') as f:
        secret = json.loads(f.read())

    # (db)
    db = Database(secret["MongoDB"])

    # Test
    print( db.GetSubmissionRecords() )