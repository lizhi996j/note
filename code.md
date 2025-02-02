### Used Code
#### os module
1. `os.path.dirname(path)`: 返回获取指定路径中目录部分的路径
   ```python
   import os

    script_path = os.path.abspath('其它.ipynb')
   script_dir = os.path.dirname(script_path)
   print(script_dir)
   ```

2. `os.path.abspath(path)`: 返回绝对路径
3. `os.path.realpath(path)`: 去除符号链接(symbolic link)
4. `__file__`: 返回当前文件路径; （如果在包里，则是包的地址）

##### os.system(command)
执行系统命令，返回命令执行结果

#### os.popen(command)
执行系统命令，返回命令执行结果的文件对象.






#### sys module
1. `sys.argv`: 命令行参数
2. `sys.path`: 模块搜索路径
3. `sys.exit()`: 退出程序

#### collections module

#### random module
1. `random.sample(population, k)`: 从population中随机抽取k个元素，返回一个列表；
可以用于数据集的随机抽样；

#### python
###### 标准容器：`list`, `tuple`, `dict`, `set`
 - `list`: 可变，有序，元素可重复
 - `tuple`: 不可变，有序，元素可重复
 - `dict`: key-value对，key不可重复
 - `set`: 不可重复，无序
###### `list` 方法：
  - `append(x)`: 将元素 x 添加到列表的末尾
  - `extend(iterable)`: 将可迭代对象的元素添加到列表的末尾
  ```python
  lst = [1, 2, 3]
  lst.append([4, 5])
  print(lst)  # 输出: [1, 2, 3, [4, 5]]
  list.extend([4, 5])
  print(lst)  # 输出: [1, 2, 3, 4, 5]
  ```
  - `sort(key=None, reverse=False)`: 对列表进行排序
  - `insert(i, x)`: 在索引 i 处插入元素 x
  - `remove(x)`: 删除列表中第一个值为 x 的元素
  - `pop([i])`: 删除索引 i 处的元素，并返回它。如果未指定索引，则删除最后一个元素
  - `clear()`: 删除列表中的所有元素
  - `index(x[, start[, end]])`: 返回列表中第一个出现的元素 x 的索引位置。如果指定了 start 和 end，则在指定的范围内查找
  - `count(x)`: 返回列表中值为 x 的元素的数量
###### `dict` 方法：
  - `get(key[, default])`: 返回键 key 对应的值。如果键不存在，则返回默认值 default
  - `pop(key[, default])`: 删除键 key 对应的值，并返回它。如果键不存在，则返回默认值 default
  - `popitem()`: 删除并返回字典中的一个键值对。字典是无序的，所以不保证删除哪个键值对
  - `clear()`: 删除字典中的所有键值对
  - `update([other])`: 将字典 other 中的键值对添加到字典中。如果键已存在，则覆盖它
  - `keys()`: 返回字典中的所有键
  - `values()`: 返回字典中的所有值
  - `items()`: 返回字典中的所有键值对
  - 迭代字典的方式：
      1. 方式1：
      ```python
      my_dict = {'a': 1, 'b': 2, 'c': 3}
      for key, value in my_dict.items():
      print(key, value)
      ```
      2. 方式2：
      ```python   
      for key in my_dict:
      print(key, my_dict[key])
       ```


###### 可迭代对象：
  - `zip()`: 将多个可迭代对象（如列表、元组等）中的元素打包成一个元组迭代器，每个元组包含来自每个可迭代对象对应位置的元素
  - `enumerate()`: 返回元素和索引
  - `reversed()`: 返回反向迭代器
  - `sorted(iterable, key=None, reverse=False)`: 排序函数
      - `iterable`: 需要排序的可迭代对象（如列表、元组、字符串等）
      - `key`: 一个函数，用于从每个元素中提取用于排序的关键字。如果未指定，则直接比较元素
      - `reverse`: 一个布尔值。如果为 True，则按降序排序；如果为 False（默认值），则按升序排序
###### `list()`, `dict()`
###### `",".join()`: 连成字符串
###### 函数变量
###### 字典解析：
    ```python
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    def my_function(a, b, c):
        print(a, b, c)
    my_function(**my_dict)
    ```
    ```python
    def test4(a, b=2, *args, **kwargs):
        print(a, b, args, kwargs)
    test4(1)
    test4(1, 1)
    test4(1, *(1, 2, 3, 3, 4,))
    test4(1, *(1, 2, 3, 3, 4,), cc=123, c=123)

    lists = ["a", "b"]
    dicts = {"key": 123}
    test4(1, *lists, **dicts)
    ```
###### 创建字典：
    ```python
    dic_values = {'%g' % (line[0]): line[1:] for line in values}
    ```
###### pass
`pass`: 啥也不干
###### 写入 CSV：
    ```python
    with open('file.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    ```
###### 集合操作：
    - 交：`set1 & set2`
    - 并：`set1 | set2`
    - 差：`set1 - set2`
    - 对称差：`set1 ^ set2`

###### yield
 `yield` 是 Python 中的一个关键字，用于定义生成器函数。生成器使用 `yield` 而不是 `return` 来返回值。每次调用生成器的 `__next__()` 方法时，函数执行到 `yield` 语句，返回一个值并暂停执行，直到下一次调用 `__next__()` 才继续从暂停的位置执行。这使得生成器可以一次返回一个值，而不是一次返回所有值，节省内存。

    **示例**：
    ```python
    def simple_generator():
        yield 1
        yield 2
        yield 3

    # 使用生成器
    gen = simple_generator()
    print(next(gen))  # 输出: 1
    print(next(gen))  # 输出: 2
    print(next(gen))  # 输出: 3
    ```
###### filter函数：
```python
filter(function, iterable)
```
  - function: 过滤函数，返回True/False
  - iterable: 可迭代对象（如列表、元组等）
  - 返回一个filter对象，通常需要转换为list
  - 示例：
    ```python
    list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
    ```
  - 输出：
    ```python
    [2, 4]
    ```

###### map函数：
`map()` 函数是 Python 的一个内置函数，用于将一个函数应用到可迭代对象（如列表、元组等）的每个元素上。它返回一个 map 对象（迭代器）。

 **基本语法**：
```python
map(function, iterable, ...)
```

 **常见用法示例**：

  1. **基本使用**：
  ```python
  # 将列表中的每个数字平方
  numbers = [1, 2, 3, 4, 5]
  squared = map(lambda x: x**2, numbers)
  print(list(squared))  # 输出: [1, 4, 9, 16, 25]

  # 将字符串转换为整数
  str_nums = ['1', '2', '3', '4']
  int_nums = map(int, str_nums)
  print(list(int_nums))  # 输出: [1, 2, 3, 4]
  ```

  2. **使用自定义函数**：
  ```python
  def multiply_by_two(x):
      return x * 2

  numbers = [1, 2, 3, 4]
  doubled = map(multiply_by_two, numbers)
  print(list(doubled))  # 输出: [2, 4, 6, 8]
  ```

  3. **处理多个迭代器**：
  ```python
  # 将两个列表对应元素相加
  list1 = [1, 2, 3]
  list2 = [10, 20, 30]
  summed = map(lambda x, y: x + y, list1, list2)
  print(list(summed))  # 输出: [11, 22, 33]
  ```

  4. **结合字符串操作**：
  ```python
  # 将所有字符串转为大写
  words = ['hello', 'world', 'python']
  upper_words = map(str.upper, words)
  print(list(upper_words))  # 输出: ['HELLO', 'WORLD', 'PYTHON']
  ```

  重要特点：
  1. map() 返回一个迭代器，需要使用 list() 或其他方式转换才能查看结果
  2. 比列表推导式更适合处理简单的转换
  3. 可以处理多个输入迭代器
  4. 内存效率高，因为它是惰性计算的

  对比列表推导式：
  ```python
  # 使用 map
  numbers = [1, 2, 3, 4, 5]
  squared_map = map(lambda x: x**2, numbers)

  # 使用列表推导式
  squared_list = [x**2 for x in numbers]

  # 两者结果相同，但使用场景可能不同
  ```

  使用建议：
  1. 当需要对序列中的每个元素应用相同的函数时，使用 map()
  2. 当转换逻辑简单时，map() 可能比列表推导式更清晰
  3. 当处理大量数据时，map() 的惰性计算特性可能更有优势
  4. 如果需要更复杂的转换逻辑，可能列表推导式更合适

###### 可迭代对象，迭代器和生成器
1. 可迭代对象
可迭代对象的核心是实现了 `__iter__()` 方法或 `__getitem__()` 方法。
- 常用的可迭代对象有：
    - 列表（list）
    - 元组（tuple）
    - 字符串（str）
    - 字典（dict）
    - 集合（set）
    - range()
- 使用`__iter__()`方法实现可迭代对象：
```python
class MyIterable:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        return iter(self.data)
```
- 使用`__getitem__()`方法实现可迭代对象：
```python
class GetItemExample:
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, index):
        if index >= len(self.data):
            raise IndexError
        return self.data[index]

# 使用示例
getitem_obj = GetItemExample([1, 2, 3])
print(getitem_obj[0])  # 输出: 1
for item in getitem_obj:  # 也可以遍历
    print(item)  # 输出: 1, 2, 3
```
区别：`__iter__`：需要配合 `__next__` 方法一起使用，实现完整的迭代器协议
`__getitem__`：只需要实现一个方法，通过索引访问元素。

