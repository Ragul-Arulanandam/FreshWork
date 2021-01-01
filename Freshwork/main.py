import json
import os

class KVD:
    def __init__(self,filepath='data.json'):
        try:
            if(filepath == 'data.json'):
                self.filelocation = filepath
                self.openfile()
            else:
                self.filelocation = filepath
                filepath = os.path.dirname(filepath)
                if not os.path.exists(filepath):
                    os.makedirs(filepath)
                if not os.path.isfile(self.filelocation):
                    self.openfile()
        except OSError:
            raise OSError("ERROR: INVALID PATH.")

    def openfile(self):
        with open(self.filelocation, 'w') as file:
            json.dump({}, file)

    def sizecheck(self,filepath):
        size = (os.stat(filepath).st_size)
        if size < (1024*1024*1024):
            return 0
        return 1

    def create(self,inputdata):
        if(self.sizecheck(self.filelocation)):
                raise Exception('ERROR : File size is exceeding 1GB')
        with open(self.filelocation,'r') as f:
            data = json.load(f)
            data.update(inputdata)
        with open(self.filelocation,'w') as f:
            json.dump(data,f)
            return data

    def read(self,inputkey):
        with open(self.filelocation,'r') as f:
            data = json.load(f)
            if(inputkey in data):
                return data[inputkey]
            else:
                raise KeyError(f"ERROR:  {inputkey} is INVALID KEY")

    def Del(self,inputkey):
        with open(self.filelocation, 'r') as f:
            data = json.load(f)
            if(inputkey in data):
                del data[inputkey]
                with open(self.filelocation,'w') as f:
                    json.dump(data,f)
                return data
            else:
                raise KeyError(f"ERROR:  {inputkey} is INVALID KEY")


