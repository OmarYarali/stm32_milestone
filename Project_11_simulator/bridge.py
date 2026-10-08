import serial
import pyvjoy

j = pyvjoy.VJoyDevice(1)

ser = serial.Serial('COM10', 115200)

while True:
    line = ser.readline().decode('utf-8').strip()
    channels = line.split(',')

    if len(channels) == 7:
        roll, pitch, throttle, yaw, swA, swB, swC = map(int, channels)

        j.set_axis(pyvjoy.HID_USAGE_X, int((roll - 1000) * 32.768))
        j.set_axis(pyvjoy.HID_USAGE_Y, int((2000 - pitch) * 32.768))
        j.set_axis(pyvjoy.HID_USAGE_Z, int((throttle - 1000) * 32.768))
        j.set_axis(pyvjoy.HID_USAGE_RZ, int((yaw - 1000) * 32.768))
        j.set_button(1, 1 if swA > 1500 else 0)
        j.set_button(2, 1 if swB > 1500 else 0)
        j.set_button(3, 1 if swC > 1500 else 0)