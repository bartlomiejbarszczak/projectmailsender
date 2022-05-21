from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from src.htmlstructure import htmltext
import os


def message(subject="Notification", text="", img=None, attachment=None):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg.attach(MIMEText(htmltext(text), 'html'))

    if img is not None:
        if type(img) is not list:
            img = [img]

        for one_img in img:
            img_data = open(one_img, 'rb').read()
            msg.attach(MIMEImage(img_data, name=os.path.basename(one_img)))

    if attachment is not None:
        if type(attachment) is not list:
            attachment = [attachment]

        for one_attachment in attachment:
            with open(one_attachment, 'rb') as f:
                file = MIMEApplication(f.read(), name=os.path.basename(one_attachment))
            file['Content-Disposition'] = f'attachment; filename="{os.path.basename(one_attachment)}"'
            msg.attach(file)

    return msg
