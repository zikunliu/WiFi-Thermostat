import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #fan 
GPIO.setup(13, GPIO.OUT) #cool
GPIO.setup(15, GPIO.OUT) #valve



def AC_Running_Function(mode_state, set_temp,cur_temp,fan_state):
        if(fan_state=='On'):
            GPIO.output(11,True)
        else:
            GPIO.output(11,False)

        if(mode_state=='cool'): 
            GPIO.output(15, False)
            if(cur_temp>set_temp):
                GPIO.output(13, True)
                GPIO.output(11,True)
                GPIO.output(15, True)
            if(cur_temp<=set_temp):
                GPIO.output(13, False)
                GPIO.output(15, True)
                if(fan_state=='Auto'):
                        GPIO.output(11,False)

        if(mode_state=='heat'):
            if(cur_temp<set_temp):
                GPIO.output(15, False)
                GPIO.output(13, True)
                GPIO.output(11,True)
            if(cur_temp>=set_temp):
                GPIO.output(15, False)
                GPIO.output(13, False)
                if(fan_state=='Auto'):
                        GPIO.output(11,False)

        if(mode_state=='off'):
            GPIO.output(15, False)
            GPIO.output(13, False)

#GPIO.cleanup()         

