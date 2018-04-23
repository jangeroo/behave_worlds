from behave.formatter.base import Formatter


class NotAFormatter(object):
    pass


class SuperFormatter(Formatter):
    name = "super"
    description = "Super-duper formatter."
