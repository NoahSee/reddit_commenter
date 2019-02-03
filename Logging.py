import datetime
import time
import json

class LoggingHandler:

    def __init__(self):
        self.data = []

        # Modifiable
        self.filename = "Log.json"
        self.enteries_to_keep = 10

    def __call__(self,string):
        """
        @string : string
        - Prints string
        - Adds string to log with a timestamp
        """
        print(string)
        now = datetime.datetime.now().strftime("%d%m%y %H:%M:%S") # get timestamp
        logstring = '{} - {}'.format(now,string) # Add timestamp to string
        self.data.append(logstring) # Updata data
        self.data = self.data[-self.enteries_to_keep:] # Keep last N enteries

        # Write file
        f = open(self.filename, "w")
        f.write(json.dumps(self.data))
        f.close()

    def PrintLog(self):
        """
        - Prints Log, for debugging purpose only
        """

        # Read File
        f = open(self.filename, "r")
        data = json.loads(f.read())
        f.close()

        # Print out nicely
        print('PrintLog :',)
        for log in data: print('    ', log)

### Test Portion | Run Logging.py to test ###

if __name__ == "__main__":
    Log = LoggingHandler()
    for i in range(1,20):
        Log( 'Event {}'.format(i) )
    Log.PrintLog()