django-sendmail-backend
=======================

Its a simple command line sendmail backend for Django


# Motivation

I like to use **msmtp** to abstract the smtp server from my projects.
Because it is easy to set environment specifity mail server.


# Install

    pip install django_sendmail_backend


# Usage

Set the EMAIL_BACKEND var in your settings module

    EMAIL_BACKEND = 'django_sendmail_backend.backends.EmailBackend'

If your sendmail binary is not at /usr/sbin/sendmail (see MTA section below),
you'll also need to set

    SENDMAIL_BINARY = '/path/to/sendmail'


# MTA

You will need any mta installed (like postfix or exim) and a executable
**sendmail** command.

Try to install [msmtp](http://msmtp.sourceforge.net/) for test


## On Debian/Ubuntu

    sudo apt-get install msmtp-mta