- 关于iter函数：
基本语法：`iter(object[, sentinel]) `
    - 关于sentinel(哨兵的意思):

```python
# 使用 sentinel 参数创建迭代器
# 当返回值等于 sentinel 时停止迭代
def readline():
    return input("Enter a line (or 'quit' to stop): ")

# 创建迭代器，当输入 'quit' 时停止
iterator = iter(readline, 'quit')
for line in iterator:
    print(f"You entered: {line}")

```

    - 与for的关系：
    
```python
# for 循环内部实际上是这样工作的：
my_list = [1, 2, 3]

# 这个 for 循环:
for item in my_list:
    print(item)

# 等价于:
iterator = iter(my_list)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break
```
     - 一些应用场景
```python
# 1. 逐行读取文件
with open('file.txt', 'r') as f:
    iterator = iter(f)
    first_line = next(iterator)  # 读取第一行
    second_line = next(iterator)  # 读取第二行

# 2. 遍历字典
my_dict = {'a': 1, 'b': 2}
# 获取键的迭代器
key_iterator = iter(my_dict)
# 获取值的迭代器
value_iterator = iter(my_dict.values())
# 获取键值对的迭代器
item_iterator = iter(my_dict.items())

# 3. 创建无限迭代器
from itertools import count
counter = iter(count())  # 创建一个从0开始的无限计数器
```




2. 迭代器
迭代器是实现了 `__iter__()` 方法和 `__next__()` 方法的对象。

3. 生成器
生成器是一种特殊的迭代器,使用 yield 关键字定义生成器函数,生成器函数执行时不会一次性生成所有值，而是在需要时才生成下一个值,这种"延迟计算"的特性使得生成器特别适合处理大量数据

###### 装饰器
装饰器(Decorator)是 Python 中一个非常重要的特性，它是一种用于修改或增强函数或类功能的设计模式。装饰器本质上是一个函数，它接受一个函数作为参数，并返回一个新的函数，从而在不修改原函数代码的情况下，为其添加新的功能。
```python
def my_decorator(func):
    def wrapper():
        print("在函数执行之前")
        func()
        print("在函数执行之后")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# 调用函数
say_hello()
```



###### 异常
1. try-except-else-finally:
   工作原理:
   - try 块:
     - 尝试执行 try 块中的代码
     - 如果代码正常执行(无异常):
       - 跳过 except 块
       - 执行 else 块(如果存在)
   
   - except 块:
     - 当 try 块发生异常时:
       - Python 停止 try 块执行
       - 检查异常是否与 except 块指定的异常类型匹配
       - 如果匹配,执行对应的 except 块
       - 如果无匹配的 except,异常向上传递(可能导致程序终止)
   
   - finally 块:
     - 无论是否发生异常都会执行
     - 通常用于清理资源

2. raise: 手动抛出异常

3. 常见异常类型:
   - `SyntaxError`: 语法错误
   - `NameError`: 使用未定义的变量
   - `TypeError`: 类型错误
   - `ValueError`: 值错误
   - `IndexError`: 索引错误
   - `KeyError`: 字典键错误
   - `FileNotFoundError`: 文件未找到
   - `ZeroDivisionError`: 除零错误
   - `AttributeError`: 属性错误
   - `ImportError`: 导入错误

4. 自定义异常:
   ```python
   class MyCustomError(Exception):
       def __init__(self, message):
           self.message = message
           super().__init__(self.message)
   
   # 使用自定义异常
   try:
       raise MyCustomError("这是一个自定义错误")
   except MyCustomError as e:
       print(e.message)
   ```

5. 关于异常的处理
- 当使用 `raise Exception` 时:
  - 当前代码立即停止执行
  - 控制权转移到调用代码的上下文
  - 若无异常捕获,程序终止并显示错误信息

- 异常处理:
  - 若有 `try...except` 捕获异常,程序可继续运行。在 `except` 块中可处理异常、清理资源、记录错误
  - 若未捕获异常:
    - 程序终止
    - 输出 traceback 信息
    - 显示异常类型和位置

###### 工厂函数
工厂函数（Factory Function）是一个返回对象的函数，而不是直接返回一个值。它通常用于创建和返回类的实例，允许你在创建对象时封装一些逻辑，从而提供更灵活和可扩展的对象创建方式。
特点：
封装创建逻辑：工厂函数可以包含创建对象所需的复杂逻辑，比如参数验证、条件判断等。
返回不同类型的对象：根据输入参数，工厂函数可以返回不同类型的对象。
提高代码的可维护性：通过集中管理对象的创建，工厂函数可以使代码更易于维护和扩展。
示例：
以下是一个简单的工厂函数示例：
```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_factory(animal_type):
    if animal_type == 'dog':
        return Dog()
    elif animal_type == 'cat':
        return Cat()
    else:
        raise ValueError("Unknown animal type")

# 使用工厂函数创建对象
animal1 = animal_factory('dog')
animal2 = animal_factory('cat')

print(animal1.speak())  # 输出: Woof!
print(animal2.speak())  # 输出: Meow!
```

在这个例子中，animal_factory 是一个工厂函数，根据传入的 animal_type 参数返回不同类型的动物对象。这样，你可以在不直接使用类名的情况下创建对象，从而提高了代码的灵活性和可读性。


###### 魔术方法：
双下划线（__）开头和结尾的方法，用于实现类的特殊行为。通常不需要直接调用它们，而是由 Python 解释器在特定情况下自动调用。
常见的魔术方法：
```python
class MyClass:
    # 构造函数，创建对象时调用
    def __init__(self, value):
        self.value = value
    
    # 字符串表示，str()或print()时调用
    def __str__(self):
        return f"MyClass value: {self.value}"
    
    # 迭代器协议，使对象可迭代
    def __iter__(self):
        return iter([self.value])
    
    # 比较运算符 ==
    def __eq__(self, other):
        return self.value == other.value
    
    # 长度，len()函数调用时使用
    def __len__(self):
        return len(self.value)

class MyList:
    def __init__(self):
        self.data = []
    
    # 使对象可以像列表一样用索引访问
    def __getitem__(self, index):
        return self.data[index]
    
    # 使对象可以像列表一样用索引赋值
    def __setitem__(self, index, value):
        self.data[index] = value
    
    # 使对象可以用加号运算
    def __add__(self, other):
        new_list = MyList()
        new_list.data = self.data + other.data
        return new_list

class Number:
    def __init__(self, value):
        self.value = value
    
    # 当使用 + 运算符时自动调用
    def __add__(self, other):
        return Number(self.value + other.value)
    
    # 当使用 print() 或 str() 时自动调用
    def __str__(self):
        return str(self.value)

# 使用示例
n1 = Number(5)
n2 = Number(3)
result = n1 + n2  # 自动调用 __add__
print(result)     # 自动调用 __str__
```
`__new__()` 用于实例化一个对象；`__init__()` 用于初始化一个对象，`__new__()` 在 `__init__()` 之前被调用
#### numpy module
##### np.Ndarray的生成：
1. 用np.array()创建数组：
```python
numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
```
- 关于copy：
```python
import numpy as np

# 创建原始列表
original = [1, 2, 3]

# copy=True（默认）
arr1 = np.array(original, copy=True)
arr1[0] = 100  # 修改arr1不会影响original
print(original)  # 输出: [1, 2, 3]
print(arr1)      # 输出: [100, 2, 3]

# copy=False
arr2 = np.array(original, copy=False)
# 注意：即使设置copy=False，从Python列表创建numpy数组时
# 仍会进行复制，因为numpy数组和Python列表的内存布局不同

# 但对于numpy数组之间的操作，copy=False会更明显：
arr3 = np.array([1, 2, 3])
arr4 = np.array(arr3, copy=False)  # 创建视图
arr4[0] = 100  # 修改arr4会影响arr3
print(arr3)  # 输出: [100, 2, 3]
print(arr4)  # 输出: [100, 2, 3]
```

2. 初始化数组的方法： 
    2.1 生成0，1数组：
    - np.empty(shape, dtype=float, order='C')
    - np.zeros(shape, dtype=float, order='C')
    - np.ones(shape, fill_value, dtype=None, order='C') #shape是元组形式传递
    - np.zeros_like(a, dtype=None, order='C', subok=True, shape=None) #a是numpy数组
    - np.ones_like(a, dtype=None, order='C', subok=True, shape=None)
    
    2.2 生成均匀分布：
    - np.random.rand(d0, d1, ..., dn) 
    - np.random.random(size=None) size是元组形式传递 注意与np.random.rand()的不同
    ```python
    np.random.rand(2, 3)
    np.random.rand(2, 3, 4)
    ```
    生成随机数范围是0-1之间均匀分布
    - np.random.randint(low, high=None, size=None, dtype=int) #low是下限，high是上限，size是元组形式传递
    
    2.3 生成正态分布：
    - np.random.randn(d0, d1, ..., dn) #生成正态分布随机数;均值为0，标准差为1；
    
    2.4 生成随机整数：
    - np.random.randint(low, high=None, size=None, dtype=int) #low是下限，high是上限，size是元组形式传递

