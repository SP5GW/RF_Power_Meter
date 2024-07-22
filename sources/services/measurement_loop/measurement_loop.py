"""Sample code and test for adafruit_in219"""

import time
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219


i2c_bus = board.I2C()

ina1 = INA219(i2c_bus,addr=0x40)
ina2 = INA219(i2c_bus,addr=0x41)
ina3 = INA219(i2c_bus,addr=0x42)

print("ina219 test")

ina1.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina1.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina1.bus_voltage_range = BusVoltageRange.RANGE_16V

ina2.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina2.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina2.bus_voltage_range = BusVoltageRange.RANGE_16V

ina3.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina3.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina3.bus_voltage_range = BusVoltageRange.RANGE_16V


# measure and display loop
while True:
    bus_voltage1 = ina1.bus_voltage        # voltage on V- (load side)
    shunt_voltage1 = ina1.shunt_voltage    # voltage between V+ and V- across the shunt
    power1 = ina1.power
    current1 = ina1.current                # current in mA

    bus_voltage2 = ina2.bus_voltage        # voltage on V- (load side)
    shunt_voltage2 = ina2.shunt_voltage    # voltage between V+ and V- across the shunt
    power2 = ina2.power
    current2 = ina2.current                # current in mA
    
    bus_voltage3 = ina3.bus_voltage        # voltage on V- (load side)
    shunt_voltage3 = ina3.shunt_voltage    # voltage between V+ and V- across the shunt
    power3 = ina3.power
    current3 = ina3.current                # current in mA
    
    attenuation = -40
    band = "80m"
    
    if band == "160m":
        power_dbm = ((bus_voltage3-2.1734)/0.0297) - attenuation
    elif band == "80m":
        power_dbm = ((bus_voltage3-2.1759)/0.029) - attenuation
    elif band == "60m":
        power_dbm = ((bus_voltage3-2.1814)/0.03) - attenuation
    elif band == "40m":
        power_dbm = ((bus_voltage3-2.1813)/0.0302) - attenuation
    elif band == "20m" or band == "18m":
        power_dbm = ((bus_voltage3-2.1734)/0.0297) - attenuation
    elif band == "15m":
        power_dbm = ((bus_voltage3-2.1746)/0.0298) - attenuation
    else:
        print("unsuported band selected, exiting the program...")
        exit (1);
        
    power_watt = 0.001*(10**(power_dbm/10))
    #power_dbm = (34.48276*bus_voltage3) - 74.88966 - attenuation
    #power_watt = 0.001*(10**(power_dbm/10))
    
    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    #print("PSU Voltage:{:6.3f}V    Shunt Voltage:{:9.6f}V    Load Voltage:{:6.3f}V    Power:{:9.6f}W    Current:{:9.6f}A".format((bus_voltage1 + shunt_voltage1),(shunt_voltage1),(bus_voltage1),(power1),(current1/1000)))
    #print("PSU Voltage:{:6.3f}V    Shunt Voltage:{:9.6f}V    Load Voltage:{:6.3f}V    Power:{:9.6f}W    Current:{:9.6f}A".format((bus_voltage2 + shunt_voltage2),(shunt_voltage2),(bus_voltage2),(power2),(current2/1000)))
    print("PSU Voltage:{:6.3f}V    Shunt Voltage:{:9.6f}V    Load Voltage:{:6.3f}V    Power:{:9.6f}W    Current:{:9.6f}A".format((bus_voltage3 + shunt_voltage3),(shunt_voltage3),(bus_voltage3),(power3),(current3/1000)))
    #print("RMS RF Power: {:6.3f}dBm".format((0.0245*bus_voltage3+2.22443)))
    print("RMS RF Power: {:6.1f}dBm".format(power_dbm))
    print("RMS RF Power: {:6.1f}W".format(power_watt))
    print("")
    print("")
    time.sleep(1)
