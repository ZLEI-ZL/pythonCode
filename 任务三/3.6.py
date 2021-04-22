#e4.2TextProgressBar.py
import time

k = "Starting ... Done!"

for i in range(len(k)):
    print("{}".format(k[i]), end="")
    time.sleep(0.05)
