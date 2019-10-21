import HTMLTestRunner_PY3
import unittest
import os
import time
from EmailSendCommon import EmailSendpy
email=EmailSendpy.EmailSend("979669145@qq.com")
case_path=r"G:\API_project_test\ApiTestCase"
if __name__=="__main__":
    discover=unittest.defaultTestLoader.discover(case_path,pattern="*case.py")
    suite=unittest.TestSuite()
    suite.addTest(discover)
    report_dir=r"G:\API_project_test\TestReport"
    report_name=os.path.join(report_dir,time.strftime("%Y-%m-%d",time.localtime())+"日测试结果.html")
    report=open(report_name,"wb")
    runner=HTMLTestRunner_PY3.HTMLTestRunner(stream=report,title="接口自动化测试报告",description="xxx项目接口测试结果:")
    runner.run(suite)
    report.close()
    email.Send()
