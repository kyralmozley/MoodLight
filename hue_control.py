import requests
import json

#hue credentials
ip = "192.168.0.102"
username = "zANpoSDY77TrMmACDUMyrJY7O9fU-gmhJqQzfH1-"
url = "http://" + ip + "/api/" + username + "/lights/3/state"

def controlHue(emotion):
    settingsDir = {
        #colour to emotion matching
        'anger': {"on": True, "sat": 254, "bri": 254, "hue": 65535},        #red
        'fear': {"on": True, "bri": 254, "hue": 64571, "sat": 253},         #red
        'anticipation': {"on": True, "bri": 254, "hue": 15974, "sat": 252}, #orange
        'surprise': {"on":True,"bri":254,"hue":49657,"sat":245},            #purple
        'sadness': {"on": True, "bri": 254, "hue": 19912, "sat": 252},      #dark blue
        'joy': {"on": True, "bri": 254, "hue": 19912, "sat": 252},          #yellow
        'disgust': {"on": True, "bri": 254, "hue": 46624, "sat": 251},      #green
        'negative': {"on": True, "bri": 254, "hue": 19912, "sat": 252},     #blue
        'positive': {"on": True, "bri": 254, "hue": 33016, "sat": 53}       #white
    }

    setting = settingsDir.get(emotion)
    r = requests.put(url, json.dumps(setting), timeout=5)