3. 生成指定范围的数组
- np.arrange(start, stop, step, dtype=None)
左闭右开；
- 除此之外还有生成等差/等比数列的方法

4. 从numpy数组直接生成数组
`np.asarray(a, dtype=None, order=None)`与`np.array(a, dtype=None, copy=True, order=None, subok=False, ndmin=0)`：
   1. 相同点：
      - 当数据源不是 ndarray（如列表、元组等）时，np.array 和 np.asarray 的行为一致，都会生成一个新的 ndarray。

   2. 不同点：
      当数据源是 ndarray 时：
      - np.array：复制数据，生成新的 ndarray
      - np.asarray：直接返回引用，不复制数据

   3. 使用建议：
      - 需要确保数据独立性时（不希望原数据被修改影响结果）：使用 np.array
      - 可以接受数据共享时（为了节省内存）：使用 np.asarray



##### Ndarray的属性：
| 属性 | 说明 |
|------|------|
| ndarray.ndim | 数组的维度数量|
| ndarray.shape | 数组在每个维度上的大小。对于二维数组（矩阵），表示其行数和列数。|
| ndarray.size | 数组中元素的总个数，等于 ndarray.shape 中各个轴上大小的乘积。|
| ndarray.dtype | 数组中元素的数据类型。|


- reshape：
**语法**：
array.reshape(shape, order='C')
用于改变数组的形状，而不改变其数据。它返回一个新的数组，具有指定的形状。

**示例**：

```python
import numpy as np

# 创建一个一维数组
a = np.array([1, 2, 3, 4, 5, 6])

# 将一维数组重塑为二维数组
b = a.reshape((2, 3))

print(b)
# 输出：
# [[1 2 3]
#  [4 5 6]]
```

在上述示例中，`reshape` 方法将一维数组 `a` 重塑为一个 2 行 3 列的二维数组 `b`。

##### 切片与索引
有两种切片方式，一种是冒号索引，一种是省略号索引；
索引有基本的整数索引，还有整数数组索引，布尔索引，花式索引；

##### numpy.linalg 包
- `np.linalg.inv(a)`: 计算矩阵的逆
- `np.linalg.eig(a)`: 计算矩阵的特征值和特征向量
- `np.linalg.det(a)`: 计算矩阵的行列式
- `np.linalg.solve(a, b)`: 求解线性矩阵方程
- `np.linalg.cholesky(a)`: Cholesky 分解
##### 运算：
- `np.dot(v1, v2)`: 向量点乘
- `np.linalg.norm(v)`: 向量范数
- `np.sum(a, axis=0)`: 按行求和
##### numpy函数
###### sum函数
   - axis参数是从最外层开始算的，最外层是0层
   - keepdims保留维度的位置。保留位置是说留一位，比如1*1的矩阵
   - where参数可以是条件表达式或与原数组形状兼容的布尔数组，否则报错；

###### where函数

###### np.concatenate()
###### np.expand_dims() , np.expand()
`np.expand_dims(a, axis)`
- `a`: 输入数组
- `axis`: 插入新轴的位置
例子：




###### np.squeeze()
`np.squeeze(a, axis=None)`
- `a`: 输入数组
- `axis`: 要删除的单一维度轴。如果为None，则删除所有单一维度的轴

###### np.unique
`np.unique(a, return_index=False, return_inverse=False, return_counts=False, axis=None)`


3. 高维numpy数组乘法*：
    - **基本规则：**
        - 假设有两个数组 `A` 和 `B`。
        - 如果这两个数组的维度相同，且每个维度的长度相同，那么它们可以进行元素级的乘法。
        - 如果这两个数组的维度不同，或者维度相同但长度不同，那么它们无法进行元素级的乘法。
    - **广播机制：**
        - 如果两个数组的维度数不同，将维度较小的数组的形状前面补1，使得两个数组具有相同的维度数。
        - 然后，从后向前比较两个数组的每一个维度：
            - 如果两个维度的长度相同，或者其中一个维度的长度是1，那么这两个维度是兼容的，可以进行广播。
            - 如果两个维度的长度不相同且都不为1，则无法进行广播，抛出错误。
        - 广播之后，每个数组的形状将是两个数组形状的各个维度的最大值。
        - 在计算过程中，长度为1的维度将沿着该维度重复，以匹配最大长度。
    - **示例**：
        ```python
        import numpy as np

        # 创建两个数组
        A = np.array([[1, 2], [3, 4], [5, 6]])
        B = np.array([[2, 3], [4, 5], [6, 7]])

        # 对两个数组进行元素级乘法
        C = A * B

        print(C)
        # 输出：
        # [[ 2  6]
        #  [12 20]
        #  [30 42]]
        ```




##### 广播机制：
1. 如果数组的维度数不同，将维度较小的数组的形状前面补1，使得两个数组具有相同的维度数。
2. 然后，从后向前比较两个数组的每一个维度：
    - 如果两个维度的长度相同，或者其中一个维度的长度是1，那么这两个维度是兼容的，可以进行广播。
    - 如果两个维度的长度不相同且都不为1，则无法进行广播，抛出错误。
3. 广播之后，每个数组的形状将是两个数组形状的各个维度的最大值。
4. 在计算过程中，长度为1的维度将沿着该维度重复，以匹配最大长度。

##### 其它：
1. `np.random.permutation`
2. `.squeeze`: 删除为1的维度
3. `np.where`: 条件筛选，条件赋值
4. `np.logical_and`: 按元素求交

