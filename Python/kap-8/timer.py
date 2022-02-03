import time
startzeit = time.perf_counter()
time.sleep(1)
stopzeit = time.perf_counter()
print(stopzeit - startzeit)