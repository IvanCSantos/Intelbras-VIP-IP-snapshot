# Intelbras-VIP-IP-snapshot

### How to use this script
First you must change the getSnapshot.py file by entering the following information:  
URL = the URL to the snapshot utility of your Intelbras camera (format: http://<user>:<password>@<ip>:<HTTPport>/cgi-bin/snapshot.cgi?)  
path = the path to where you wish to save the snapshot

#### Install the dependencies
pip install requests or python -m pip install requests  
pip install Pillow or python -m pip install Pillow  
Note: if you are running this on an Windows Machine, instead of Pillow install Images

#### Run the script
python ./getSnapshot.py