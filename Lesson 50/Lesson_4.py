#from datetime import time
import time

print(time)
start_time = time.time()
print(time.ctime())
time.sleep(2.5)
end_time = time.time()
print(end_time - start_time)
print()

new_time = time.time()

my_range = range(100000)
print(my_range[100])

new_end_time = time.time()
print("Total duration of the operation: ", new_end_time - new_time)
