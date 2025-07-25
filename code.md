学习注意：
1. 学习一个函数要看输入参数类型，所属的类，返回的类型，返回的维度；




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

#### datetime
1. `datetime.datetime.now()`: 获取当前日期和时间

#### json模块

#### 正则表达式
##### 捕获组

#### python
##### 万物皆对象
python中实例与对象是一样的；
- 类也是对象
```python
>>> isinstance(object, type)
True               # object 是 type 的实例

>>> isinstance(type, object)
True               # type 是 object 的实例

>>> issubclass(type, object)
True               # type 是 object 的子类

>>> issubclass(object, type)
False              # object 不是 type 的子类
```
object是类但也是type的对象；
type是object的子类，同时也是object的对象；



##### 基本用法
###### 基本数据类型：
1. 数值类型(Numeric Types)：
   - int：整数，如42
   - float：浮点数，如3.14
   - complex：复数，如3+4j
   - bool：布尔值，True或False
2. 序列类型(Sequence Types)：
   - str：字符串，如"hello"
   - list：列表，如[1, 2, 3]
   - tuple：元组，如(1, 2, 3)
   - range：范围，如range(5)
3. 映射类型(Mapping Type)：
   - dict：字典，如{'a': 1, 'b': 2}
4. 集合类型(Set Types)：
   - set：可变集合，如{1, 2, 3}
   - frozenset：不可变集合
5. 二进制类型(Binary Types)：
   - bytes：不可变字节序列，如b'hello'
   - bytearray：可变字节序列
   - memoryview：内存视图
###### 标准容器：`list`, `tuple`, `dict`, `set`
 - `list`: 可变，有序，元素可重复
 - `tuple`: 不可变，有序，元素可重复
 - `dict`: key-value对，key不可重复
 - `set`: 可变 不可重复，无序
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
###### 类方法，静态方法和实例方法：
- 类方法的应用：
  1. 替代构造函数
     - from_string() 方法提供了一种从字符串创建对象的替代方式，而不仅仅局限于标准的 __init__

  2. 访问和修改类变量
     - get_count() 方法访问类变量 employee_count，展示了类方法可以直接操作类级别的数据

  3. 批量创建实例
     - create_interns() 方法展示了如何使用类方法批量创建类的实例

  4. 支持继承
     - 所有这些类方法都使用 cls 而不是硬编码的类名，这样子类可以继承这些方法并且正确工作
```python
class Employee:
    # 类变量，跟踪所有员工数量
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        # 增加员工计数
        Employee.employee_count += 1
    
    def display_info(self):
        return f"姓名: {self.name}, 薪资: {self.salary}"
    
    @classmethod
    def from_string(cls, emp_string):
        """从格式化字符串创建员工对象"""
        name, salary = emp_string.split('-')
        return cls(name, float(salary))
    
    @classmethod
    def get_count(cls):
        """获取当前员工总数"""
        return cls.employee_count
    
    @classmethod
    def create_interns(cls, names):
        """批量创建实习生 - 固定薪资为2000"""
        interns = []
        for name in names:
            interns.append(cls(name, 2000))
        return interns

# 正常创建员工
emp1 = Employee("张三", 8000)
emp2 = Employee("李四", 9000)

# 使用类方法从字符串创建员工
emp3 = Employee.from_string("王五-7500")

# 获取员工总数
print(f"当前员工总数: {Employee.get_count()}")  # 输出: 当前员工总数: 3

# 批量创建实习生
intern_names = ["小明", "小红", "小华"]
interns = Employee.create_interns(intern_names)

# 检查创建的实习生
for intern in interns:
    print(intern.display_info())

# 再次获取员工总数
print(f"添加实习生后员工总数: {Employee.get_count()}")  # 输出: 添加实习生后员工总数: 6
```
- 静态方法的应用：
   用法：实现与类相关但不访问类的内部状态的功能；
   特点：不接收特殊的第一个参数（不像实例方法接收 self 或类方法接收 cls）
        不能访问或修改类属性或实例属性
```python
class MathHelper:
    
    @staticmethod
    def is_prime(n):
        """检查一个数是否是质数"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    @staticmethod
    def factorial(n):
        """计算阶乘"""
        if n < 0:
            raise ValueError("阶乘不能用于负数")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """摄氏度转华氏度"""
        return (celsius * 9/5) + 32
    
    @staticmethod
    def validate_number(value):
        """验证一个值是否为数字"""
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

# 直接通过类调用静态方法，无需创建实例
print(f"7是质数吗？{MathHelper.is_prime(7)}")  # 输出: 7是质数吗？True
print(f"8是质数吗？{MathHelper.is_prime(8)}")  # 输出: 8是质数吗？False

# 计算阶乘
print(f"5的阶乘是：{MathHelper.factorial(5)}")  # 输出: 5的阶乘是：120

# 温度转换
celsius = 25
fahrenheit = MathHelper.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C = {fahrenheit}°F")  # 输出: 25°C = 77.0°F

# 验证输入
values = [10, "20", "abc", None, 3.14]
for value in values:
    if MathHelper.validate_number(value):
        print(f"{value} 是一个有效的数字")
    else:
        print(f"{value} 不是一个有效的数字")
```
###### 函数变量的用法：
1. 回调
2. 高阶函数
仅留个记录，具体作用会展开



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
###### 循环的创建字典：
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

###### eval()函数：
可以直接运行字符串：
```python
eval("1+1")
```


##### 高级一点的用法：
###### 可迭代对象，迭代器
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
**注意：** 要使用 __iter__()，需要在一个类中定义它，并且通常还需要定义 __next__() 方法或者让 __iter__() 返回一个实现了 __next__() 的对象来创建一个迭代器;
```python
class MyIterable:
    def __init__(self, data):
        self.data = data
    def __iter__(self):
        return iter(self.data)
```
**注意这里返回的是其它类型的迭代器；**


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
**区别：`__iter__`：需要配合 `__next__` 方法一起使用，实现完整的迭代器协议**
`__getitem__`：只需要实现一个方法，通过索引访问元素。

- 关于iter()函数：不是类方法但也返回可迭代对象的迭代器；
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
迭代器是实现了 `__iter__()` 方法**和** `__next__()` 方法的对象。


