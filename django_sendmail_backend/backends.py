# -*- coding: utf-8 -*-

from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend
from subprocess import Popen, PIPE


class EmailBackend(ConsoleEmailBackend):

    def send_messages(self, email_messages):
        recipient_email = email_messages[0].to[0]
        mail_command = Popen("/usr/sbin/sendmail %s" % recipient_email, stdin=PIPE, shell=True)
        self.stream = mail_command.stdin

        super(EmailBackend, self).send_messages(email_messages)

        mail_command.communicate()
