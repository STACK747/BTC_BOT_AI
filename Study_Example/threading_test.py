#thread多线程演示
import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Thread 1 - Number: {i}")
        time.sleep(1)  # 模拟耗时操作

def print_letters():
    for letter in "ABCDE":
        print(f"Thread 2 - Letter: {letter}")
        time.sleep(1)  # 模拟耗时操作

# 创建线程
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# 启动线程
t1.start()
t2.start()

# 等待线程完成
t1.join()
t2.join()

print("Main thread finished.")