**`__iter()__`,`__next()__`和`__getitem()__`的区别：**
`__getitem()__`：实现了`__getitem()__`方法的对象是可迭代对象，而不是迭代器。`__getitem()__`方法接受一个索引参数，返回对应位置的元素。`__getitem()__`方法可以通过索引访问元素，但不能实现惰性计算，也不能保存状态信息。
- `__iter()__`：返回可迭代对象，next()返回迭代器；只实现`__next()__`的话不能for;

```python
print("=== 1. 基础迭代器例子 - 数字范围 ===")

class NumberRange:
    """生成指定范围内的数字"""
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start
    
    def __iter__(self):
        return self    ###========注意这里返回的是自身；
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result

# 使用例子
print("生成 1 到 5 的数字:")
for num in NumberRange(1, 6):
    print(f"  {num}")

print("\n生成 0 到 10 的偶数:")
for num in NumberRange(0, 11, 2):
    print(f"  {num}")
```

**迭代器与可迭代对象区别：**
1. 消耗性
迭代器是消耗性的，一旦迭代完就不能重新迭代
可迭代对象可以重复迭代，每次迭代都会创建新的迭代器
2. 内存效率
迭代器是惰性的，只在需要时才生成下一个值
可迭代对象通常会在内存中保存所有元素
3. 访问方式
可迭代对象支持索引、切片等操作（如果实现了__getitem__）
迭代器只能按顺序访问，不能回退或随机访问
4. 使用场景：
可迭代对象适合：需要多次遍历数据;需要随机访问元素;数据量较小，可以全部加载到内存
迭代器适合：处理大量数据;生成无限序列;只需要遍历一次;需要节省内存

- 判断是不是可迭代对象/可迭代
```python
from collections.abc import Iterable,Iterator
isinstance(obj,Iterable) # 判断obj是否是可迭代对象
isinstance(obj,Iterator) # 判断obj是否是迭代器
``` 

###### 生成器
- 生成器是一种特殊的迭代器,使用 yield 关键字定义生成器函数,生成器函数执行时不会一次性生成所有值，而是在需要时才生成下一个值,这种"延迟计算"的特性使得生成器特别适合处理大量数据

- 在 Python 里，“生成器（generator）”是一类 特殊的迭代器。它遵循迭代器协议——实现 __iter__() 并返回自身，以及 __next__()——但生成器 不是手写这两个方法，而是由：

生成器函数：函数体里出现 yield 关键字

生成器表达式：形如 (expr for x in iterable)

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
相当于: 
```python
say_hello = my_decorator(say_hello)
say_hello()
```

- 使用functools.wraps保留原函数信息：
例子见notebook

wraps函数复制了以下属性：
```python
WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__annotations__', '__doc__')
WRAPPER_UPDATES = ('__dict__',)
```
这些属性被赋值到 wrapper 上，使其看起来就像原始函数。




###### 参数化装饰器
参数化装饰器使用一个外层函数接受参数：
```python
def log(prefix):  # 外层函数，接受参数
    def decorator(func):  # 真正的装饰器
        def wrapper(*args, **kwargs):
            print(f"{prefix} - Calling {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator  # 返回装饰器

@log("INFO")
def greet(name):
    print(f"Hello, {name}!")
```
相当于：
```python
greet = log("INFO")(greet)
greet("Alice")
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

3.1 ValueError
```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is too high")
    return age

# 使用示例
try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")  # 输出: Error: Age cannot be negative
```


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

###### 回调：
回调(Callback)是指将一个函数作为参数传递给另一个函数，并在特定事件发生或特定条件满足时被调用。这个被传递的函数就叫做回调函数。
1. 例1：错误处理
```python
def process_data(data, success_callback, error_callback):
    try:
        result = data / 0  # 可能出错的操作
        success_callback(result)  # 成功时的回调
    except Exception as e:
        error_callback(str(e))  # 错误时的回调

# 定义回调函数
def on_success(result):
    print(f"操作成功，结果是: {result}")

def on_error(error_msg):
    print(f"操作失败，错误信息: {error_msg}")

# 使用回调
process_data(10, on_success, on_error)
```

2. 例2：事件处理中的回调
```python
#事件处理中的回调
class EventSystem:

    def __init__(self):
        self.callbacks = {}
    
    def register(self, event_name, callback):
        if event_name not in self.callbacks:
            self.callbacks[event_name] = []
        self.callbacks[event_name].append(callback)
    
    def trigger(self, event_name):
        if event_name in self.callbacks:
            for callback in self.callbacks[event_name]:
                callback()

def on_start():
    print("Started!")

def on_end():
    print("Ended!")

# 使用事件系统
events = EventSystem()
events.register('start', on_start)
events.register('end', on_end)

events.trigger('start')  # 输出: Started!
events.trigger('end')    # 输出: Ended!

```

###### 函数工厂

###### 函数式编程和命令式编程

###### 高阶函数
高阶函数是指至少满足以下一个条件的函数：
- 接受一个或多个函数作为参数。
- 返回一个函数作为结果。
高阶函数的概念是函数式编程的核心之一，它允许函数像数据一样被传递和操作。

###### 描述符
允许自定义访问类属性时的行为：
例1：
```python
class ValidString:
    def __init__(self, minlen=0):
        self.minlen = minlen
        
    def __get__(self, obj, owner=None):
        return obj._name
    
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        if len(value) < self.minlen:
            raise ValueError(f'String too short, min length is {self.minlen}')
        obj._name = value

class Person:
    name = ValidString(minlen=3)  # 验证名字长度至少为3
    
    def __init__(self, name):
        self.name = name

