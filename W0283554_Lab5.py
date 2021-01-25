#Part 1:
# from gpiozero import Button # import module LED
# from gpiozero import LED # import module LED
# from time import sleep
# button = Button(2)
# led = LED(17)
# 
# while True:
#     if button.is_pressed:
#         print("Pressed")
#         led.on() #set the GPIO 17 to high
#     else:
#         print("Released")
#     led.off()#set tje GPIO 17 to low
#     sleep(1)

#Part2.1
# from gpiozero import PWMLED
# from time import sleep
# 
# led = PWMLED(17)
# 
# while True:
#     led.value = 0 #off
#     sleep(1)
#     led.value = 0.5 #half brightness
#     sleep(1)
#     led.value = 1 # full brightness
#     sleep(1)

#Part2.2
import math
from gpiozero import PWMLED
from time import sleep
blvl = 10
led = PWMLED(17)

for j in range(0, 2):
    for i in range(0, 4):
        led.value = math.sin((i/blvl)*math.pi)
        sleep(1/0.3)
        i+=1
    led.value = math.sin(0)

# while True:
#     led.value = math.sin(math.pi) #off
#     sleep(3.33)
#     led.value = math.sin(math.pi/4) #half brightness
#     sleep(3.33)
#     led.value = math.sin(math.pi/2) # full brightness
#     sleep(3.33)