# from concurrent.futures import ProcessPoolExecutor
# import time

# def double(x):
#     time.sleep(1)
#     return x * 2

# if __name__ == "__main__":
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         results = executor.map(double, [10, 20, 30, 40])

#     print(list(results))  # 输出: [20, 40, 60, 80]


# import time
# from concurrent.futures import ThreadPoolExecutor

# def square(x):
#     time.sleep(1)
#     print(f"Processing {x}")
#     return x * x

# with ThreadPoolExecutor(max_workers=3) as executor:
#     futures = [executor.submit(square, i) for i in range(5)]
#     for future in futures:
#         print(future.result())

# # a:/note/Code/python并发.py
# # Processing 0
# # Processing 1
# # Processing 2
# # 0
# # 1
# # 4
# # Processing 4
# # Processing 3
# # 9
# # 16