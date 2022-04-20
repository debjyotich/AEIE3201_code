import serial
import time
import numpy as np
import pandas as pd

read_char_num = 7  # don't modify this

# can take user input
no_of_data_points = 20
delay_time_sec = 1
serial_port = "/dev/cu.usbmodem14101"
serial_baud = 9600

sensor_data, data_points = [], []  # define empty lists
ser = serial.Serial(serial_port, serial_baud)
for i in range(0, no_of_data_points):
    serial_data = float(ser.read(read_char_num).decode().strip())
    print(f"The data at {i} is {serial_data}")
    # print("", end="..")
    sensor_data.append(serial_data)
    data_points.append(i)
    time.sleep(delay_time_sec)  # take one second delay
print("\n")

data_avg = round(np.average(sensor_data), 2)
sensor_data_frame = {"S No.": data_points, "Sensor_data": sensor_data}

df_w = pd.DataFrame(sensor_data_frame, columns=["S No.", "Sensor_data"])

df_w.to_csv("results.csv", index=False)

# print(f"The avg. of sensor data {data_avg}")
# print(sensor_data_frame)
