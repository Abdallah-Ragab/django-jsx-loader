from django import template
from django.template import Context
from ..utils import hash_string

class JSXScriptNode(template.Node):
    def render(self, context: Context) -> str:
        self.template_id = self.get_template_id(context.template.origin.name)
        context["jsx_loader"] = {}
        context["jsx_loader"]["_counter"] = 0
        return ""

    def get_template_id(self, template_path):
        return hash_string(template_path)[:6]