from django import template
from django.template import Context
from ..utils import hash_string

class JSXScriptNode(template.Node):
    def render(self, context: Context) -> str:
        print(context.template_name)
        print(context.template.name)
        print(context.template.origin)
        print(context.template.origin.name)
        print(context.template.origin.template_name)

        return "script"