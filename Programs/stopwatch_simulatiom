import time 
import random 
n = int(input("Enter number of intervals: "))
total_time = 0 
print("Stopwatch simulation started...\n") 
for i in range(n): 
    interval = random.randint(1, 3)   # random delay between 1 and 3 seconds 
    start = time.time() 
    time.sleep(interval) 
    end = time.time() 
    elapsed = end - start 
    total_time += elapsed 
    print(f"Interval {i+1}: {elapsed:.2f} seconds") 
average_time = total_time / n 
print("\nAverage elapsed time:", round(average_time, 2), "seconds")
