import time
import multiprocessing

start = time.perf_counter()

def do_something():
    print("Sleeping 1 sec")
    time.sleep(1)
    print("Done Sleeping...")

processes = []

for p in range(10):
    p = multiprocessing.Process(target=do_something)
    p.start()
    processes.append(p)

for p in processes:
    p.join()



finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")