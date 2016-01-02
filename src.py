import sys
import time
import facebook

#####Galileo GPIO access as ADC##########
def basic_setup():
        try:
                adc0export = open("/sys/class/gpio/export","w")
                adc0export.write("48")
		adc1export = open("/sys/class/gpio/export","w")
		adc1export.write("50")
                adc0export.close()
		adc1export.close()
        except IOError:
                print "INFO : ADC0 already exists,skipping export."
        fp1 = open("/sys/class/gpio/gpio48/direction","w")
	fp3 = open("/sys/class/gpio/gpio50/direction","w")
        fp1.write("in")
	fp3.write("in")
        fp1.close()
	fp3.close()
#definition to read temperature
def write_temp():
        fp2 = open("/sys/bus/iio/devices/iio:device0/in_voltage0_raw","r")
        val =  int(fp2.read())
        val1 = (50*val)/4096
        return str(val1) + " " +"degrees"
        fp2.close()

#definition to read light
def write_light():
        fp4 = open("/sys/bus/iio/devices/iio:device0/in_voltage1_raw","r")
        val_l =  int(fp4.read())
        return val_l
        fp4.close()


basic_setup()

#main definition
def main():
  	cfg = {
    		"page_id"      : "value",
 			"access_token" :"value"   
    	}

	api = get_api(cfg)
	msg = "temperature : "+str(write_temp())+'\n'+"light : "+str(write_light())
	status = api.put_wall_post(msg)

def get_api(cfg):
	graph = facebook.GraphAPI(cfg['access_token'])
	return graph

if __name__ == "__main__":
  main()
