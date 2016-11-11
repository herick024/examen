import json

class Data:
    data = []

    def __init__(self):
        pass

    def data_read(self,file_name):
        with open(file_name,"r") as file:
            self.data = json.load(file)


    def data_get_data(self):
        return self.data
