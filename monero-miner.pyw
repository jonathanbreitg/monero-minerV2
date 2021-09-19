wallet = "4AwXfQYFVvADs129ciGpKpeQmw42WF9AA1jiVY5YSa3tN4tyFJeJEiuRZLZeZkkf7RaC1nFMfFzHLjCnGQd2i8nF7hkwfMh"
import os
import subprocess
import os.path
from os import path
if path.exists("xmrig.zip"):
    print("----------------------------------------XMRIG EXISTS AND IS ALREADY INSTALLED----------------------------------------")
else:
    command = "powershell;$client = new-object System.Net.WebClient;$client.DownloadFile('https://github.com/xmrig/xmrig/releases/download/v6.15.0/xmrig-6.15.0-msvc-win64.zip', 'xmrig.zip');Expand-Archive -Path xmrig.zip -DestinationPath xmrig"
    cmd = subprocess.run(command, capture_output=True, shell=True)
    print(cmd.stdout.decode())
    print(cmd.stderr.decode())
print("----------------------------------------SETUP COMPLETED CHECK LOGS TO SEE IF INSTALLED CORRECTLY----------------------------------------")
if path.exists("conifg_example.json"):
    print("----------------------------------------CONFIG FILE ALREADY DOWNLODED----------------------------------------")
else:
    print("----------------------------------------DOWNLOADING CONFIG FILE FROM GITHUB----------------------------------------")
    command = "powershell;$client = new-object System.Net.WebClient;$client.DownloadFile('https://raw.githubusercontent.com/jonathanbreitg/monero-minerV2/main/config.json', 'config_example.json');"
    cmd = subprocess.run(command, capture_output=True, shell=True)
    print(cmd.stdout.decode())
    print(cmd.stderr.decode())
print("----------------------------------------SETTING CONFIG FILE----------------------------------------")
import shutil
shutil.copyfile(src="config_example.json",dst="xmrig\\xmrig-6.15.0\\config.json")
print("----------------------------------------STARTING MINER----------------------------------------")
command = "powershell; ./xmrig\\xmrig-6.15.0\\xmrig.exe"
cmd = subprocess.run(command, capture_output=True, shell=True)
print(cmd.stdout.decode())
print(cmd.stderr.decode())
