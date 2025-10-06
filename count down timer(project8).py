# import time

# mytime=int(input("enter time in seconds:"))


# while (mytime>=0):
#     print("time remaining",mytime)
#     t1=time.sleep(1)
#     mytime-=1
    
# print("Times up")

   
import time
mytime=int(input("enter time in seconds:"))

for i in range(mytime,-1,-1):
    seconds=i%60
    minutes=int(i/60)%60
    hrs=int(i/3600)%60
    print(f"TIMER: {hrs:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times up")
