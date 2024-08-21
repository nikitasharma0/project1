import time
from plyer import notification

if __name__ == "__main__":
  while True:
    notification.notify(
      title="MEDSS!!!",
      message="Time to take daily med.",
      app_icon="medical icon.ico",
      timeout=10
    )
    time.sleep(54000)