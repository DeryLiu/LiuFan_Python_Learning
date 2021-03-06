'''
logging模块用于便捷记录日志且线程安全。

日志级别

Level	Numeric value
CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0
只有大于当前日志等级的操作才会被记录。
'''

'''实例'''

# 写入单文件

import logging
# 创建一个log.log日志文件
logging.basicConfig(filename='log.log',
                    # 格式化的字符串
                    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s',
                    # 时间
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    # 错误级别
                    level=logging.NOTSET
                    )
logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')
logging.log(logging.INFO, 'NOTSET')

'''
执行结果
ansheng@ansheng-me:~$ ls
log.py
ansheng@ansheng-me:~$ python log.py
ansheng@ansheng-me:~$ ls
log.log  log.py
ansheng@ansheng-me:~$ cat log.log
2016-05-27 21:46:15 PM - root - CRITICAL - log: critical
2016-05-27 21:46:15 PM - root - ERROR - log: error
2016-05-27 21:46:15 PM - root - WARNING - log: warning
2016-05-27 21:46:15 PM - root - INFO - log: info
2016-05-27 21:46:15 PM - root - DEBUG - log: debug
2016-05-27 21:46:15 PM - root - INFO - log: NOTSET
logging.basicConfig函数各参数
'''

'''
参数	说明
filename	指定日志文件名
filemode	和file函数意义相同，指定日志文件的打开模式，’w’或’a’
format	指定输出的格式和内容，format可以输出很多有用信息，如下所示
datefmt	指定时间格式，同time.strftime()
level	设置日志级别，默认为logging.WARNING
format参数

参数	说明
%(levelno)s	打印日志级别的数值
%(levelname)s	打印日志级别名称
%(pathname)s	打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s	打印当前执行程序名
%(funcName)s	打印日志的当前函数
%(lineno)d	打印日志的当前行号
%(asctime)s	打印日志的时间
%(thread)d	打印线程ID
%(threadName)s	打印线程名称
%(process)d	打印进程ID
%(message)s	打印日志信息
'''

# 多文件日志
# 对于上述记录日志的功能，只能将日志记录在单文件中，如果想要设置多个日志文件，logging.basicConfig将无法完成，需要自定义文件和日志操作对象。

import logging
# 创建文件
file_1 = logging.FileHandler("log1.log", "a")
# 创建写入的日志格式
fmt1 = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(message)s")
# 文件用格式
file_1.setFormatter(fmt1)
file_2 = logging.FileHandler("log2.log", "a")
fmt2 = logging.Formatter()
file_2.setFormatter(fmt2)
logger1 = logging.Logger("s1", level=logging.ERROR)
logger1.addHandler(file_1)
logger1.addHandler(file_2)
logger1.critical("1111")
# 定义文件
file_2_1 = logging.FileHandler('l2_1.log', 'a')
fmt = logging.Formatter()
file_2_1.setFormatter(fmt)
# 定义日志
logger2 = logging.Logger('s2', level=logging.INFO)
logger2.addHandler(file_2_1)

# 如上述创建的两个日志对象
# 当使用logger1写日志时，会将相应的内容写入 l1_1.log 和 l1_2.log 文件中
# 当使用logger2写日志时，会将相应的内容写入 l2_1.log 文件中