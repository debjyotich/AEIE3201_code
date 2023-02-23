import serial
import time
import numpy as np
import pandas as pd

sensor_data, data_points = [], []  # define empty lists


class serial_read:
    def __init__(self, serial_port, serial_baud):
        self.serialPort = serial_port
        self.serialBaud = serial_baud

    def serialConnect(self, no_of_data_points, read_char_num, delay_time_sec):
        ser = serial.Serial(self.serialPort, self.serialBaud)
        for i in range(0, no_of_data_points):
            serial_data = float(ser.read(read_char_num).decode().strip())
            print(f"The data at {i} is {serial_data}")
            # print("", end="..")
            sensor_data.append(serial_data)
            data_points.append(i)
            time.sleep(delay_time_sec)  # take one second delay
        print("\n")

    def calcAvg(self):
        return round(np.average(sensor_data), 2)

    def printCSV(self, file_name):
        sensor_data_frame = {"S No.": data_points, "Sensor_data": sensor_data}
        df_w = pd.DataFrame(sensor_data_frame, columns=["S No.", "Sensor_data"])
        df_w.to_csv(file_name, index=False)
