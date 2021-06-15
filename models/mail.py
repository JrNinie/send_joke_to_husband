import yagmail
import settings


class Mail:
    def send_mail(self,
                  contents=None,
                  sender_mail=settings.SENDER_MAIL,
                  sender_password=settings.SENDER_PASSWORD,
                  sender_host=settings.SENDER_HOST,
                  receiver_mail=settings.RECEIVER_MAIL,
                  subject=settings.SUBJECT):
        """Send mail

        Parameters
        ----------
        sender_mail : string
            Email of sender
        sender_password : string
            Password of sender's mail
        sender_host : string
            Host of sender's mail provider
        receiver_mail : string
            Email of receiver
        subject : string
            Subject of mail
        content : string
            Content of mail
        """

        # Initializing the yagmail instance
        yag = yagmail.SMTP(user=sender_mail,
                           password=sender_password,
                           host=sender_host)
        # Sending the email
        yag.send(to=receiver_mail, subject=subject, contents=contents)