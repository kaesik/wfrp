import time
czas = time.gmtime()
time.sleep(int(60)-int(czas[5]))
print("Wybiła pełna minuta.")
