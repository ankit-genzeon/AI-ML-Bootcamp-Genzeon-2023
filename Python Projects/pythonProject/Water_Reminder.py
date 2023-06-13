from plyer import notification
import time

if __name__ == "__main__":
    while True:
        try:
            notification.notify(
                title="Please Drink Water",
                timeout=10
            )
        except Exception as e:
            print("Error displaying notification:", str(e))
        time.sleep(60)