# 使用
p = Person("Bob")      # 报错：名字太短
p = Person("Alice")    # 正确
p.name = "Jo"         # 报错：名字太短
p.name = 123          # 报错：不是字符串
```

- 注意描述符有obj参数。


###### 模块中的CLI接口
可以直接在命令行运行，避免写python脚本


##### 一些小点：
###### value[-1]和value[-1:]的区别：
- value[-1]：返回最后一个元素
- value[-1:]：返回最后一个元素的切片，返回的是一个包含最后一个元素的列表

###### setattr()
setattr(object, name, value)
设置对象的属性值。
The setattr() function is particularly useful when:
- The attribute name is determined dynamically at runtime
- You're working with attribute names that are stored in variables
- You need to set attributes programmatically

######  Nan,None,Inf的区别：
- Nan (Not a Number)：
  - 类型：浮点数的一种特殊值，属于float类型
  - 来源：数学运算中的未定义结果，在NumPy/PyTorch中常见
  - 特性：
    - 与任何值比较都返回 False，包括与自身比较
    - 参与的任何算术运算结果都是 NaN
  - 产生：
    - 0/0
    - 0*inf
    - inf-inf
    - inf/inf
    - inf*0

- None：
  - 类型：Python的内置单例对象，是NoneType类型的唯一实例
  - 来源：Python语言的内置类型，不是计算结果
  - 用途：表示变量没有值、缺失值或未初始化

- Inf (Infinity)：
  - 类型：浮点数的一种特殊值，属于float类型
  - 表示无穷大



#### numpy module
numpy数组的特点是高维，同类型元素。

##### ndarray 的组成：
ndarray 内部由以下内容组成：

- 一个指向数据（内存或内存映射文件中的一块数据）的指针。
- 数据类型或 dtype，描述在数组中的固定大小值的格子。
- 一个表示数组形状（shape）的元组，表示各维度大小的元组。
- 一个跨度元组（stride），其中的整数指的是为了前进到当前维度下一个元素需要"跨过"的字节数。

副本与拷贝的区别：
副本（View）：
- 共享底层数据
- 不分配新内存
- 原数组修改会影响副本
- 副本修改也会影响原数组
- 通常由切片、重塑等操作创建

拷贝（Copy）：
- 创建数据的完全独立副本
- 分配新内存
- 原数组修改不影响拷贝
- 拷贝修改不影响原数组
- 通过.copy()方法显式创建

产生副本的操作：
- 切片操作
- 转置
- 改变形状

产生拷贝操作：
- 使用.copy()方法

##### numpy 数据类型 dtype
1. 字节顺序的小端法与大端法：
- 小端法：低位字节存储在内存的低地址端，高位字节存储在内存的高地址端。
- 大端法：高位字节存储在内存的低地址端，低位字节存储在内存的高地址端。

- 例子：对于16位进制数0x12345678; 在计算机中通常按bit存储，1个字节(byte)等于8个比特(bit), 所以1个16进制位需要0.5个字节保存，两个16进制位需要1个字节保存。
所以0x12345678在内存中存储为：
0001 0010 | 0011 0100 | 0101 0110 | 0111 1000
按小端法存储为：(低位字节存储在内存的低地址端)
78 56 34 12 
按大端法存储为：(高位字节存储在内存的低地址端)
12 34 56 78

（0b是二进制，0o是八进制，0x是十六进制）

2. numpy中的数据类型：
- f       浮点型
- c       复数浮点型
- m       timedelta（时间间隔）
- M       datetime（日期时间）
- O       (Python) 对象
- S, a    (byte-)字符串
- U       Unicode
- V       原始数据 (void)

例如 int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替; 
这里的1，2，3，4指的是字节；

##### np.Ndarray的生成：
4种生成方法：
1. 用np.array()创建数组：
```python
numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
```
- 关于order: 指定行还是列优先。
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
    - np.empty(shape, dtype=float, order='C') #数组是元组形式传递，但也可以是列表；
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
    - np.random.randint(low, high=None, size=None, dtype=int) #low是下限，high是上限，size是元组形式传递；
    - size可以是多维的；如果只输入一个数比如randint(10),10是上界，0是下界；

3. 指定范围生成数组
- np.arrange(start, stop, step, dtype=None)
左闭右开；
- np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
- np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)

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
| ndarray.itemsize | 数组中每个元素的字节大小。|
| ndarray.nbytes | 数组中所有元素的字节大小。|
| ndarray.flags | 数组内存的读写模式。|


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

##### 迭代数组
函数：`np.nditer`
返回迭代器。
用order参数指定迭代顺序，有C和F两种，C是行优先，F是列优先；
用op_flags参数指定每个元素的读写模式，有readonly，readwrite，writeonly，以及readwrite+triviallayout，readwrite+same_kind，readwrite+refs_ok；
用flag参数控制
可以进行广播迭代

##### 数组操作
###### 改变数组形状
- `np.reshape(a, newshape, order='C')`
- `np.flatten(a, order='C')`
- `np.ndarray.flat`
注： np.flatten()和np.ndarray.flat的区别：
np.flatten()返回的是一个新数组，而np.ndarray.flat返回的是一个迭代器。
- `np.ravel(a, order='C')`
返回一个新的数组，该数组是原始数组的视图，因此改变返回的数组会影响原始数组。

###### 翻转数组
1. numpy.ndarry.T
对高维数组会完全反转轴序。
例子：
```python
import numpy as np
arr = np.arrange(24).reshape(2,3,4)
arr.T #形状为(4,3,2)
```
2. numpy.transpose(arr,axes)
axes用来指定新的轴序。
例子：
```python
import numpy as np
arr = np.arrange(24).reshape(2,3,4)
np.tranpose(arr,axes=(2,1,0)) #形状是(4,3,2)
```

3. numpy.rollaxis(arr, axis, start=0)
调整数据轴的顺序，类似于拿扑克牌时把一张牌插到另一张牌后面。
如果 axis 参数值大于或等于 normalized start，则 axis 从后向前滚动，直到 start 位置；如果 axis 参数值小于 normalized start，则 axis 轴从前往后滚动，直到 start 的前一个位置，即 start-1 位置
eg 1. start>axis
```python
import numpy as np
arr = np.arange(24).reshape(2,3,4)
np.rollaxis(arr,0,2) #返回的形状是：(3,4,2)
```
eg 2. start < axis
```python   
import numpy as np
arr = np.arange(24).reshape(2,3,4)
np.transpose(arr,2,0) #返回的形状是：(4,2,3)

