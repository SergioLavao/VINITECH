import csv
import time
import board
import busio
import digitalio
import adafruit_dht
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

def dht_config():
	dht_config.dht = adafruit_dht.DHT11(board.D23)

def spi_config():
	# create the spi bus
	spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
	 
	# create the cs (chip select)
	cs = digitalio.DigitalInOut(board.CE0)
	 
	# create the mcp object
	mcp = MCP.MCP3008(spi, cs)
	 
	# create an analog input channel on pin 0
	spi_config.CH_0 = AnalogIn(mcp, MCP.P0)
	spi_config.CH_1 = AnalogIn(mcp, MCP.P1)

def get_data(data):
	data[0] = spi_config.CH_0.voltage	
	data[1] = spi_config.CH_1.voltage
	data[2] = dht_config.dht.temperature
	data[3] = dht_config.dht.humidity

def save_data(data, fileName):
	with open(fileName,'a', newline='') as f:	
		write = csv.writer(f)
		write.writerow(data)	
	print(data, flush=True)

def clear_data(pos, fileName):
	with open(fileName,'a', newline='') as f:
		f.truncate(pos)

def main():

	labels = ['Peso', 'Luz', 'Temperatura', 'Humedad']
	data = [0,0,0,0]
	dht = 0

	clear_data(0, 'data.csv')
	save_data(labels, 'data.csv')
	spi_config()
	dht_config()

	while True:
		get_data(data)
		save_data(data , 'data.csv')
		time.sleep(1)

if __name__ == "__main__":
    main()