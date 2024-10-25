from utils.file_utils import read_xls
from yaml import safe_load
from utils.openspace import Openspace

config = safe_load(open('config.yaml'))
file = config['file']
names = read_xls(file)

#Initialize the default 6 tables with 4 seats
room = Openspace(names)
room.organize()
print(room)

