# 系统自带日志
import logging

logging.basicConfig(filename='xxx.log',
                    format='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=10)
logging.debug('X1测试环境')  # 10         #测试环境
logging.info('X2正常信息')  # 20         #正常信息
logging.warning('X3警告信息')  # 30         #警告信息
logging.error('X4错误信息')  # 40         #错误信息
logging.critical('X5严重错误')  # 50         #严重错误
logging.log(10, 'X6自定义')  # 自定义

# 2020-02-20 22:02:09-root-DEBUG-logging_module:X1
# 2020-02-20 22:02:09-root-INFO-logging_module:X2
# 2020-02-20 22:02:09-root-WARNING-logging_module:X3
# 2020-02-20 22:02:09-root-ERROR-logging_module:X4
# 2020-02-20 22:02:09-root-CRITICAL-logging_module:X5
# 2020-02-20 22:02:09-root-DEBUG-logging_module:X6
# 时间                用户 等级  运行模块      信息

# 自定义日志
import logging

log_file = logging.FileHandler('xx1.log', mode='a', encoding='utf-8')  # 创建一个对象
log_file.setFormatter(logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s'))  # 定义格式
log_1 = logging.Logger('root', level=logging.ERROR)  # 定义用户和错误级别
log_1.addHandler(log_file)  # 写入错误
log_1.error('未知错误')  # 错误备注
