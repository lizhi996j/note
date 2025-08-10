## cocurrent 包
### executor.submit()
例子：
运行executor.submit()后会立即返回features对象；
submit将任务提交给线程池，由线程数运行；
使用for feature in features是会阻塞，输出结果顺序与features列表顺序一致；
使用for feature in as_completed(features)是会阻塞，输出结果顺序与features列表顺序不一致,按运行顺序输出；
```python
import time
from concurrent.futures import ThreadPoolExecutor

def square(x):
    time.sleep(1)
    print(f"Processing {x}")
    return x * x

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(square, i) for i in range(5)]
    for future in futures:
        print(future.result())

# a:/note/Code/python并发.py
# Processing 0
# Processing 1
# Processing 2
# 0
# 1
# 4
# Processing 4
# Processing 3
# 9
# 16
```

## multiprocessing 包(多进程), threading 包(多线程)
- multiprocessing.Process 用于创建进程。
- multiprocessing.Pool 提供了一个进程池，用于并行处理多个任务。
- Queue 和 Pipe 用于进程间通信。
- Manager 用于共享数据。
Queue适用于简单的数据传递，比如生产者-消费者模型； Manager适用于更复杂的场景；