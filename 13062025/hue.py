# %%
from phue import Bridge
import random
import time

bridge = Bridge("192.168.178.43")

deckenlampe = bridge.get_light_objects("name")["Deckenlampe"]
deckenlampe.on = True
deckenlampe.brightness = 254
for i in range(0, 10):

    deckenlampe.xy = [random.random(), random.random()]
    time.sleep(1)
deckenlampe.on = False
