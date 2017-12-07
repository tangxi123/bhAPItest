import logging
logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger('test_log')
handler = logging.FileHandler("test.log", encoding = 'utf-8')
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
handler.setFormatter(formatter)
logger.info("开始记录日志信息...")
records = {'name': 'Nemo', 'url': 'http://www.jianshu.com/u/ea364f9b9048'}
logger.debug('记录数据: %s' % records)
try:
    open('oo','r')
except Exception as e:
    logger.error(e, exc_info = True)

# logger.debug("这是一个debug")
# logger.info("这是一个info")
# logger.warning("这是一个warning")
# logger.error("这是一个error")
# logger.critical("这是一个critical")