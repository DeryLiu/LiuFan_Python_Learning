'''
improt random

random.random()

生成0-1的小数

>>> random.random()
0.06511225392331632
>>> random.random()
0.9063480964287944
>>> random.random()
0.1255900898753961
>>> random.random()
0.6676866041289258
random.randint(a, b)

输出a和b范围内的数，包括a和b

>>> random.randint(1,2)
1
>>> random.randint(1,2)
1
>>> random.randint(1,2)
1
>>> random.randint(1,2)
2
>>> random.randint(1,2)
1
>>> random.randint(1,2)
1
random.randrange(start, stop[, step])

输出start到stop-1之间的数，可设置步长

>>> random.randrange(1,3)
2
>>> random.randrange(1,3)
1
>>> random.randrange(1,3)
2
随机验证码实例

#!/usr/bin/env python
import random
checkcode = ''
# for循环四次
for i in range(4):
    # current=0-3的数字
    current = random.randrange(0,4)
    # 如果current的值不等于i
    if current != i:
        # 通过chr把数字转换为一个字母赋值给temp
        temp = chr(random.randint(65,90))
    else:
        # 否则temp=0-9之间的数字
        temp = random.randint(0,9)
    # checkcode = checkcode + str(temp)
    checkcode += str(temp)
# 输出字符
print(checkcode)
执行

ansheng@ansheng-me:~$ python s.py
TCQ1
ansheng@ansheng-me:~$ python s.py
8L01
ansheng@ansheng-me:~$ python s.py
N2EB
ansheng@ansheng-me:~$ python s.py
XIDO
'''