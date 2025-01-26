import time

def Function():
    print("Currently In Function....")
    print("Sleep For 1 Sec....")
    time.sleep(1)
    print("Done With Sleep....")

start=time.perf_counter()
# Calling Function() 4 Times....
Function()
Function()
Function()
Function()
end=time.perf_counter()
print(f"Time Taken By Function: {int(end-start)} Sec")