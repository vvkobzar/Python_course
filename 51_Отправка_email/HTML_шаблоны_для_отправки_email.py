# Быстро создать HTML документ - открывает документ с .html - ! + TAB
from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

my_email = EmailMessage()

html_tamplate = Template(
    Path("51_Отправка_email/templates/index.html").read_text())
html_content = html_tamplate.substitute({'name': 'Vlad', 'date': 'tomorrow'})
# Метод substitute() заменяет переменные в html файле, которые начинаются с $

my_email['from'] = 'Vladislav'
my_email['to'] = 'friend@gmail.com'
my_email['subject'] = "Let's go out"
my_email.set_content(html_content, 'html')
# Если не указывать 'html', то отправится текст

with smtplib.SMTP(host='79.137.205.83', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent!")
