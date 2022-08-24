import json

filename_origin = "Earthquake_data.json"
filename_destination = "Readable_eq_data.json"

class Eq_data_converter:
    def __init__(self):
        '''no particular attributes needed'''

    def load_data(self):
        with open(filename_origin) as file_origin:
            all_eq_data = json.load(file_origin)
            return all_eq_data

    def store_data_as_readable(self):
        source_file = self.load_data()
        with open(filename_destination, "w") as file_destination:
            json.dump(source_file, file_destination, indent=4)

my_converter = Eq_data_converter()
my_converter.store_data_as_readable()