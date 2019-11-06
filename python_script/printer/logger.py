import logging
from logging import handlers
# reference: https://www.cnblogs.com/nancyzhu/p/8551506.html


experiment_id = 1

class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename, level='info', when='D', backCount=3, format='%(asctime)s %(levelname)s:%(message)s', datefmt="%Y-%M-%d %H:%M:%S"):
        # more detailed format: '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(format, datefmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount, encoding='utf-8')  # 往文件里写入
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)

logger = Logger('out_{}.log'.format(experiment_id), level='info').logger

logger.info('xxx')
