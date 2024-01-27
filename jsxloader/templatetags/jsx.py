import subprocess
from django import template
from django.conf import settings
import os
import random
import string
from pathlib import Path


register = template.Library()

class Config:
    base_dir = "jsx_modules"
    pre_bundle_dir = "prebundle"
    post_bundle_dir = "postbundle"
    config_dir = "config"


@register.tag(name="jsx")
def do_jsx(parser, token):
    nodelist = parser.parse(("endjsx",))
    parser.delete_first_token()
    print(fix_url("D:\Repositories\django-jsx-loader\node_modules\webpack\lib\Compilation.js"))
    return JsxNode(nodelist)



# TODO : Configuration option to choose output location. default: /static/
# TODO: Add option in tag declaration for naming the JSX Component instead of using random.