#### Pandas
Pandas主要有两种数据结构：DataFrame和Series。
Pandas转换为numpy： `DataFrame.values`
Pandas与Numpy的主要区别：
- Pandas的索引可以有标签。
- Pandas各列数据是异质的。Numpy数据类型是同质的。
##### 1. `pd.read_csv`
##### 2. `pd.DataFrame`：
   1. 一般用法：
   DataFrame 构造方法如下：
   ```python
   pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
   ```
   
   参数说明：
   - `data`：DataFrame 的数据部分
       - 可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象
       - 如果不提供此参数，则创建一个空的 DataFrame
   - `index`：DataFrame 的行索引
       - 用于标识每行数据
       - 可以是列表、数组、索引对象等
       - 如果不提供此参数，则创建一个默认的整数索引
   - `columns`：DataFrame 的列索引  
       - 用于标识每列数据
       - 可以是列表、数组、索引对象等
       - 如果不提供此参数，则创建一个默认的整数索引
   - `dtype`：指定 DataFrame 的数据类型
       - 可以是 NumPy 的数据类型，例如 np.int64、np.float64 等
       - 如果不提供此参数，则根据数据自动推断数据类型
   - `copy`：是否复制数据
       - 默认为 False，表示不复制数据
       - 如果设置为 True，则复制输入的数据
   2. 数据框的创建：
       1. **从列表创建数据框：**
       ```python
       import pandas as pd

        data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

       # 创建DataFrame
       df = pd.DataFrame(data, columns=['Site', 'Age'])

       # 使用astype方法设置每列的数据类型
       df['Site'] = df['Site'].astype(str)
       df['Age'] = df['Age'].astype(float)

       print(df)
       ```

      1. **两种从字典创建数据框的方法**：
       法一：
       ```python
       import pandas as pd

       data = {'Site': ['Google', 'Runoob', 'Wiki'], 'Age': [10, 12, 13]}
       df = pd.DataFrame(data)
       print(df)
       ```  
       法二：
       ```python
       import pandas as pd

       data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

       df = pd.DataFrame(data)

       print (df)
       ```
       2. **从numpy数组创建数据框：**
       ```python
       import pandas as pd
       import numpy as np

       data = np.array([[1, 2, 3], [4, 5, 6]])
       df = pd.DataFrame(data, columns=['A', 'B', 'C'])
       print(df)
       ```
    3. **使用行/列的位置/标签索引**： `loc`/`iloc`方法： (i的意思是index)
        1. 使用行标签返回一行或多行数据：
        ```python
        import pandas as pd
        import pandas as pd

        data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
        }

        df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

        # 指定索引
        print(df.loc[["day2", "day2"]])
        # 如果使用如下会报错，因为此时行标签不是0，1，2了，此时要使用iloc
        print(df.loc[[0, 1]]) 
        # 不能直接使用索引/标签获得元素
        print(df.loc["day1", "calories"])
        # 需要先使用列索引再用行索引
        print(df["calories"]["day1"])
        #可以使用如下代码切片行：（区间左闭右开）
        print(df[1:3])
        ```
        **注意上面例子中iloc和loc的区别**
        2. 使用行索引返回一行或多行数据：
        ```python
        import pandas as pd

        data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
        }

        # 数据载入到 DataFrame 对象
        df = pd.DataFrame(data)

        # 返回第一行和第二行
        print(df.loc[[0, 1]])
        ```
    4. 数据的增删改查：
    ```python
    #修改列数据：
    df['calories'] = [100, 200, 300]
    #增加一列或多列数据：
    df['new_column'] = [100, 200, 300]
      
      #使用字典增加多列：(注意：新DataFrame的索引与原DataFrame不匹配会导致NaN，因此需要index.)
    new_cols = {
    'col1': [1, 2, 3],
    'col2': [4, 5, 6]
    }
    df = df.join(pd.DataFrame(new_cols, index=["day1", "day2", "day3"]))

      #使用assign方法增加多列：
    df = df.assign(col3=[7, 8, 9], col4=[10, 11, 12])

    # 增加一行或多行数据：使用 loc、concat 方法 
    df.loc['day4'] = [100, 200]

    new_row = pd.DataFrame({'calories': [100], 'duration': [50]}, index=['day5'])
    df = pd.concat([df, new_row], ignore_index=True)#ignore_index=True 表示忽略原来的索引，重新生成索引 
    
    # 删除行数据：
    # 删除单行
    df = df.drop(index='row_label')  # 使用行标签
    # 或
    df = df.drop(0)  # 使用行索引号
    # 删除多行
    df = df.drop(index=['row1', 'row2'])  # 使用行标签列表
    # 或
    df = df.drop([0, 1])  # 使用行索引号列表

    # 删除列数据
    # 删除单列
    df = df.drop('column_name', axis=1)  # 使用列名
    # 或
    df = df.drop(columns='column_name')  # 使用 columns 参数
    # 删除多列
    df = df.drop(['col1', 'col2'], axis=1)  # 使用列名列表
    # 或
    df = df.drop(columns=['col1', 'col2'])
    ```
    5. dataFrame的属性和方法：
    **基础属性和查看数据:**
    - shape: 返回 DataFrame 的行数和列数（行数, 列数）
    - columns: 返回 DataFrame 的所有列名
    - index: 返回 DataFrame 的行索引
    - dtypes: 返回每一列的数值数据类型
    - head(n): 返回 DataFrame 的前 n 行数据（默认前 5 行）
    - tail(n): 返回 DataFrame 的后 n 行数据（默认后 5 行）
    - info(): 显示 DataFrame 的简要信息，包括列名、数据类型、非空值数量等
    - describe(): 返回 DataFrame 数值列的统计信息，如均值、标准差、最小值等
    **索引、选择和排序:**
    - loc[]: 按标签索引选择数据
    - iloc[]: 按位置索引选择数据
    - at[]: 访问 DataFrame 中单个元素（比 loc[] 更高效）
    - iat[]: 访问 DataFrame 中单个元素（比 iloc[] 更高效）
    - sort_values(by): 按照指定列排序
    - sort_index(): 按行索引排序
    **数据清洗和转换:**
    - dropna(): 删除含有缺失值（NaN）的行或列
    - fillna(value): 用指定的值填充缺失值
    - isnull(): 判断缺失值，返回一个布尔值 DataFrame
    - notnull(): 判断非缺失值，返回一个布尔值 DataFrame
    - apply(func): 对 DataFrame 或 Series 应用一个函数
    - applymap(func): 对 DataFrame 的每个元素应用函数（仅对 DataFrame）
    - groupby(by): 分组操作，用于按某一列分组进行汇总统计
    - pivot_table(): 创建透视表
    **合并、连接和导出:**
    - merge(): 合并多个 DataFrame（类似 SQL 的 JOIN 操作）
    - concat(): 按行或按列连接多个 DataFrame
    - to_csv(): 将 DataFrame 导出为 CSV 文件
    - to_excel(): 将 DataFrame 导出为 Excel 文件
    - to_json(): 将 DataFrame 导出为 JSON 格式
    - to_sql(): 将 DataFrame 导出为 SQL 数据库
    **其他数据操作:**
    - query(): 使用 SQL 风格的语法查询 DataFrame
    - duplicated(): 返回布尔值 DataFrame，指示每行是否是重复的
    - drop_duplicates(): 删除重复的行
    - set_index(): 设置 DataFrame 的索引
    - reset_index(): 重置 DataFrame 的索引
    - transpose(): 转置 DataFrame（行列交换）
    6. 从csv中读取和写入文件：
    读取：DataFrame.read_csv():

    | 参数 | 说明 | 默认值 |
    |------|------|--------|
    | filepath_or_buffer | CSV 文件的路径或文件对象（支持 URL、文件路径、文件对象等）| 必需参数 |
    | sep | 定义字段分隔符，默认是逗号（,），可以改为其他字符，如制表符（\t）| ',' |
    | header | 指定行号作为列标题，默认为 0（表示第一行），或者设置为 None 没有标题 | 0 |
    | names | 自定义列名，传入列名列表 | None |
    | index_col | 用作行索引的列的列号或列名 | None |
    | usecols | 读取指定的列，可以是列的名称或列的索引 | None |
    | dtype | 强制将列转换为指定的数据类型 | None |
    | skiprows | 跳过文件开头的指定行数，或者传入一个行号的列表 | None |
    | nrows | 读取前 N 行数据 | None |
    | na_values | 指定哪些值应视为缺失值（NaN）| None |
    | skipfooter | 跳过文件结尾的指定行数 | 0 |
    | encoding | 文件的编码格式（如 utf-8，latin1 等）| None |

    写入：DataFrame.to_csv(): 注意这里是 DataFrame. 不是pd.
    | 参数 | 说明 | 默认值 |
    |------|------|--------|
    | path_or_buffer | CSV 文件的路径或文件对象（支持文件路径、文件对象）| 必需参数 |
    | sep | 定义字段分隔符，默认是逗号（,），可以改为其他字符，如制表符（\t）| ',' |
    | index | 是否写入行索引，默认 True 表示写入索引 | True |
    | columns | 指定写入的列，可以是列的名称列表 | None |
    | header | 是否写入列名，默认 True 表示写入列名，设置为 False 表示不写列名 | True |
    | mode | 写入文件的模式，默认是 w（写模式），可以设置为 a（追加模式）| 'w' |
    | encoding | 文件的编码格式，如 utf-8，latin1 等 | None |
    
    7. 指定每列的数据类型：(也可以在读取csv时指定)
    ```python
    import pandas as pd

    # 创建一个 DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['4', '5', '6'],
        'C': [7.1, 8.2, 9.3]
    })

    # 为每一列指定不同的数据类型
    df = df.astype({
        'A': 'float64',  # 将列 A 转换为浮点数
        'B': 'int32',    # 将列 B 转换为整数
        'C': 'int64'     # 将列 C 转换为整数
    })

    print(df)
    print(df.dtypes)
    ```
#####  3. Pandas 数据清洗：
1. 删除空值
    DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

    参数说明：
    | 参数 | 说明 | 默认值 |
    |------|------|--------|
    | axis | 删除的方向。0表示删除含空值的行，1表示删除含空值的列 | 0 |
    | how | 删除的条件。'any'表示任意值为空就删除，'all'表示所有值为空才删除 | 'any' |
    | thresh | 保留至少含有n个非空值的行/列 | None |
    | subset | 指定在哪些列中检查是否存在空值，可传入列名列表 | None |
    | inplace | 是否原地修改。True表示直接修改原数据并返回None | False |

    Pandas 把 n/a 和 NA 当作空数据，na 不是空数据，不符合我们要求，我们可以指定空数据类型：
    ```python
    import pandas as pd

    missing_values = ["n/a", "na", "--"]
    df = pd.read_csv('property-data.csv', na_values = missing_values)

    print (df['NUM_BEDROOMS'])
    print (df['NUM_BEDROOMS'].isnull())
    print (df.isnull().any(axis=0))#返回各列是否有空值
    ```
 2. 填充空值
 3. 数据格式错误处理
 4. 清洗错误数据
 5. 清洗重复数据

##### 4.pandas 聚合与排序
###### **排序：**

1. DataFrame.sort_values(by,axis=0,ascending=True,inplace=False)
`df.sort_values(by=[0], axis=0)` 是 pandas 中用于对 DataFrame 排序的方法。让我们逐步分析这个方法的作用。

**基本语法**
```python
DataFrame.sort_values(by, axis=0, ascending=True, inplace=False)
```
- `by`：排序依据的列名或列索引（当 `axis=0` 时），或行索引/行标签（当 `axis=1` 时）。
- `axis`：
    - `axis=0`：对行排序，默认行为。通常基于列的值排序。
    - `axis=1`：对列排序，通常基于索引或行的值排序。
- `ascending`：是否升序排列，默认为 True。
- `inplace`：是否直接修改原 DataFrame，默认为 False。

**示例**

**示例 1：按某一列的值排序**
假设有一个 DataFrame：
```python
import pandas as pd

data = {0: [3, 1, 2], 'B': ['x', 'y', 'z']}
df = pd.DataFrame(data)

print(df)
```
输出：
```css
    0  B
0  3  x
1  1  y
2  2  z
```
对第 0 列（列名为 0）排序：
```python
sorted_df = df.sort_values(by=[0], axis=0)
print(sorted_df)
```
输出：
```css
    0  B
1  1  y
2  2  z
0  3  x
```
- `axis=0` 指示按行排序（基于列的值）。
- `by=[0]` 指定排序的依据是第 0 列。

**示例 2：按多个列排序**
如果你有多个排序依据，可以传递一个列表。例如：
```python
data = {'A': [3, 1, 2], 'B': [2, 2, 1]}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by=['B', 'A'], axis=0)
print(sorted_df)
```
输出：
```css
    A  B
2  2  1
1  1  2
0  3  2
```
这里先按列 B 排序，如果值相同，则按列 A 排序。
**注意事项**
- 列的名称类型：`by` 中指定的列名需要与 DataFrame 的列名一致。如果列名是整数（如 `[0]`），则需要传入整数，而非字符串。
- 原地修改：`inplace=True` 会直接修改原 DataFrame，不会返回新对象。
- 排序稳定性：当多行有相同值时，`sort_values` 会保持原来的顺序。


