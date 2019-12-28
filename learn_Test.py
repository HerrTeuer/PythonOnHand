##L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
##print(L)



### decorator
##import time, functools
##def metric(fn):
##    @functools.wraps(fn)
##    def wrapper(*args, **kw):
##        print('%s executed in %s ms' % (fn.__name__, time.process_time()))
##        return fn(*args, **kw)
##    return wrapper
##
### 测试
##@metric
##def fast(x, y):
##    time.sleep(0.0012)
##    return x + y;
##
##@metric
##def slow(x, y, z):
##    time.sleep(0.1234)
##    return x * y * z;
##
##f = fast(11, 22)
##s = slow(11, 22, 33)
##if f != 33:
##    print('测试失败!')
##elif s != 7986:
##    print('测试失败!')




### 实例属性和类属性
##class Student(object):
##    count = 0
##    def __init__(self, name):
##        self.name = name
##        Student.count=self.count+1;
##
### 测试:
##if Student.count != 0:
##    print('测试失败!')
##else:
##    bart = Student('Bart')
##    if Student.count != 1:
##        print('测试失败!')
##    else:
##        lisa = Student('Bart')
##        if Student.count != 2:
##            print('测试失败!')
##        else:
##            print('Students:', Student.count)
##            print('测试通过!')
##

### 使用@property
##class Screen(object):
##    @property
##    def width(self):
##        return self._width
##    @property
##    def height(self):
##        return self._height
##
##    @property
##    def resolution(self):
##        return self._width*self._height
##
##    @width.setter
##    def width(self,value):
##        self._width = value;
##
##    @height.setter
##    def height(self,value):
##        self._height = value;
### 测试:
##s = Screen()
##s.width = 1024
##s.height = 768
##print('resolution =', s.resolution)
##if s.resolution == 786432:
##    print('测试通过!')
##else:
##    print('测试失败!')


# 使用枚举类
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：
from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
