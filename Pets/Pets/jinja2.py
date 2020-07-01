from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment, FileSystemLoader


def environment(**options):
    env = Environment(loader=FileSystemLoader('p_library/templates/p_library'))
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env