2. DataFrame.sort_index(axis=0,ascending=True,inplace=False)
若需要按索引排序，可以使用 `sort_index()` 方法，而不是 `sort_values()`。
```python
import pandas as pd
df_sorted = df.sort_index(axis=0, ascending=False)
print(df_sorted)
```

###### **分组后聚合：**

| 操作 | 方法 | 说明 | 示例 |
| --- | --- | --- | --- |
| 按列分组并聚合 | df.groupby(by).agg() | 按指定列（by）进行分组，agg() 可以传入不同的聚合函数，进行多种操作 | df.groupby('Department').agg({'Salary': 'mean'}) |
| 多重聚合函数应用 | df.groupby(by).agg([func1, func2]) | 可以对同一列应用多个聚合函数，返回多种聚合结果 | df.groupby('Department').agg({'Salary': ['mean', 'sum']}) |

例子：

```python
#分组聚合
import pandas as pd
data={
    'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [50000, 60000, 55000, 70000, 75000]
}
df=pd.DataFrame(data)
df.groupby("Department").agg({"Salary":"mean"})
# 多重聚合
df.groupby("Department").agg({"Salary":["mean","sum"]})
```

###### **分组后排序：**

```python
df.groupby("Department").apply(lambda x: x.sort_values("Salary"))
```

注意apply中的匿名函数是对每个分组进行操作，返回的是一个DataFrame

**基本语法**

```python
df.groupby('column_name').apply(function)
```

- `'column_name'`：用于分组的列。
- `function`：应用于每个分组的函数。这可以是一个内置函数，也可以是自定义函数。

**工作原理**

1. **分组（groupby）**：按指定列对数据进行分组。
2. **应用（apply）**：对每个分组调用指定函数，函数的输入是分组的一个子 DataFrame，输出可以是标量、Series 或 DataFrame。

**示例用法**

**示例 1：对分组数据求和**

```python
import pandas as pd

data = {'Category': ['A', 'A', 'B', 'B'],
    'Values': [10, 20, 30, 40]}
df = pd.DataFrame(data)

# 按 'Category' 分组，并计算每组数据的总和
result = df.groupby('Category').apply(lambda x: x['Values'].sum())
print(result)
```

输出：

```css
Category
A    30
B    70
dtype: int64
```

**示例 2：对分组数据进行归一化**

```python
# 对每组数据的 'Values' 列进行归一化
result = df.groupby('Category').apply(lambda x: x.assign(Normalized=x['Values'] / x['Values'].sum()))
print(result)
```

输出：

```css
Category  Values  Normalized
0        A      10    0.333333
1        A      20    0.666667
2        B      30    0.428571
3        B      40    0.571429
```

**示例 3：自定义逻辑应用**

```python
# 自定义逻辑，比如对每组数据的值取平均并标记组名
def custom_function(group):
    mean_value = group['Values'].mean()
    group['Mean'] = mean_value
    return group

result = df.groupby('Category').apply(custom_function)
print(result)
```

输出：

```css
Category  Values  Mean
0        A      10  15.0
1        A      20  15.0
2        B      30  35.0
3        B      40  35.0
```

**注意事项**

- **性能**：apply 函数的灵活性较高，但性能可能不如一些特定的聚合函数（如 sum、mean 等）。
- **函数输入**：自定义函数的输入是每个分组的一个子 DataFrame，可以访问分组内的所有列。
- **返回值**：返回值可以是 DataFrame、Series 或标量，pandas 会根据返回值调整最终的输出格式。

###### **其它：**
1. df['column_name'].value_counts()
返回一个Series，包含每个值出现的次数。
value_counts() 是Series的方法。
    
##### 5. 数据合并与连接
1. 数据库风格的连接 — pd.merge()
    merge() 方法允许根据某些列对两个 DataFrame 进行合并，类似 SQL 中的 JOIN 操作。支持内连接、外连接、左连接和右连接。

    | 参数 | 说明 |
    |------|------|
    | left | 左侧 DataFrame |
    | right | 右侧 DataFrame |
    | how | 合并方式，支持 'inner', 'outer', 'left', 'right' |
    | on | 连接的列名（如果两侧列名不同，可使用 left_on 和 right_on）|
    | left_on | 左侧 DataFrame 的连接列 |
    | right_on | 右侧 DataFrame 的连接列 |
    | suffixes | 添加后缀，以区分重复的列名 |

    示例代码：
    ```python
    import pandas as pd

    # 示例数据
    left = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
    right = pd.DataFrame({'ID': [1, 2, 4], 'Age': [24, 27, 22]})

    # 使用 merge 进行内连接
    result = pd.merge(left, right, on='ID', how='inner')
    print(result)
    ```
2. 沿轴连接 — pd.concat([DataFrame1,DataFrame2],axis=0)
    pd.concat() 是直接用来拼接的，如果出现索引不匹配，会自动填充NaN；其它两个方法并不会自动填充，而是要指定how参数。

3. 基于索引的连接 — DataFrame.join(DataFrame,how='left') 
    join() 方法是 Pandas 中的简化连接操作，通常用于基于索引将多个 DataFrame 连接。
    merge()方法是基于某列的

    | 参数 | 说明 |
    |------|------|
    | other | 需要连接的另一个 DataFrame |
    | how | 合并方式，支持 'left', 'right', 'outer', 'inner' |
    | on | 使用的连接列，默认基于索引 |

    示例代码：
    ```python
    import pandas as pd

    # 示例数据
    left = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
    right = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 4])

    # 使用 join 进行连接
    result = left.join(right, how='inner')
    print(result)
    ```

##### 6. 自定义函数的应用：
1. DataFrame.apply(function，axis=0):应用于行或列。 给函数的是series.
 ```python
 import pandas as pd
 import numpy as np
 df = pd.DataFrame(np.random.randint(0, 10, (4, 3)), 
                 columns=list('abc'), 
                 index=range(4))
 df.apply(lambda x: x.max()-x.min(), axis=0)
 ```
 
1. DataFrame.applymap(function):应用于DataFrame的每个元素
 ```python
 df.applymap(lambda x: x*10 if x%2 == 0 else x) #偶数放大10倍
 ```

1. Series.map(function):应用于Series的每个元素,可以是映射字典
 ```python
 import pandas as pd

 # 示例数据
 df = pd.DataFrame({'A': ['cat', 'dog', 'rabbit']})

 # 使用字典进行映射
 df['A'] = df['A'].map({'cat': 'kitten', 'dog': 'puppy'})
 print(df)
 ```
##### 其它应用：
###### 采样：
用于降采样，以处理数据不平衡问题。
pd.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
参数说明：
- `n`: 要抽取的样本数量
- `frac`: 抽取的比例（0-1之间的小数）
- `replace`: 是否有放回抽样，默认False
- `weights`: 各样本的权重
- `random_state`: 随机种子，用于复现结果
- `axis`: 抽样的轴向，0表示行，1表示列

示例代码：











##### 总结
1. 创建DataFrame:
2. 读取/写入csv
3. 空值处理，重复行处理
空值处理：
``` python
DataFrame.isnull().any(axis=0)
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
```
重复值处理：
```python
DataFrame.duplicated(subset=None, keep='first')
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
```
4. 排序，分组，聚合
5. 数据合并与连接
```python
pd.merge([DataFrame1,DataFrame2],on=None,how='inner')
pd.concat([DataFrame1,DataFrame2],axis=0)
DataFrame.join(DataFrame,how='inner')
```

#### matplotlib
1. plt.show(block=True):