```

4. numpy.swapaxes(arr, axis1, axis2)
交换两个轴
例子：
```python
import numpy as np
arr = np.arrange(24).reshape(2,3,4)
np.swapaxes(arr,0,2) #返回的形状是：(4,3,2)
```

###### 修改数组维度
1. numpy.broadcast(x,y):它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果
2. numpy.broadcast_to(array, shape, subok) 返回一个只读的视图；不能修改原值；
3. numpy.expand_dims(arr, axis)：相当于torch的unsqueeze函数
4. numpy.squeeze(arr, axis)


###### 连接数组
1. numpy.concatenate((a1, a2, ...), axis)：沿指定轴连接数组 
2. np.stack((a1,a2...),axis) :会改变数组维度
3. np.hstack和np.vstack 类似于np.concatenate的行为，不会改变数组维度；

###### 分割数组

###### 数组元素的添加和删除

##### 关于方法的双重实现：
reshape等方法可以通过np.reshape（）实现，也可以通过ndarray.reshape()实现。


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
np.where(condition, x, y):如果条件满足就从x中选取元素，否则就从y中选取元素；
例1：条件选择：
```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 2, arr, 0)
print(result)  # 输出: [0 0 3 4 5]
```
例2：条件查找：
```python
import numpy as np
arr_2d = np.array([1,2,3],[4,5,6])
result = np.where(arr_2d > 2)
print(arr_2d[result] )
```
例3： 从多个数组里选择
```python
import numpy as np
arr = np.array([1,2,3,4,5])
x = np.array([10,20,30,40,50])
y = np.array([100,200,300,400,500])
result = np.where(arr>2,x,y)
print(result)
```

###### np.concatenate()
###### np.expand_dims() , np.expand()
`np.expand_dims(a, axis)`
- `a`: 输入数组
- `axis`: 插入新轴的位置
例子：
```python
import numpy as np
a = np.array([1,2,3])
b = np.expand_dims(a, axis=0)
print(b)
```

没有np.expand()函数； 没有np.unsqueeze()函数； np.expand_dims()函数可以实现unsqueeze的功能；


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

###### np.einsum
`np.einsum(subscripts, *operands, out=None, dtype=None, order='K', casting='safe', optimize=False)`





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
Pandas主要有两种数据结构：DataFrame和Series。注意series也是有名字的。
Pandas转换为numpy： `DataFrame.values` 或 `DataFrame.to_numpy()`
Series转换为DataFrame: `Series.to_frame()`
Pandas与Numpy的主要区别：
- Pandas的索引可以有标签。
- Pandas各列数据是异质的。Numpy数据类型是同质的。
##### 1. `pd.read_csv`:
##### 2. `pd.DataFrame`：
   1. 一般用法：
   DataFrame 构造方法如下：
    `pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)`
   
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

       2. **两种从字典创建数据框的方法**：
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
       3. **从numpy数组创建数据框：**
       ```python
       import pandas as pd
       import numpy as np

       data = np.array([[1, 2, 3], [4, 5, 6]])
       df = pd.DataFrame(data, columns=['A', 'B', 'C'])
       print(df)
       ```

 3. **使用行/列的位置/标签索引**：`loc`/ `iloc`方法:(i的意思是index)
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
    1. 从csv中读取和写入文件：
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
    
    2. 指定每列的数据类型：(也可以在读取csv时指定)
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
    - `axis=1`：对列排序，通常基于索引或行的值排序。(GPT说axis是无效参数)
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
   返回一个 Series，包含每个值出现的次数。
value_counts() 是 Series 的方法。
    
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
    - pd.concat() 是直接用来拼接的，如果出现索引不匹配，会自动填充NaN；其它两个方法并不会自动填充，而是要指定how参数。
    比如左边数据框是id和年龄，右边数据框是id和姓名，按行拼接时，会自动填充只有一种数据的人的另一种属性为Nan。
    - 还可以按行拼接：

3. 基于索引的连接 — DataFrame.join(DataFrame,how='left') 
    索引是拼接列
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

1. Series.map(function):应用于Series的每个元素,可以是映射字典，可以是series
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

###### 转化为字典：DataFrame.to_dict()

```python
#寻找一个user交互过的所有item
user_history = pos_data.groupby('user_id').item_id.apply(list).to_dict()
```

###### DataFrame.str
用来处理字符串。
```python
# 转换大小写
df['column'].str.upper()      # 转大写
df['column'].str.lower()      # 转小写
df['column'].str.title()      # 首字母大写

# 去除空白
df['column'].str.strip()      # 去除两端空白
df['column'].str.lstrip()     # 去除左侧空白
df['column'].str.rstrip()     # 去除右侧空白
```

###### Series.unique()和Series.nunique()
Series.unique()：返回一个包含Series中唯一值的numpy数组。
Series.nunique()：返回一个包含Series中唯一值的计数。


##### 注意事项：
###### 1.多条件选择时用 & 和 | 连接，不要用 and 和 or。
因为and和or是布尔运算符，而&和|是位运算符。





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
###### torch.flatten
用法：`torch.flatten(input, start_dim=0, end_dim=-1) -> Tensor`
将输入张量展平为一维。
start_dim和end_dim是维度索引，从0开始。通常start_dim=1,从而保持batch维度。
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

###### torch.mul
用法：`torch.mul(input, other, *, out=None) -> Tensor`
逐元素相乘，要求两个张量形状相同。

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

###### tensor.gather
用法：`torch.gather(input, dim, index, out=None) -> Tensor`
用于根据索引从输入张量中收集元素。
参考：[https://blog.csdn.net/iteapoy/article/details/106203954](https://blog.csdn.net/iteapoy/article/details/106203954)

###### torch.tensordot(a,b,dims=2)
用于高维张量的收缩操作；
- dims：
    - 如果是整数 n，则对 a 的最后 n 个维度和 b 的前 n 个维度进行收缩
    - 如果是两个列表/元组（如 ([a1, a2], [b1, b2])），则分别指定 a 和 b 上要收缩的维度

可以指定两个tensor是哪一个维度做内积，然后循环做内积；
只指定一个整数nn时是第一个张量的后n个维度与第二个张量的前n个维度做内积。


###### torch.einsum()
参考：[https://zhuanlan.zhihu.com/p/71639781](https://zhuanlan.zhihu.com/p/71639781)
[https://blog.csdn.net/ViatorSun/article/details/122710515](https://blog.csdn.net/ViatorSun/article/details/122710515)



###### tensor.permute(*dims)或函数式接口：torch.permute(tensor,dims)
用法：`tensor.permute(*dims)`或`torch.permute(tensor,dims)`
沿着指定的维度重新排列张量。

- 关于*dims和dims的区别：
    - 对于tensor.permute(*dims)，可以写成tensor.permute(1, 0, 2)，但不能写成：tensor.permute([1, 0, 2])
    - 对于torch.permute(tensor,dims)，可以写成torch.permute(tensor, [1, 0, 2])，但不能写成：torch.permute(tensor, 1, 0, 2)

###### tensor.view()和tensor.reshape()的区别：
.view()要求张量连续，与原始数据共享内存，但.reshape()不要求张量连续,且不共享内存。
尽量用reshape()就行；


###### tensor.repeat(*sizes)
用法：`tensor.repeat(*sizes)`
沿着指定的维度重复张量。
*size表示表示沿着指定维度重复的次数；
**示例**：
```python
import torch

