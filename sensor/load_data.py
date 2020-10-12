import os
import glob
import csv

sensor_data = load_sensor_data()
sensor_files = glob.glob(os.path.join(os.getcwd(),'datasets','csv'))

for sensor_files(sensor_file):
with = open(sensor_file,'r') as data_file

data_reader = csv.DictReader(data_file(delimiter=',',[]))
