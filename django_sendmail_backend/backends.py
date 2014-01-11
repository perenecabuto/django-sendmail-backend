# -*- coding: utf-8 -*-

from django.core.mail.backends.console import EmailBackend as ConsoleEmailBackend
from subprocess import Popen, PIPE


class EmailBackend(ConsoleEmailBackend):

    def send_messages(self, email_messages):
        # -t: Read message for recipients
        mail_command = Popen(['/usr/sbin/sendmail', '-t'], stdin=PIPE, stderr=PIPE)
        self.stream = mail_command.stdin

        super(EmailBackend, self).send_messages(email_messages)

        (stdout, stderr) = mail_command.communicate()

        if mail_command.returncode:
            raise Exception('send_messages failed: %s' % (stderr if stderr else stdout,))
