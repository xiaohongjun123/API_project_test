import logging
import os
import time

class mylog(object):
    def __init__(self,logger_name):
        self.logger=logging.getLogger(logger_name)#设置log日志入口
        self.logger.setLevel(logging.INFO)
        rq=time.strftime("%Y-%m-%d",time.localtime(time.time()))#获取本地时间并转化成相应的格式
        all_log_path=os.path.dirname(os.path.abspath(__file__))#获取当前文件的上层路径
        error_log_path=os.path.dirname(os.path.abspath(__file__))
        all_log_name=os.path.join(all_log_path,rq+".log")#将路径和文件名拼接形成文件存放最终路径
        error_log_name=os.path.join(error_log_path,rq+"error.log")

        fh=logging.FileHandler(all_log_name)#创建一个handle，输出路径为文件输出
        fh.setLevel(logging.DEBUG)#设置输出log等级
        eh=logging.FileHandler(error_log_name)
        eh.setLevel(logging.ERROR)
        ch=logging.StreamHandler()#创建一个handle，输出去路径为控制台输出
        ch.setLevel(logging.INFO)

        all_log_formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        error_log_formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(lineno)s-%(message)s")


        fh.setFormatter(all_log_formatter)#给handle添加输出格式
        ch.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)
        self.logger.addHandler(fh)#给入口添加handle
        self.logger.addHandler(ch)
        self.logger.addHandler(eh)

    def getlog(self):
        return self.logger
if __name__=="__main__":
    log=mylog("test_log").getlog()
    log.info("test")
    log.error("error")