# 创建一个张量
x = torch.tensor([1, 2, 3])

x.repeat(2,3) 
#tensor([[1, 2, 3, 1, 2, 3, 1, 2, 3],
#        [1, 2, 3, 1, 2, 3, 1, 2, 3]])
```

###### tensor.split(split_size_or_sections, dim=0)
用法：`tensor.split(split_size_or_sections, dim=0)`
沿着指定的维度分割张量。
- split_size_or_sections：
    - 如果是整数，表示每块的大小
    - 如果是列表或元组，表示每块的具体大小
- dim：在哪个维度上分割，默认是第0维


###### torch.stack


###### torch.unique 
- 如果是三维，dims也不能输入元组，需要手动改变形状；
- 不像numpy.unique一样有return_index参数；




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





##### 关于注册参数的操作
###### self.register_parameter
用法：`self.register_parameter(name, param)`
用来注册参数，参数是nn.Parameter类型。

###### self.parameters()
用法：`self.parameters()`
返回一个迭代器，包含所有可训练的参数。
可以用list(self.parameters())转换为列表。

###### self.named_parameters()
用法：`self.named_parameters()`
返回一个迭代器，包含所有可训练的参数，并返回参数的名称。

##### nn.EmbeddingBag
nn.EmbeddingBag 是 PyTorch 中的一个层，用于处理变长序列的嵌入。它的主要特点是可以对一个"袋子"(bag)里的嵌入向量进行池化操作（如求和或平均）。
```python
import torch
import torch.nn as nn

class BagOfWordsModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()
        self.embedding = nn.EmbeddingBag(vocab_size, embedding_dim, mode='mean')
        self.fc = nn.Linear(embedding_dim, 2)  # 二分类
        
    def forward(self, text, offsets):
        embedded = self.embedding(text, offsets)
        return self.fc(embedded)

# 使用示例
vocab_size = 1000
embedding_dim = 32
model = BagOfWordsModel(vocab_size, embedding_dim)

# 假设我们有两个文档，每个文档包含不同数量的词
text = torch.tensor([1, 2, 4, 5, 4, 3, 2, 9])  # 所有文档的词索引连接在一起
offsets = torch.tensor([0, 4])  # 第一个文档从索引0开始，第二个从索引4开始

# 前向传播
output = model(text, offsets)
print(output.shape)  # torch.Size([2, 2])
```


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
###### self.modules()
返回一个迭代器，包含所有子模块。
例如：
```python
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 3)
        self.relu = nn.ReLU()
        self.fc = nn.Linear(32 * 26 * 26, 10)

    def forward(self, x):
        return self.fc(self.relu(self.conv1(x)).view(x.size(0), -1))

model = MyModel()

# 遍历所有模块
for m in model.modules():
    print(m)

```
会输出 MyModel、Conv2d、ReLU、Linear 四个模块。



##### 关于梯度的操作
###### tensor.retain_grad()
在 PyTorch 中，只有叶子节点的张量（leaf tensor）默认会保留梯度，非叶子张量的 .grad 属性在反向传播后是 None，如果你想获取它们的梯度，就要用 .retain_grad()。

###### tensor.requires_grad

###### loss.backward()的参数：
默认为torch.ones_like(loss);
其它情况：
```python
import torch

# 创建一个简单的计算图
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x * 2  # y = [2.0, 4.0, 6.0]

# 情况1: 使用全1梯度
y.backward(torch.ones_like(y))
print("情况1 - 全1梯度:", x.grad)  # 输出: tensor([2., 2., 2.])
x.grad.zero_()  # 清除梯度

# 情况2: 使用不同的权重
y.backward(torch.tensor([1.0, 2.0, 3.0]))
print("情况2 - 不同权重:", x.grad)  # 输出: tensor([2., 4., 6.])
x.grad.zero_()

# 情况3: 使用负值
y.backward(torch.tensor([-1.0, -1.0, -1.0]))
print("情况3 - 负梯度:", x.grad)  # 输出: tensor([-2., -2., -2.])
x.grad.zero_()

# 情况4: 使用零值
y.backward(torch.tensor([0.0, 0.0, 0.0]))
print("情况4 - 零梯度:", x.grad)  # 输出: tensor([0., 0., 0.])
```
情况1：每个输出元素对梯度的贡献相等，所以每个输入元素的梯度都是2（因为 y = x * 2）
情况2：第二个和第三个输出元素对梯度的贡献更大，所以它们的梯度也更大
情况3：梯度方向相反，表示我们想要最小化而不是最大化输出
情况4：没有梯度传播，因为所有输出元素的权重都是0

##### 关于torch.autograd.Function
- 通过两个静态方法：forward和backward函数自定义forward和backward过程;
- 有上下文管理对象ctx;
- backward的参数：
  ```python
  backward(ctx, *grad_outputs)
  ```
  - 参数：
    - ctx: 上下文对象，从 ctx.saved_tensors 中获取在 forward 里保存的中间变量
    - *grad_outputs: 输出对 loss 的梯度（∂L/∂output），也叫"上游梯度"。如果 forward 返回多个输出，这里就会有多个 grad
  - 返回值：
    - 返回每个 forward 输入的梯度（∂L/∂input）
    - 如果某个输入不需要梯度，可以返回 None
例子：
```python
import torch
from torch.autograd import Function