#### torch
##### 张量操作：
###### torch.matmul 
   - matmul的全称是matrix multiplication，矩阵乘法。
   - **`torch.matmul` 的高维行为**

   - **基本规则：**
       - 假设有两个张量 `A` 和 `B`。
       - 如果这两个张量都是一维的（向量），执行**点积**操作，返回一个标量。
       - 如果这两个张量至少有一维是二维或更高维度的张量，`torch.matmul` 将执行**矩阵乘法**。
       - **高维情况下（维度 ≥ 3）**，`torch.matmul` 将前面的维度视为批量维度（batch dimensions），并在最后两个维度上执行矩阵乘法。

   - **广播机制**

   当张量的维度不同时，PyTorch 会按照以下规则进行广播：

   1. **对齐维度数：**
        - 如果张量的维度数不同，将维度较小的张量的形状前面补 `1`，使得两个张量具有相同的维度数。

   2. **批量维度的广播：**
        - 从后向前比较（不包括最后两个矩阵乘积的维度），如果维度值相同，或者其中一个为 `1`，则认为是可广播的。
        - 如果两个张量在某个批量维度上不相等且不为 `1`，则无法广播，操作会报错。

   3. **矩阵乘法：**
        - 在匹配并广播批量维度后，`torch.matmul` 会在最后两个维度上执行矩阵乘法。

   - **示例**

   - **示例 1：基本批量矩阵乘法**

   ```python
   import torch

   # 张量 A，形状为 [batch_size, M, K]
   A = torch.randn(10, 3, 4)  # 10 个 3x4 的矩阵

   # 张量 B，形状为 [batch_size, K, N]
   B = torch.randn(10, 4, 5)  # 10 个 4x5 的矩阵

   # 执行批量矩阵乘法
   C = torch.matmul(A, B)  # 结果形状为 [10, 3, 5]
   print(C.shape)
   # 输出：torch.Size([10, 3, 5])
   ```

   - **示例 2：广播批量维度**

   ```python
   import torch

   # 张量 A，形状为 [batch_size_A, M, K]
   A = torch.randn(2, 3, 4)  # 2 个 3x4 的矩阵

   # 张量 B，形状为 [K, N]
   B = torch.randn(4, 5)     # 单个 4x5 的矩阵

   # B 的批量维度将被广播为 2
   C = torch.matmul(A, B)  # 结果形状为 [2, 3, 5]
   print(C.shape)
   # 输出：torch.Size([2, 3, 5])
   ```

   在这个示例中，`B` 的形状被视为 `[1, 4, 5]`，然后在第一个维度上广播为 `2`，以匹配 `A` 的批量维度。

   - **示例 3：高维批量矩阵乘法**

   ```python
   import torch

   # 张量 A，形状为 [D1, D2, M, K]
   A = torch.randn(2, 3, 4, 5)

   # 张量 B，形状为 [D1, D2, K, N]
   B = torch.randn(2, 3, 5, 6)

   # 结果形状为 [2, 3, 4, 6]
   C = torch.matmul(A, B)
   print(C.shape)
   # 输出：torch.Size([2, 3, 4, 6])
   ```

   在这里，`A` 和 `B` 都有批量维度 `[2, 3]`，`torch.matmul` 会在这两个维度上逐元素地执行矩阵乘法。

   - **示例 4：批量维度的广播**

   ```python
   import torch

   # 张量 A，形状为 [D1, M, K]
   A = torch.randn(2, 3, 4)

   # 张量 B，形状为 [D2, K, N]
   B = torch.randn(1, 4, 5)  # 注意 D2=1，可以广播

   # 批量维度将被广播为 [2]
   C = torch.matmul(A, B)
   print(C.shape)
   # 输出：torch.Size([2, 3, 5])
   ```

   - **广播机制的详细解释**

   - **对齐维度：**
       - 假设 `A` 的维度是 `[A_1, A_2, ..., A_n, M, K]`，`B` 的维度是 `[B_1, B_2, ..., B_n, K, N]`。
       - 其中，`A` 和 `B` 的批量维度是 `[A_1, A_2, ..., A_n]` 和 `[B_1, B_2, ..., B_n]`。

   - **批量维度的广播：**
       - 对于每个批量维度 `i`，如果 `A_i == B_i`，或者其中一个为 `1`，则可以进行广播。
       - 结果的批量维度为每个 `A_i` 和 `B_i` 中较大的那个。

   - **矩阵乘法：**
       - 在广播后的批量维度上，`torch.matmul` 在 `A` 和 `B` 的最后两个维度上执行矩阵乘法。
       - 即对于每个批量，执行形状

   - **注意事项**

   1. **维度匹配：**
      - 确保用于矩阵乘法的最后两个维度是可乘的，即 `A` 的倒数第二个维度 `K` 与 `B` 的倒数第二个维度 `K` 相等。

   2. **广播限制：**
      - 如果批量维度不能广播（即尺寸不相等且没有为 `1` 的维度），会引发错误。

   3. **性能考虑：**
      - 高维矩阵乘法可能会占用大量内存和计算资源，处理大型数据时需要注意优化。

   - **常见应用**

   - **神经网络中的批量处理：**
     - 在处理批量数据时，如批量输入样本，`torch.matmul` 可以高效地执行矩阵乘法。

   - **注意力机制：**
     - 在实现自注意力（Self-Attention）时，需要对高维张量进行矩阵乘法。

     ```python
     # 示例：自注意力中的矩阵乘法
     import torch

     batch_size = 8
     seq_len = 20
     d_model = 64

     # 输入张量，形状为 [batch_size, seq_len, d_model]
     queries = torch.randn(batch_size, seq_len, d_model)
     keys = torch.randn(batch_size, seq_len, d_model)

     # 转置 keys 的最后两个维度
     keys_transposed = keys.transpose(-2, -1)

     # 矩阵乘法，结果形状为 [batch_size, seq_len, seq_len]
     attention_scores = torch.matmul(queries, keys_transposed)
     print(attention_scores.shape)
     # 输出：torch.Size([8, 20, 20])
     ```

   - **与 `torch.bmm` 的区别**

   - `torch.bmm`（批量矩阵乘法）仅适用于维度为 3 的张量（形状为 `[batch_size, M, N]`），即只能处理单个批量维度。

   - `torch.matmul` 更通用，可以处理维度 ≥ 1 的张量，支持多个批量维度。

   - **总结**

   - **高维矩阵乘法：** `torch.matmul` 可以对高维张量进行批量矩阵乘法，批量维度按照广播机制处理。
   - **广播机制：** 当批量维度不同时，PyTorch 会按照广播规则来扩展维度，以使得矩阵乘法可以进行。
   - **矩阵乘法维度：** 确保用于矩阵乘法的两个张量的最后两个维度是可乘的（即形状为 `[M, K]` 和 `[K, N]`）。

   通过理解 `torch.matmul` 在高维时的行为和广播机制，您可以更有效地处理批量数据和高维矩阵运算。同时，注意调整张量的形状，以满足矩阵乘法的要求，可以避免在运行时出现错误。

   - **参考文档**

   - [PyTorch 官方文档：`torch.matmul`](https://pytorch.org/docs/stable/generated/torch.matmul.html)
   - [PyTorch 广播语义](https://pytorch.org/docs/stable/notes/broadcasting.html)

   希望以上解释能够帮助您理解 `torch.matmul` 在高维张量时的工作方式！

###### torch.norm
用法：`torch.norm(input, p=2, dim=None, keepdim=False, out=None) -> Tensor`
计算输入张量的范数。


###### .squeeze
用法：`torch.squeeze(input, dim=None, out=None) -> Tensor` 
用来移除输入张量中的一维条目，即把所有维数为1的维度去掉。当给定dim时，那么只移除给定维数为1的维度。返回的张量会和输入张量共享内存，所以改变其中一个的内容会改变另一个。
###### .unsqueeze
用法：`torch.unsqueeze(input, dim, out=None) -> Tensor`
返回一个新的张量，对输入的指定位置插入维度 1
1. .view
    需要张量连续，与原始数据共享内存，但.reshape()不要求张量连续,且不共享内存。
    用法：`torch.view(*shape) -> Tensor`
    ```python
    import torch

    # 创建一个张量
    x = torch.randn(4, 4)

    # 使用 view 方法改变张量形状
    y = x.view(2, 8)

    print(y.shape)
    # 输出：torch.Size([2, 8])
    ```
    如果张量在内存中不是连续的，可以先使用 `contiguous()` 方法使其连续。

    **示例**：

    ```python
    import torch

    # 创建一个非连续张量
    x = torch.randn(4, 4).transpose(0, 1)

    # 使张量连续
    x_contiguous = x.contiguous()

    # 使用 view 方法改变张量形状
    y = x_contiguous.view(2, 8)

    print(y.shape)
    # 输出：torch.Size([2, 8])
    ```

###### Dataloader
    
 - `torch.utils.data.DataLoader` 是 PyTorch 中用于加载数据的工具，可以自动进行批量加载、打乱数据等操作。
 - <font color='red'>注意：Dataloader可以传入numpy数组，返回tensor.</font>
 e.g.
 ```python
 import numpy as np
 from torch.utils.data import Dataset,DataLoader

 totoal_data=50
 batch_size=10
 dim=5

 dataset=np.random.rand(batch_size,dim)
 for data in DataLoader(dataset,batch_size=batch_size, shuffle=True):
     print("The type of data is :{}, the size of data is {}".format(type(data),data.size()))
 ```     
 - **基本用法**
     - 创建 DataLoader 对象时，需要传入一个 `Dataset` 对象，用于提供数据。
     - 可以指定 `batch_size` 参数，表示每个批次的样本数量。
     - 可以设置 `shuffle=True`，表示在每个 epoch 开始时打乱数据。
     - 可以设置 `num_workers`，表示用于数据加载的子进程数。
 - **示例**
     ```python
     import torch
     from torch.utils.data import DataLoader, TensorDataset

     # 创建一个张量数据集
     data = torch.randn(100, 3)
     targets = torch.randint(0, 2, (100,))

     dataset = TensorDataset(data, targets)

     # 创建 DataLoader 对象
     dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

     # 遍历 DataLoader
     for batch in dataloader:
         inputs, labels = batch
         print(inputs.shape, labels.shape)
     ```
 - **注意事项**
     - **数据集**：`DataLoader` 需要传入一个 `Dataset` 对象，如 `TensorDataset`、`ImageFolder` 等。
     - **批量大小**：可以通过 `batch_size` 参数指定每个批次的样本数量。
     - **打乱数据**：设置 `shuffle=True` 可以在每个 epoch 开始时打乱数据。
     - **多进程加载**：可以设置 `num_workers` 参数，表示用于数据加载的子进程数。

###### torch.nn.CrossEntropyLoss
  - **`torch.nn.CrossEntropyLoss`** 是 PyTorch 中用于多分类任务的损失函数。它结合了 `nn.LogSoftmax()` 和 `nn.NLLLoss()`，适用于分类问题。
  - **基本用法**：
    ```python
    import torch
    import torch.nn as nn

    # 创建损失函数对象
    criterion = nn.CrossEntropyLoss()

    # 假设有两个样本的预测值和对应的标签
    predictions = torch.tensor([[2.0, 1.0, 0.1], [0.5, 2.5, 0.3]])
    labels = torch.tensor([0, 1])

    # 计算损失
    loss = criterion(predictions, labels)
    print(loss.item())
    ```
  - **初始化参数**：
    - `weight`：可选，给每个类别的损失赋予不同的权重。
    - `size_average`：已弃用，使用 `reduction` 参数代替。
    - `ignore_index`：可选，指定一个类别索引，该类别的损失将被忽略。
    - `reduction`：指定应用于输出的归约方式，默认为 `mean`。可选值为 `none`、`mean` 和 `sum`。
  - **注意事项**：
      - 目标标签应该是类别的索引（整数），而不是独热编码（one-hot encoding）。
      - 标签的形状应为 [batch_size]，每个元素是 [0, C-1] 之间的整数，其中 C 是类别数。
      - input（logits）的形状应为 [batch_size, num_classes]。对于多维输入（如时间序列），可能需要调整 input 和 target 的形状以匹配。
      - 避免手动添加 Softmax 层：因为 CrossEntropyLoss 已经包含了 LogSoftmax，手动添加 Softmax 会导致计算上的重复和不必要的数值问题。
###### tensor.permute和tensor.reshape区别：
  - **`permute` 和 `reshape` 的区别**：
      - `permute` 和 `reshape` 都可以用于改变张量的形状，但它们的作用有所不同。
      - `permute` 用于交换张量的维度，可以灵活地调整维度的顺序。
      - `reshape` 用于改变张量的形状，但不能改变张量的维度顺序。
      - `permute` 通常用于高维张量的维度交换，`reshape` 用于形状调整。
  - **示例**：
      ```python
      import torch

      # 创建一个 3x4x5 的张量
      x = torch.randn(3, 4, 5)

      # 使用 permute 交换维度
      y = x.permute(1, 2, 0)  # 将第 1 维移动到最后
      print(y.shape)
      # 输出：torch.Size([4, 5, 3])

      # 使用 reshape 改变形状
      z = x.reshape(2, 3, 10)  # 改为 2x3x10
      print(z.shape)
      # 输出：torch.Size([2, 3, 10])
      ```
  - **注意事项**：
      - `permute` 和 `reshape` 都是返回新的张量，不会改变原始张量。
      - `permute` 可以交换维度，但不能改变维度的数量。
      - `reshape` 可以改变形状，但不能改变维度的顺序。
      - 在处理高维张量时，`permute` 和 `reshape` 可以灵活地调整张量的形状和维度顺序。



###### tensor.gather
用法：`torch.gather(input, dim, index, out=None) -> Tensor`
用于根据索引从输入张量中收集元素。
参考：[https://blog.csdn.net/iteapoy/article/details/106203954](https://blog.csdn.net/iteapoy/article/details/106203954)

##### 关于注册参数的操作
###### self.register_parameter
用法：`self.register_parameter(name, param)`
用来注册参数，参数是nn.Parameter类型。

###### self.parameters()
用法：`self.parameters()`
返回一个迭代器，包含所有可训练的参数。

###### self.named_parameters()
用法：`self.named_parameters()`
返回一个迭代器，包含所有可训练的参数，并返回参数的名称。

##### 关于model的操作
###### nn.sequential和nn.ModuleList
nn.ModuleList 是 PyTorch 中 torch.nn 模块的一部分，用于存储一组子模块。这些子模块通常是神经网络的层，nn.ModuleList 可以方便地管理它们，同时与 PyTorch 的其他功能（如自动微分和模型参数管理）集成良好。

**特点和功能**
- **存储子模块**： nn.ModuleList 是一个有序的模块列表，每个元素都是 nn.Module 的实例（例如线性层、卷积层等）。
- **动态构造网络**： 可以在构造时动态地添加、删除或访问子模块，非常适合可变层数或结构的模型。
- **参数管理**： 使用 nn.ModuleList 添加的子模块，其参数会自动注册到父模块中，便于优化和保存。

**与 Python 的普通列表的区别**：
- 普通列表只是 Python 数据容器，无法与 PyTorch 的模块管理系统集成。
- nn.ModuleList 会确保其中的模块正确加入模型中，参与训练和推理。

**基本用法**
- **定义和使用**：
    ```python
    import torch
    import torch.nn as nn

    class MyModel(nn.Module):
        def __init__(self):
            super(MyModel, self).__init__()
            # 创建一个 ModuleList，包含多个线性层
            self.layers = nn.ModuleList([
                nn.Linear(10, 20),
                nn.Linear(20, 30),
                nn.Linear(30, 40)
            ])

        def forward(self, x):
            for layer in self.layers:
                x = layer(x)
            return x

    # 实例化模型
    model = MyModel()

    # 输入张量
    input_tensor = torch.randn(1, 10)

    # 前向传播
    output = model(input_tensor)
    print(output.shape)  # 输出: torch.Size([1, 40])
    ```

- **动态添加模块**：
    ```python
    # 动态添加层
    model.layers.append(nn.Linear(40, 50))

    # 更新后前向传播
    output = model(input_tensor)
    print(output.shape)  # 输出: torch.Size([1, 50])
    ```

**常见问题和注意事项**
- **与 Sequential 的区别**：
    - nn.ModuleList 只是存储模块，不会定义顺序的前向传播逻辑。
    - 如果需要自动执行前向传播逻辑，可以使用 nn.Sequential。
    ```python
    nn.Sequential(
        nn.Linear(10, 20),
        nn.ReLU(),
        nn.Linear(20, 30)
    )
    ```
    - 而使用 nn.ModuleList 时，你需要手动定义 forward 函数来调用每一层。

- **不支持张量**：
    - nn.ModuleList 只能存储 nn.Module 子类的实例，不能存储张量或普通 Python 对象。
    - 如果需要存储张量，可以直接用 Python 列表。

- **访问方式**： 可以像 Python 列表一样通过索引访问其中的模块。

**使用场景**
- **动态网络**： 在网络结构中，层的数量可能不固定。例如，RNN、Transformer 等模型中，可能需要存储若干个重复的子模块。
- **子网络管理**： 当模型中需要管理多个不同的子模块时，nn.ModuleList 可以作为子模块的容器，方便地对其进行迭代和操作。

###### nn.moduleDict
```python
# 创建
model_dict = nn.ModuleDict({
    'linear1': nn.Linear(10, 5),
    'linear2': nn.Linear(5, 1)
})

# 访问
output1 = model_dict['linear1'](input)
```


#### scikit-learn (keras)
1. `precision_recall_curve`: 返回不同阈值下的 precision 和 recall 以及阈值
2. `roc_auc_score`
3. `verbose`: 控制输出信息

#### tensorflow
1. `tf.compact`
2. `tf.zeros`
3. `tf.eye`
4. `tf.shape`
5. `tf.linalg`: 对角阵 `tf.eye` 是单位阵

#### 快捷键
1. 多行注释：`Shift + P`
2. 多行前移：`Shift + Tab`
3. 反撤销：`Ctrl + Shift + Z`
4. Fn 与功能键（声音等）冲突：`Fn + F12`

#### terminal 命令
- `history | grep <关键词>`
- 查看帮助：`info ls` 或 `ls --help`
- `cat 文件`: 打开文件

#### git 命令
- git的user.name和user.email设置：
`git config --global user.name "your_name"`
`git config --global user.email "your_email@example.com"`
用来知道是谁提交的代码

- `index`: 暂存区
- `working tree`: 工作区
- vscode 下 git diff 视图：左边是历史，右边是当前的

- `git log`: `git log` 后一直没有光标问题解决：按 `q`
- `git reflog`: 获得版本号

- `git status`
- `git diff <文件名>`

- `git add`
- `git commit`
- `git checkout --<文件名>`: 工作区回到和版本库相同状态（用于撤销修改，撤销删除）

- `git reset --hard HEAD^`: 版本回退 (HEAD 是指向 master 的指针)
- `git reset --hard <版本号>`: 到指定版本

- 追加到上一次提交：（待补充）

- 查看分支：`git branch`
- 创建分支：`git branch <name>`
- 切换分支：`git checkout <name>`
- 创建并切换分支：`git checkout -b <name>`
- 合并某分支到当前分支：`git merge <name>`
- 删除分支：`git branch -d <name>`

- `git clone` 不会把 origin 的分支拉下来

- `git remote -v`

问题：git 比对版本的时候会不会丢失之前工作？

#### Some technique
1. `non_zero_mask = a > 0`: 获得为正的 index
2. `perf = -1`: 有些函数会返回 -1



### Linux:
#### source 的主要用途
加载环境变量

1. 加载环境变量和配置文件
- 常用于加载配置文件（如 .bashrc、.bash_profile）
- 示例: `source ~/.bashrc` 
  重新加载当前用户的 .bashrc 文件，应用其中定义的环境变量、别名等配置

2. 执行脚本并保留变量
- 使用 source 执行脚本时，变量会保留在当前 Shell 会话中
- 示例:
  ```bash
  # example.sh
  MY_VAR="Hello, world!"
  
  # 使用 source
  source example.sh
  echo $MY_VAR  # 输出: Hello, world!
  ```
- 直接运行脚本（如 bash example.sh）则变量不会保留

3. 运行设置脚本
- 用于配置开发环境或虚拟环境
- 示例: `source venv/bin/activate` (Python虚拟环境)

4. source 与直接执行脚本的区别:
| 功能 | source 执行脚本 | 直接执行脚本 |
|------|----------------|--------------|
| 运行环境 | 当前 Shell | 启动新的子 Shell |
| 变量保留 | 是 | 否 |
| 适用场景 | 修改当前Shell环境 | 独立执行脚本 |

1. /opt和/usr区别：
/usr中文件可以直接在命令行运行
2. 桌面图标的位置：
`/usr/share/applications/`
3. `/bin`和`/usr/bin`和`/usr/local/bin`的区别：
- `/bin`：系统命令，通常是系统自带的命令，如 `ls`, `cp`, `mv` 等。
- `/usr/bin`：用户命令，通常是系统自带的命令，如 `ls`, `cp`, `mv` 等。
- `/usr/local/bin`：用户命令，通常是用户安装的命令，如 `conda`, `pip` 等。

### Mysql
1. 几个英文句子的含义：
- "connecting to MySQL using a blank password"：使用空密码连接到 MySQL
- "VALIDATE PASSWORD COMPONENT can be used to test passwords"：使用密码验证组件来测试密码
- 

### CUDA安装：
1. `nvidia-smi` 查看显卡信息; cuda version是支持的最高版本


### Cursor：
Compresser
引用

### VScode/Cursor 设置：
1. **设置快捷键**：
    - `Ctrl + K Ctrl + S`
    - 打开 `keybinds.json` 文件：
    ```json
    {
        "key": "ctrl+1",
        "command": "editor.action.insertSnippet",
        "args": {
            "snippet": "(需要插入代码)"
        },
        "when": "editorTextFocus"
    }
    ```
    - `command` 除了以上还有 `type` 选项，用于直接插入指定的文本，不支持设置光标位置
2. **Markdown 在插入行间公式后不显示的问题**：
    - 参考链接: [GitHub Issue #1032](https://github.com/yzhang-gh/vscode-markdown/issues/1032)
    - 解决方案：禁用 `markdown-math` 扩展，使用 `@builtin markdown` 禁用。
3. enable editor preview单击打开文件后无法出现在bar中。
4. activate bar是最左侧一栏
### 网络相关：
#### `netstat -ano` 命令
`netstat -ano` 是一个 Windows 命令，用于显示网络连接、路由表、网络接口统计信息以及网络协议的详细信息。以下是该命令的输出解释：

- `-a`：显示所有连接和监听端口。
- `-n`：以数字形式显示地址和端口号。
- `-o`：显示与每个连接关联的进程 ID (PID)。

你可以在命令提示符中运行以下命令来查看网络连接：

```sh
netstat -ano
```

这将输出类似以下内容：

```
Proto  Local Address          Foreign Address        State           PID
TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       1234
TCP    192.168.1.100:139      192.168.1.101:445      ESTABLISHED     5678
...
```

- `Proto`：协议类型（TCP 或 UDP）。
- `Local Address`：本地地址和端口号。
- `Foreign Address`：远程地址和端口号。
- `State`：连接状态（如 LISTENING、ESTABLISHED 等）。
- `PID`：进程 ID，可以在任务管理器中找到对应的进程。

如果你需要进一步分析某个特定的连接，可以使用 `tasklist` 命令结合 PID 来找到对应的进程：

```sh
tasklist /FI "PID eq 1234"
```

这将显示 PID 为 1234 的进程信息。

#### HTTP与HTTPS区别
HTTP（HyperText Transfer Protocol）和 HTTPS（HyperText Transfer Protocol Secure）是用于在 Web 浏览器和 Web 服务器之间传输数据的协议。以下是它们的主要区别：
    1. **安全性**：
- **HTTP**：数据以明文形式传输，容易被中间人攻击（如窃听、篡改）。
- **HTTPS**：使用 SSL/TLS 协议对数据进行加密，确保数据在传输过程中不被窃听和篡改。
    2. **端口**：
- **HTTP**：默认使用端口 80。
    - **HTTPS**：默认使用端口 443。

    1. **证书**：
    - **HTTP**：不需要证书。
    - **HTTPS**：需要由受信任的证书颁发机构（CA）颁发的 SSL/TLS 证书。

    1. **性能**：
    - **HTTP**：由于没有加密和解密过程，性能稍微高一些。
    - **HTTPS**：由于需要加密和解密数据，性能稍微低一些，但现代硬件和优化技术已经使得这种差异非常小。

    1. **SEO**：
    - **HTTP**：搜索引擎对 HTTP 网站的排名可能较低。
    - **HTTPS**：搜索引擎（如 Google）更倾向于对 HTTPS 网站进行更高的排名。

    1. **浏览器支持**：
    - **HTTP**：现代浏览器会标记 HTTP 网站为“不安全”。
    - **HTTPS**：现代浏览器会显示安全锁图标，表示网站是安全的。

    总结：
    - **HTTP** 适用于不需要保护敏感数据的普通网站。
    - **HTTPS** 适用于需要保护敏感数据（如登录信息、支付信息）的安全网站。
#### LAN,WAN,VLAN
- LAN: 局域网
- WAN: 广域网
- VLAN: 虚拟局域网
- WLAN: 无线局域网



### common knowledge
##### `__init__.py` 作用：
1. 使得文件夹成为一个 package
2. 定义包的初始化行为：`__init__.py` 文件可以包含代码，在导入包时自动执行。你可以在其中初始化包的状态或导入其他模块
3. 控制包的导出内容：可以使用 `__init__.py` 中的 `__all__` 列表来定义当使用 `from package import *` 时导出的模块或函数
4. 简化导入路径：你可以在 `__init__.py` 中导入包内的模块，使外部使用时路径更加简洁

##### 文档里方括号含义：
方括号 `[]` 通常表示可选参数。这意味着在调用函数时，可以选择性地提供这些参数；如果不提供，则使用默认值。
例如：`dict.get(key[, default])`

##### 给函数编写文档
在 Python 的文档字符串（docstring）中，`:param` 和 `Args:` 都用于描述函数参数，但它们的使用方式和风格有所不同。以下是它们的区别和示例：

1. `:param` 标记
`:param` 标记是一种详细的参数描述方式，通常与 `:type` 标记一起使用。它们的格式如下：

```python
:param param_name: 描述参数的用途
:type param_name: 参数的类型
```

2. `Args:` 标记
`Args:` 标记是一种简洁的参数描述方式，通常用于 Google 风格的文档字符串。它的格式如下：

```python
Args:
    param_name (param_type): 描述参数的用途
```

3. 示例对比

使用 `:param` 标记：
```python
def train(epochs=20, batchSize=1024, lr=0.01, lamda=0.1, factors_dim=64):
    """
    训练ALS模型。

    该函数使用交替最小二乘法（ALS）训练推荐系统模型。模型通过多次迭代和批量梯度下降来优化用户和物品的隐向量。

    :param epochs: 迭代次数，默认为20。
    :type epochs: int
    :param batchSize: 每个批次的数据量，默认为1024。
    :type batchSize: int
    :param lr: 学习率，默认为0.01。
    :type lr: float
    :param lamda: 正则化系数，默认为0.1。
    :type lamda: float
    :param factors_dim: 隐因子的数量，默认为64。
    :type factors_dim: int
    :return: None
    """
    # 函数实现
    pass
```

使用 `Args:` 标记：
```python
def train(epochs=20, batchSize=1024, lr=0.01, lamda=0.1, factors_dim=64):
    """
    训练ALS模型。

    该函数使用交替最小二乘法（ALS）训练推荐系统模型。模型通过多次迭代和批量梯度下降来优化用户和物品的隐向量。

    Args:
        epochs (int): 迭代次数，默认为20。
        batchSize (int): 每个批次的数据量，默认为1024。
        lr (float): 学习率，默认为0.01。
        lamda (float): 正则化系数，默认为0.1。
        factors_dim (int): 隐因子的数量，默认为64。

    Returns:
        None
    """
    # 函数实现
    pass
```

4. 选择哪种风格
- **`:param` 标记**：适用于 Sphinx 风格的文档字符串，通常与 `:type` 标记一起使用，提供详细的参数描述。
- **`Args:` 标记**：适用于 Google 风格的文档字符串，简洁明了，适合快速描述参数。

##### Byte String和Unicode String:
- 在 Python 中，字符串有两种主要类型：`str` 和 `bytes`。
- `str` 是 Unicode 字符串，通常用于表示文本数据。
- `bytes` 是字节串，通常用于表示二进制数据。
- Byte string: 主要支持 ASCII 字符（0-127） Unicode: 支持所有字符（包括中文、日文、emoji等）

##### ssh的公钥放在服务器的~/.ssh/authorized_keys文件中