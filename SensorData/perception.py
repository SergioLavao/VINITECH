import csv
import time
import board
import busio
import digitalio
import adafruit_dht
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

def dht_config():
	'''
	Configura el sensor DHT11 en el puerto GPIO 23
	'''
	dht_config.dht = adafruit_dht.DHT11(board.D23)

def spi_config():
	'''
	Congigura la comunicacion SPI usando el conversor MCP
	'''
	# Configuración bus SPI
	spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
	 
	# Configuración Chip Select
	cs = digitalio.DigitalInOut(board.CE0)
	 
	# MCP con Chip Select y bus SPI
	mcp = MCP.MCP3008(spi, cs)
	 
	# Configuración canales a leer
	spi_config.CH_0 = AnalogIn(mcp, MCP.P0)
	spi_config.CH_1 = AnalogIn(mcp, MCP.P1)

def get_data(data):
	'''
	Almacena los datos adquiridos por SPI y con el sensor DHT11
	'''
	# Guardar datos de voltaje SPI 
	data[0] = spi_config.CH_0.voltage	
	data[1] = spi_config.CH_1.voltage

	# Guardar datos de temperatura y humedad
	data[2] = dht_config.dht.temperature
	data[3] = dht_config.dht.humidity

def save_data(data, fileName):
	'''
	Guarda los datos del vector data en el archivo fileName
	y muestra estos en la terminal
	'''
	with open(fileName,'a', newline='') as f:	
		write = csv.writer(f)
		write.writerow(data)	
	print(data, flush=True)

def clear_data(pos, fileName):
	'''
	Borra el contenido del archivor fileName a partir de la
	posición pos
	'''
	with open(fileName,'a', newline='') as f:
		f.truncate(pos)

def main():

	labels = ['Peso', 'Luz', 'Temperatura', 'Humedad']
	data = [0,0,0,0]

	clear_data(0, 'data.csv')
	save_data(labels, 'data.csv')
	spi_config()
	dht_config()

	while True:
		try:
			get_data(data)
			save_data(data , 'data.csv')
			time.sleep(1)
		except RuntimeError:
			pass
		except KeyboardInterrupt:
			break

if __name__ == "__main__":
    main()