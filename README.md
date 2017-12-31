# Cam Flooder
Cam flooder tool, gui version.

![alt text](http://i.imgur.com/BmZVXGB.png)


This app was made to experiment with CAM flooding techniques.
Cam flooding techniques are meant to overload network switches.

DISCLAIMER: Please use responsibly.
Unauthorized use of this tool can get you fired and/or prosecuted.
Only use this tool inside a closed lab environment, where you have full authorization to conduct such tests.
Don't test this tool inside a production network.
I'm not responsible if you DoS your network or destroy your switches. USE AT YOUR OWN RISK.

This tool is still very experimental and is using a very crude technique: massive ethernet frame bombardment.
It's been tested against Cisco virtual VIRL switches, and a real Cisco SG300 switch.

I need to do further tests against physical switches, but right now this project is halted for budget reasons.


Before you have fun with this tool, you should understand the following points:

- I'm not responsible if you DoS your network or destroy your switches. USE AT YOUR OWN RISK.

- I STRONGLY advise you to test it inside a closed lab. Failure to do so could result in loss of connectivity inside your whole LAN.

- Start slowly. Be patient. Use the slider with a low value.

- Wait.

- Monitor your outgoing ethernet frames with a network capture tool (Wireshark or tcpdump). 

- Check out your switch CAM table. Use the appropriate command. You need a 'manageable' switch to do so.

- Monitor your switch. It could become unresponsive under very heavy load. Check out for syslog messages like "CPU hog", indicating that your switch's CPU is overloaded.

- If your switch reaches 100% CPU usage, you could DoS your whole LAN.

- Results may vary depending on a lot of factors: brand/model of switch, amount of CAM entries, CPU speed, etc.

- This attack is not stealthy! It is extremely noisy and will get noticed by security software.

- Again, NEVER EVER use this inside a production network. 








