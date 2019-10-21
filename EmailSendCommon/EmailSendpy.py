import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time
import os
from LogCommon import LogCommonpy
class EmailSend(object):
    def __init__(self,recipients):
        self.recipients=recipients
    def Send(self):
        mail_host="smtp.qq.com"
        mai_username="879337649@qq.com"
        mail_passwd="iozcnjjudirxbfba"
        mail_sender="879337649@qq.com"

        message=MIMEMultipart()
        message["From"]=Header("tester","utf-8")
        message["To"]=Header("leader","utf-8")
        ti=time.strftime("%Y-%m-%d",time.localtime())
        subject=str(ti)+"日自动化测试结果"
        message["Subject"]=Header(subject,"utf-8")
        message.attach(MIMEText("本轮接口测试测试结果","plain","utf-8"))
        if os.path.exists(r"E:\apk\app_1.0_1_201907241956.apk")==True:
            att1=MIMEText(open((r"E:\apk\app_1.0_1_201907241956.apk"),"rb").read(),"base64","utf-8")
            att1["Content-Type"]="application/octet-stream"
            att1["Content-Disposition"]="attachment;filename='test.apk'"
            message.attach(att1)
        else:
            time.sleep(3)
            att1 = MIMEText(open((r"E:\apk\app_1.0_1_201907241956.apk"),"rb").read(),"base64","utf-8")
            att1["Content-Type"] = "application/octet-stream"
            att1["Content-Disposition"] = "attachment;filename='test.apk'"
            message.attach(att1)
        try:
            smtpobj=smtplib.SMTP_SSL(mail_host,465)
            #       smtpobj.set_debuglevel(1)
            smtpobj.login(mai_username,mail_passwd)
            smtpobj.sendmail(mail_sender,self.recipients,message.as_string())
            print("发送成功")
        except smtplib.SMTPException as e:
            print(e)
if __name__=="__main__":
    sd=EmailSend("979669145@qq.com")
    sd.Send()
