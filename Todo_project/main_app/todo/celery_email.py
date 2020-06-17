import logging
import smtplib

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'Hunter.Alex@mail.ru'
EMAIL_HOST_PASSWORD = 'qwerty123'
EMAIL_USE_TLS = True  # TLS settings


class Mailer:
    """
     Send email messages helper class
    """

    def __init__(self, from_email=None):
        # TODO setup the default from email

        server = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
        server.ehlo()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        self.server = server

    def send_email(self, recipient, subject, body):
        FROM = EMAIL_HOST_USER
        TO = recipient if isinstance(recipient, list) else [recipient]
        SUBJECT = subject
        TEXT = body

        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        self.server.sendmail(FROM, TO, message)
        logging.info('Succesful sending')

    def close(self):
        self.server.close()
