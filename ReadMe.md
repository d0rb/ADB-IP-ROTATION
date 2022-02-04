## ADB IP ROTATE
This an [Python](https://www.python.org/downloads/)  script based on [Android Debug Bridge (adb) ](https://developer.android.com/studio/command-line/adb) shell scripting.
For this to work , you need a Android device with api > 2.2 ( I think…) and developers mode enabled , you also must have your phone connected to the computer through a usb cable , also inorder for the script to run propely you must have ALL apps closed in the backround.
## What is this? 
This scripts simply toggles airplane mode on and off through adb.
## Why?
Most of the mobile carriers will assing a new IP to your device each time a connection is made ( airplane mode off / on ) , Since now days most the residential ISPs will let you sit on one IP address for a long time , mobile carriers won't. 
So if you need to change IPs once in a while,all you need is your android smartphone.
(Instead of buying residential proxies)

## Thins you need to know
You must have all the apps closed and the phone rest without a lockscreen.
The IP will still be could redirected to you , unless it not your phone. ( this is not a proxy..)
Phone is unsable during the operation , using it may break the software form keep on running.
## Getting Started
1 Download the project 
2 Get the needed libaries
3 Install [Google USB Driver](https://developer.android.com/studio/run/win-usb)
```bash
pip install subprocess
pip install rich
pip install requests
```
4 Edit ADB location on line 7.
5 Edit your device namae ( Use emulator -list-avds )

## Run the script
```bash
Connect your phone to the PC , and set data tethering to enable
python ADB_IP_ROTATE.py
```


