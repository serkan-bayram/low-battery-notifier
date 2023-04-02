import subprocess
import time
import psutil

# Setting when to send notification
LOW_BATTERY_THRESHOLDS = {
            range(0,6): "Just let me die at this point.",
            range(6,11): "You have to hurry.",
            range(11,21): "Put me on charge."
        }
# Setting how often we check
NOTIFICATION_INTERVAL = 60
# Creating a set to check which ranges used.
SENT_THRESHOLDS = set()

# Sending notification with notify-send
def sendNotification(message):
    subprocess.Popen(['notify-send', message])

def main():
    # Get battery details
    battery = psutil.sensors_battery()

    if battery is None:
        # Battery information is not available
        return

    percent = int(battery.percent)
    status = battery.power_plugged
    
    pairs = LOW_BATTERY_THRESHOLDS.items()
    # Not charging
    if not status:
        for threshold, message in pairs:
            # Checking that did we send notification for the current percentage
            if percent in threshold and threshold not in SENT_THRESHOLDS:
                # Dimming the screen for only once if percentage is one of these ranges
                if len(SENT_THRESHOLDS) == 0: subprocess.Popen(["brightnessctl", "set", "5%"])
                sendNotification(f"Your remaining battery is {percent}%.\n{message}")
                SENT_THRESHOLDS.add(threshold)
    else:
        # Clearing the sent thresholds if the device started to charging
        SENT_THRESHOLDS.clear()



if __name__ == "__main__":
    sendNotification("Low battery notifier is working now.")

    while True:
        main()
        time.sleep(NOTIFICATION_INTERVAL)
