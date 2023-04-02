# Low Battery Notifier

I'm using i3 wm and noticed it doesn't send any notification when my battery gets low. I had that kind of troubles on different desktop environments before and here is a simple script to fix it.

## Dependencies
I used <b>notify-send</b> to send notifications and <b>psutil</b> to get battery details.

### Notify-send
Run ```notify-send -v``` to check is notify-send installed.

If it isn't, you can run ```sudo apt-get install libnotify-bin``` for Debian based distros.

### Psutil
You can run ```pip install psutil``` to get psutil if it isn't installed already.

## Installation

1- Clone this repo to your local.
```bash
git clone git@github.com:serkan-bayram/low-battery-notifier.git
```

2- Set ```main.py``` to run at startup. If you are using i3 wm you can simply put
```bash 
exec --no-startup-id python3 /path/to/script.py
``` 
in your i3 config.
