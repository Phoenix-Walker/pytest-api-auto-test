import logging
import os

def get_logger():
    # 创建logger实例
    logger = logging.getLogger("api_auto_test")
    logger.setLevel(logging.INFO)
    # 避免重复添加handler
    if not logger.handlers:如果不是日志记录器。处理程序：
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')格式化器 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # 控制台输出
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger

log = get_logger()日志 =获取日志记录器()
