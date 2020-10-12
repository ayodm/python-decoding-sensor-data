import os
import glob
import csv

sensor_data = load_sensor_data()
sensor_files = glob.glob(os.path.join(os.getcwd(),'datasets','csv'))

for sensor_file in sensor_files:
    with open(sensor_file,'r') as df
    data_file = df.readlines()
    data_reader = csv.DictReader(data_file(delimiter=',',[]))
