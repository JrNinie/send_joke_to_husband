# send eamil to my husband
import yagmail
import settings

def send_mail(sender_account, sender_password, sender_host, mail_recipient, subject, contents):

    # Initializing the yagmail instance
    yag = yagmail.SMTP(user=sender_account, password=sender_password, host=sender_host)
    # Sending the email
    yag.send(to=mail_recipient, subject=subject, contents=contents)


RECIPIENT_ACCOUNT="xxx@gmail.com"
SUBJECT="Great news"
CONTENTS="You're the winner"

send_mail(settings.SENDER_ACCOUNT, settings.SENDER_PASSWORD, settings.SENDER_HOST, RECIPIENT_ACCOUNT, SUBJECT, CONTENTS)