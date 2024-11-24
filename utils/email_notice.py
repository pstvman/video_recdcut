import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

def send_email(subject, body, to_email):
    # 邮件服务器配置
    smtp_server = os.getenv("SMTP_ADDRESS")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_user = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    # 添加邮件内容
    msg.attach(MIMEText(body, 'plain'))

    server = None  # 初始化 server 变量
    try:
        # 连接到邮件服务器
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 启用TLS
        server.login(smtp_user, smtp_password)
        
        # 发送邮件
        server.sendmail(smtp_user, to_email, msg.as_string())
        print(f"邮件已成功投递至 {to_email}")
    except Exception as e:
        print(f"邮件投递失败: {e}")
    finally:
        # 关闭服务器连接
        if server is not None:
            try:
                server.quit()
            except Exception as e:
                print(f"关闭连接时发生错误: {e}")


email_subject = "状态通知(测试邮件)"
email_body = "This is a test email, you can just ignore it. \n\n\nthanks."
to_email = os.getenv("TO_MAIL_ADDRESS")
# 调用函数发送邮件
send_email(email_subject, email_body, to_email)
