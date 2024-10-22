import machine, time
   
# Setup pins
p = [machine.Pin(i, machine.Pin.OUT) for i in range(18, 22)]
SHCP, STCP, DS, OE = p

def shift(bits):
    OE.value(1)
    for b in bits:
        DS.value(b)
        SHCP.value(1)
        SHCP.value(0)
    STCP.value(1)
    STCP.value(0)
    OE.value(0)
    time.sleep(0.02)


circle_order = [0,13,14,15,4,3,2,1,8,7,6,5,12,9,10,11, ]
while True:
    for position in circle_order:
        pattern = [0] * 16  # Create list of 16 zeros
        pattern[position] = 1  # Turn on current LED
        shift(pattern)
        time.sleep(0.001)  # Speed of rotation