class ScaleFunction(Function):
    @staticmethod
    def forward(ctx, x, scale_factor):
        # 保存scale_factor用于反向传播
        ctx.save_for_backward(scale_factor)
        # 前向传播：将输入乘以缩放因子
        return x * scale_factor

    @staticmethod
    def backward(ctx, grad_output):
        # 获取保存的scale_factor
        scale_factor, = ctx.saved_tensors
        # 反向传播：梯度乘以缩放因子
        return grad_output * scale_factor, None

# 使用示例
def test_scale_function():
    # 创建输入张量
    x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
    scale_factor = torch.tensor(2.0)
    
    # 使用自定义函数
    y = ScaleFunction.apply(x, scale_factor)
    
    # 计算梯度
    y.sum().backward()
    
    print("输入:", x)
    print("输出:", y)
    print("输入梯度:", x.grad)  # 应该看到梯度都是2.0

# 运行测试
test_scale_function()
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
##### 如果终端窗口不够长，如何查看历史输出
如果您是在普通终端中：
使用鼠标滚轮向上滚动
或使用 Shift+PageUp 向上滚动
如果您在使用screen：
按 Ctrl+a 然后按 [ 键进入滚动模式
使用方向键或PageUp/PageDown键滚动
按 Esc 键退出滚动模式
如果您在使用tmux：
按 Ctrl+b 然后按 [ 键进入复制模式
使用方向键或PageUp/PageDown键滚动
按 q 键退出复制模式
根据您的终端提示，您可能正在使用screen，试试第二种方法。

### C++ 笔记
#### typedef
typedef 是 C/C++ 中用于给已有类型起别名的关键字； 更推荐使用using;
给普通类型起别名，如：
```cpp
typedef int my_int;
my_int a = 10;
```
给函数指针起别名，如：
```cpp
typedef int (*func_ptr)(int, int);
func_ptr add = [](int a, int b) -> int { return a + b; };
```

#### 匿名函数
```cpp
[capture](parameter_list) -> return_type { function_body }
```
- capture: 捕获列表，可以捕获外部变量
- parameter_list: 参数列表
- return_type: 返回类型
- function_body: 函数体

例子：
```cpp
int x = 100;
auto add = [x](int a) -> int { return a + x; };
add(10);
```
#### void的用法：
1. 函数返回类型	void func()	表示这个函数没有返回值
2. 指针类型	void *ptr	表示这是一个"不定类型"的指针，可以指向任何类型

#### 模板库：
C++ 标准模板库（STL）：
C++ 标准模板库（STL：Standard Template Library）是 C++ 最重要的模板库之一。

STL 包含：
| 组件 | 说明 | 示例 |
|------|------|------|
| 容器 | Containers | vector, list, map, set |
| 算法 | Algorithms | sort, find, copy, accumulate |
| 迭代器 | Iterators | begin(), end(), 自定义迭代器 |

一个例子：
```cpp
#include <vector>
#include <algorithm>
#include <iostream>

int main() {
    std::vector<int> v = {3, 1, 4, 1, 5};
    std::sort(v.begin(), v.end());
    for (int i : v) std::cout << i << " ";  // 输出 1 1 3 4 5
}
```

#### vector的用法：
定义：
```cpp
std::vector<int> v={1,2,3,4,5};
```
常用方法：
- `v.push_back(x)`: 在末尾添加元素
- `v.size()`: 返回元素个数
- `v[10]`: 访问第10个元素
- 循环：
```cpp
for (int i : v) std::cout << i << " ";
```

#### set的用法：
用于存储不重复的元素，并且这些元素会自动按照升序排序，只读元素：不能直接修改某个元素的值。
```cpp
std::set<int> s = {1,2,3,4,5};
```
常用方法：
- `insert(val)`: 插入元素
- `erase(val)`: 删除元素
- `find(val)`: 查找元素，返回迭代器
- `count(val)`: 返回元素出现次数，由于是set，所以返回值只能是0或1
- `size()`: 返回元素数量
- `clear()`: 清空集合
- `begin()/end()`: 返回迭代器
- `empty()`: 判断集合是否为空

#### unordered_set的用法：
用于存储不重复的元素，但是这些元素不会自动按照升序排序。
```cpp
std::unordered_set<int> s = {1,2,3,4,5};
```
常用方法：
- `insert(val)`: 插入元素
- `erase(val)`: 删除元素
- `find(val)`: 查找元素，返回迭代器
- `count(val)`: 返回元素出现次数，由于是unordered_set，所以返回值只能是0或1
- `size()`: 返回元素数量
- `clear()`: 清空集合
- `begin()/end()`: 返回迭代器
- 循环：
```cpp
for (auto x : us) std::cout << x << " ";
```

### git 命令
#### git status
1. 一个例子：本地仓库落后远程仓库1个commit，且工作区有修改。
```bash
PS A:\coding\learn_git> git status
On branch main
Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   hello_world.py

no changes added to commit (use "git add" and/or "git commit -a")
```
最后一行由于没有stage的内容，所以也就没有可以commit的内容.
2. 一个例子：
```bash
git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours) ##### 您的本地分支有 1 个远程没有的提交，远程分支有 1 个您本地没有的提交，两个分支"分歧"了

You have unmerged paths. # 有未解决冲突
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   hello_world.py

no changes added to commit (use "git add" and/or "git commit -a")
```
#### git pull = git fetch + git merge

#### git ls-files 相关
git ls-files 是一个 Git 命令，用来列出当前 Git 仓库中被 Git 跟踪的所有文件。它会显示已添加到 Git 索引（暂存区）的文件

#### git diff 相关
- git diff 查看工作区与暂存区差异
- git diff --cached(或--staged) 查看暂存区与最近提交差异
- git diff HEAD 查看工作区与最近提交差异
- git diff <file> 查看工作区与暂存区差异
- git diff --cached <file> 查看暂存区与最近提交差异
- git diff HEAD <file> 查看工作区与最近提交差异
- git diff <commit1> <commit2> 查看两个提交之间的差异
- git diff <commit> <file> 查看某个提交与某个文件的差异

git diff 的输出：统一差异格式（unified diff):
一个例子：
```bash
diff --git a/example.txt b/example.txt ##### a表示左侧，b表示右侧
index 3b18e72..a5f9c1e 100644
--- a/example.txt
+++ b/example.txt
@@ -1,4 +1,5 @@ ###### 表示旧版本的1到4行，新版本的1到5行；
-Hello, world!  #### -表示旧版本有，新版本无
 This is a demo file. ### 没符号表示没变化
+We have added this new line. ### +表示新版本有，旧版本无
 And this line remains unchanged.
+Another addition here.
```

#### git stash 相关：
- `git stash list`: 
- `git stash pop [<stash>@{<idx>}] [--index]`: 将指定（默认是最新的）stash 条目中的改动重新应用到当前工作区和暂存区
- `git stash`: 
- `git stash push --staged`:只保留暂存区内容；
- `git stash push file`: stash某文件；
-  

#### git checkout 相关
- `git checkout -- <file>`: 还原暂存区版本；
- `git checkout HEAD --<file>`: 还原到最后一次提交，
- `git checkout <branch>`: 切换分支
- `git checkout <commit-id> -- <file-name>`: 将文件还原到指定版本的内容;会同时写入工作区和暂存区；

#### git reset 相关
- git reset <file>: 将指定文件从暂存区移除，但保留工作区的修改内容。

#### git restore
用来替代git checkout和git reset
如果文件被暂存，git restore --staged <file>: 将指定文件从暂存区移除，但保留工作区的修改内容。
如果文件未被暂存，git restore <file>: 会还原成暂存区版本；

#### 其它
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

#### 疑问
1. 如果给远程推送的时候有覆写，会不会推送成功？

### github 网站教程
#### review a pull request
Reviewing a pull request is an opportunity to examine another contributor's changes and give them feedback.

#### 一些编程思想
##### 向量化思想
从数据框里取数，不要一行一行的取，而是把index组成numpy，一下子取出来，这样速度快。







### Conda环境
#### 小知识
##### Linux中conda环境位置：
`/home/用户名/.Conda `
##### 包的位置：
`/home/用户名/.Conda/envs/环境名/lib/python3.10/site-packages`
##### nltk下载文件的位置：
`~/.nltk_data`
##### .conda/pkgs 内容：
在 .conda/pkgs 目录下，conda 会存储你安装的所有包的缓存文件。


### Linux:
#### 使用乌邦图的常识：
##### 命令行窗口使用crtl+shift+C和ctrl+shift+V进行粘贴复制；
##### 右键没有新建文件的问题： 
GNOME 桌面环境（如 Ubuntu 默认桌面）中常见的问题：默认没有“右键新建文档”选项。GNOME 的右键菜单“新建文档”功能，是基于一个 模板文件夹（Templates） 来显示的。如果 ~/Templates 目录中没有文件，右键菜单就不会显示“新建文档”。 使用如下：
```bash
mkdir -p ~/Templates
touch ~/Templates/Empty\ Document.txt
```
之后就有了；


#### shell与bash:
- Shell（壳）
Shell 是一个程序，它提供了一个用户与操作系统（如 Linux、Unix）进行交互的界面。就像它的名字"壳"一样，它是包裹在操作系统核心（kernel）外面的一层。
- bash: 是 Linux 系统默认的 shell 程序，它提供了丰富的命令行功能和脚本编程能力。

#### 超级用户(root)
登录后可以用su命令切换到超级用户；
su - username 切换到指定用户；
sudo 以超级用户权限执行命令；

#### 用户组
groups 查看当前用户所属组
（每个用户都有一个同名主组）
示例：
```Shell
$ groups
zhi-li adm cdrom sudo dip plugdev users lpadmin
# 显示当前用户 zhi-li 属于多个用户组:
# - zhi-li (主组)
# - adm
# - cdrom 
# - sudo
# - dip
# - plugdev
# - users
# - lpadmin
```

#### 文件属性
- ls -l 查看文件属性
  - 显示出来的第一行total表示当前目录下所有文件和子目录所占用的磁盘块（block）总数 但不计算子目录内文件占用磁盘数量
  - 其余内容包括文件类型、权限、硬链接数、所属用户、所属组、文件大小、修改时间、文件名


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


#### /opt和/usr区别：
/usr 是系统标准软件的"共享仓库"，而 /opt 是"外来的大软件"专属地盘。

/usr vs /opt 对比表：
| 特性 | /usr | /opt |
|------|------|------|
| 用途 | 系统自带 & 标准包管理器安装的软件（如 APT 安装的） | 外部提供的独立大软件（通常是第三方预编译包） |
| 结构 | 拥有多个子目录，如 /usr/bin, /usr/lib, /usr/share 等 | 每个软件一个子目录，如 /opt/google/chrome/ |
| 管理方式 | 通常由包管理器（如 apt、dpkg）管理 | 通常是用户手动解压或安装的 |
| 设计目标 | 提供给所有用户共享的软件库和工具 | 容纳"非标准"、自包含、不会影响系统的独立应用 |
| 示例 | /usr/bin/vim, /usr/lib/libc.so.6 | /opt/pycharm, /opt/Matlab, /opt/Google/chrome |
#### 桌面图标的位置：
`/usr/share/applications/`
#### `/bin`和`/usr/bin`和`/usr/local/bin`的区别：
- `/bin`：存放的是系统启动和运行最基本的可执行程序，在系统尚未挂载 /usr、网络不可用、图形界面没启动之前，系统就必须能执行这些命令；，如 `ls`, `cp`, `mv`,`rm` 等。
- `/usr/bin`：/usr/bin 是 Linux 中用于存放非基本命令的用户级可执行程序（binary executables）的目录，如 `ssh`,`vim`,`code`(VScode) 等。
- `/usr/local/bin`：/usr/local 是为“本地手动安装的软件”预留的目录，用于区别于系统软件包管理器（如 apt、yum）自动安装的软件。
自定义安装的是指：解压 .tar.gz 到某路径，下载 .AppImage、.run、.sh 安装脚本， 通过./configure && make && sudo make install 安装。
### 编译安装和独立软件仓
- 编译安装：./configure && make && sudo make install
#### 关于文件结构
🧱 /bin, /lib, /sbin: 系统核心组件

👨 /home, /root: 用户家目录

⚙️ /etc: 配置大本营

🧪 /proc, /sys: 内核接口

🧳 /opt, /usr, /var: 应用和数据的集合区

⛺ /tmp, /mnt, /media: 临时或挂载区


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
5. vscode 下 git diff 视图：左边是历史，右边是当前的
6. 多行光标：
✅ 在 VS Code 中选中 某单词 批量编辑：
方法一：使用 Ctrl + D（或 Cmd + D on Mac）
将光标放在第一个 某单词 上。

连续按 Ctrl + D（Mac 是 Cmd + D）可以逐个选中下一个相同的单词。

多个光标出现后即可同步修改。

方法二：Ctrl + Shift + L（或 Cmd + Shift + L）
用鼠标或键盘选中一次 某单词。

然后按 Ctrl + Shift + L（Mac 是 Cmd + Shift + L）。

所有相同的文本会被添加为多光标，一起编辑。

方法三：Alt + Click 添加光标到每一行
如果 某单词 分布位置不同，可使用 Alt + Click 手动在每一行上添加光标。
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
    - **HTTP**：现代浏览器会标记 HTTP 网站为"不安全"。
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

##### 前端与后端
###### 前端（Frontend）
1. 定义: 前端是用户直接交互的部分，通常称为客户端。它包括网页的视觉部分和用户体验。
2. 技术栈:
HTML (HyperText Markup Language): 用于创建网页的结构。
CSS (Cascading Style Sheets): 用于设计和布局网页的外观。
JavaScript: 用于实现网页的动态功能和交互。
3. 框架和库:
React: 一个用于构建用户界面的JavaScript库。
Angular: 一个由Google开发的前端框架。
Vue.js: 一个渐进式JavaScript框架。
4. 职责:
设计和实现用户界面。
确保网页在不同设备和浏览器上的兼容性。
提供良好的用户体验和交互。
###### 后端（Backend）
1. 定义: 后端是支持前端的服务器端部分，负责数据处理、业务逻辑和数据库管理。
2. 技术栈:
服务器端语言: 如Python, Java, Ruby, PHP, Node.js。
数据库: 如MySQL, PostgreSQL, MongoDB。
服务器: 如Apache, Nginx。

3. 框架:
Django: 一个Python的Web框架。
Spring: 一个Java的Web框架。
Express.js: 一个Node.js的Web框架。
4. 职责:
处理来自前端的请求。
管理和操作数据库。
实现应用程序的业务逻辑。
确保数据的安全性和完整性。
###### 交互
API (Application Programming Interface): 前端和后端通过API进行通信。API定义了前端如何请求数据以及后端如何响应这些请求。

##### 技术栈
技术栈（Tech Stack）是指在软件开发中使用的一组技术、工具和框架的集合。它包括用于构建应用程序的所有技术层，从前端到后端，再到数据库和服务器。技术栈通常分为以下几个主要部分

##### Tab的含义
"Tab" 在计算机领域有多个含义，具体要看上下文。常见的几种意思如下：

制表符（Tab Key）：键盘上的 Tab 键，通常用于在文本编辑器或代码编辑器中插入制表符（\t），或者在表单和界面元素之间切换。

e.g. Press Tab to indent the code.（按 Tab 键缩进代码。）
浏览器标签页（Browser Tab）：网页浏览器（如 Chrome、Firefox）中的标签页，每个 Tab 代表一个打开的网页。

e.g. I have too many tabs open in my browser.（我的浏览器打开了太多标签页。）
软件界面中的选项卡（UI Tab）：许多应用程序（如 Excel、VS Code）都使用 Tab 来组织不同的页面或功能。

e.g. Switch to the "Home" tab in Excel.（切换到 Excel 的"主页"选项卡。）
代码缩进方式（Tab vs. Space）：在编程中，Tab 也可以指用 制表符（Tab） 进行缩进，而不是使用空格（Space）。不同项目可能有不同的代码风格。

e.g. Some programmers prefer tabs over spaces for indentation.（有些程序员喜欢用 Tab 代替空格进行缩进。）

##### icon和buttom的区别
Icon 和 Button 是两种常见的 UI (用户界面) 元素，它们在功能和外观上有所不同。以下是它们之间的主要区别：

Icon (图标)
定义：图标通常是一个小的、简洁的 图形，用于表示某种功能、操作或内容。图标通常不包含文字，依靠视觉元素（例如图形或符号）来传达信息。

功能：图标本身通常是 点击或触摸的目标，但它并不总是作为“按钮”来使用。有时图标只是用作表示某些功能的视觉元素。

外观：图标通常较小，简洁，形状多样（如圆形、方形、符号等）。

例子：例如，在大多数应用程序中，放大镜图标表示搜索，信封图标表示邮件，齿轮图标表示设置。

Button (按钮)
定义：按钮是一种交互式元素，通常包含 文字、图标或两者结合，并且明确表示用户可以 点击它来执行某个操作。按钮通常具有较大的可点击区域，易于识别。

功能：按钮通常用于触发某些操作，比如提交表单、切换页面或触发事件。按钮上的文字或图标会明确告诉用户这个按钮的用途。

外观：按钮通常比图标大，并且会有 可视化的变化（如背景颜色变化或浮动效果），以明确告诉用户它是一个交互式元素。

例子：例如，页面上的“提交”按钮、社交媒体应用中的“点赞”按钮、或网站上的“注册”按钮

##### 语法糖
语法糖（Syntactic Sugar）是指在编程语言中，通过提供一些更简洁、更易读的语法形式，使得程序员可以更方便地书写代码。这种语法的变化并不会改变程序的功能或逻辑，只是让代码更直观、简洁、易懂
比如
- 列表推导式：
```python
result = []
for i in range(10):
    if i % 2 == 0:
        result.append(i)
print(result)
```
可以简化为：
```python
result = [i for i in range(10) if i % 2 == 0]
```
- 装饰器：
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

def say_hello(name):
    print(f"Hello, {name}!")

say_hello = decorator(say_hello)  # 手动应用装饰器
say_hello("Alice")
```
可以简化为：
```python
@decorator
def say_hello(name):
    print(f"Hello, {name}!")
```