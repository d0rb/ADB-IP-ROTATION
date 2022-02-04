import subprocess
import time
from rich.console import Console
import requests

version = '1.0.0'
adb = "E:\\android-SDK\\platform-tools\\adb.exe" # Please edit with your own path.
phone_id = 'RZ8MC0Q0Y5Y' # Use emulator -list-avds to find your device name.
jsonfile = ''
console = Console()
cmdAirPlane_show = adb+" -s "+phone_id+" shell am start -a android.settings.AIRPLANE_MODE_SETTINGS" # load airplane screen activity
cmdAirPlane_on = adb+" -s "+phone_id+" shell settings put global airplane_mode_on 0" # setting airplane mode on.
cmdAirPlane_off = adb+" -s "+phone_id+" shell settings put global airplane_mode_on 1" # setting airplane mode off.
cmdAirPlane_show_close_openapps =  adb+" -s "+phone_id+" shell  input keyevent KEYCODE_APP_SWITCH" # load the taskbar screen.
cmdAirPlane_show_close_choose_app =  adb+" -s "+phone_id+" shell input keyevent 23" # choose the lastest app.(cmdAirPlane_show)
cmdAirPlane_show_close_del =  adb+" -s "+phone_id+" shell input keyevent DEL"  # stop the app from running. (cmdAirPlane_show)
cmd_wake_up = adb+" -s "+phone_id+" shell input keyevent KEYCODE_WAKEUP" # wake up the phone.
cmd_fake_tap =  adb+" -s "+phone_id+" shell  input tap 500 500" # Fake tap to overcome a bug where the phone would randomly load other app on desktop.

hostname = ''
country = ''

sleep_interval = 1800

# Noice api giving us some info but mosltly the ip.
def getCurrnetIP():
    global hostname,ip_addr,country
    json = requests.get('http://ipinfo.io/json',proxies={'http':'','https':''}).json()
    try:
        hostname = json['hostname']
        country = json['country']
    except KeyError:
        hostname = 'Unknown'

    console.print("Country : "+json['country'], style="bold yellow")
    console.print("Hostname : "+hostname, style="bold yellow")
    console.print("IP : "+json['ip'], style="bold yellow")

def adbControl():
    console.print("Strating..", style="bold green")
    subprocess.Popen(cmd_wake_up)
    time.sleep(3)
    subprocess.Popen(cmdAirPlane_show)
    time.sleep(2)
    subprocess.Popen(cmdAirPlane_off)
    time.sleep(2)
    subprocess.Popen(cmdAirPlane_on)
    time.sleep(2)
    subprocess.Popen(cmdAirPlane_show_close_openapps)
    time.sleep(2)
    subprocess.Popen(cmdAirPlane_show_close_choose_app)
    time.sleep(2)
    subprocess.Popen(cmdAirPlane_show_close_del)
    time.sleep(2)
    subprocess.Popen(cmd_fake_tap)
    time.sleep(5)
    
    getCurrnetIP()
    console.print("Sleeping "+str(sleep_interval)+" secondes..", style="bold blue")
    
    time.sleep(sleep_interval)
    
    console.print("Hello!", style="bold cyan")
    adbControl()
def main():
    
    console.print("ADB ROTATION LOADED", style="bold green")
    console.print("Version : "+version, style="bold cyan")
    console.print("This is a free , open source project visit me on github : https://github.com/D0rb/", style="bold red")
    
    getCurrnetIP()
    adbControl()
if __name__ == "__main__":        
    main()
