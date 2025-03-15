import multiprocessing
import threading
import time
#在实际项目中，threading 模块通常用于并发执行任务，比如处理 I/O 操作、网络请求或后台任务，而
#不会阻塞主线程的执行。下面给你一个实际项目的示例，比如在一个 Web 应用或后台服务中，使用多线程处理日志记录和数据处理。
#假设你有一个系统，它需要定期从某个数据源获取数据并写入日志，同时执行计算任务。我们可以用 threading 来实现这个并发处理，以提高效率。
#如何在项目中使用 threading？
# 避免阻塞主线程：如果你的程序需要执行多个任务（如日志记录、定期刷新数据、与外部 API 交互等），可以用 threading 来并行执行它们，而不会影响主业务逻辑。
# 提高 I/O 任务效率：比如在爬虫项目中，多个线程可以同时发送请求，提高爬取效率。
# 后台任务：在 Flask 或 Django Web 应用中，可以使用线程来处理异步任务，如发送邮件、处理用户上传文件等。
#另： 线程是进程内的一个执行单元，它共享进程的内存空间。
# Python 的 threading 模块创建的线程是 真正的系统级线程，但 Python 线程受 GIL 影响，不能真正并行运行 Python 代码（计算任务）。
# 操作系统会调度这些线程，并可能把不同的线程分配到不同的 CPU 核心上执行（但 Python 线程仍然是 伪并行，因为 GIL 只允许一个 Python 线程运行 Python 代码）。
#如果你希望让 Python 真正使用多个 CPU 核心，你应该使用 multiprocessing 而不是 threading：
#import multiprocessing
#def compute(x):
#    return x * x
#if __name__ == "__main__":
#   with multiprocessing.Pool(4) as pool:  # 4 个 CPU 核心并行计算
#       results = pool.map(compute, range(10))
#   print(results)


# 模拟数据采集任务
def fetch_data():
    for i in range(5):
        print(f"[{time.strftime('%H:%M:%S')}] Fetching data {i}...")
        time.sleep(2)  # 模拟网络请求或数据库查询

# 模拟日志写入任务
def write_logs():
    for i in range(5):
        print(f"[{time.strftime('%H:%M:%S')}] Writing log entry {i}...")
        time.sleep(1)  # 模拟日志写入延迟

# 创建两个线程来执行这两个任务
thread1 = threading.Thread(target=fetch_data)
thread2 = threading.Thread(target=write_logs)

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()

print("All tasks completed.")
