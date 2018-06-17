"""This program handles the PCA9685 over I2C
"""

import smbus

class pca9685:
    #Configuration
    Osc = 20000000 # 20 MHz
    Frequency = 50 # 50 Hz
    #Registers
    MODE1 = 0x00
    MODE2 = 0x01
    CHANNEL0 = 0x06
    PRESCALE = 0xFE

    def __init__(self, address, bus=1):
        self.address = address
        self.bus = smbus.SMBus(bus)
        self.prescale = round((self.Osc / (4096 * self.Frequency)) -1)

        self.bus.write_byte_data(self.address, self.MODE1, 0x01)
        self.bus.write_byte_data(self.address, self.MODE1, 0x11)
        self.bus.write_byte_data(self.address, self.MODE1, 0x51)

        self.bus.write_byte_data(self.address, self.PRESCALE, self.prescale)
        self.bus.write_byte_data(self.address, self.MODE1, 0xA1)
        self.bus.write_byte_data(self.address, self.MODE2, 0x04)

        self.tick = 1000000 * (self.prescale + 1.0) / self.Osc

    def OutPut(self, channel, time):
        val = int(round(time / self.tick))
        self.bus.write_byte_data(self.address, channel * 4 + self.CHANNEL0, 0x00)
        self.bus.write_byte_data(self.address, channel * 4 + self.CHANNEL0 + 1, 0x00)
        self.bus.write_byte_data(self.address, channel * 4 + self.CHANNEL0 + 2, val & 0xFF)
        self.bus.write_byte_data(self.address, channel * 4 + self.CHANNEL0 + 3, (val >> 8) & 0x07)