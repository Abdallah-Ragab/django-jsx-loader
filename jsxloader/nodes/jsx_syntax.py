from django import template
from django.template import Context

class JSXSyntaxNode(template.Node):

    def __init__(self, nodelist, *args, **kwargs):
        super(JSXSyntaxNode, self).__init__(*args, **kwargs)
        self.nodelist = nodelist

    def render(self, context: Context) -> str:
        print(f"From JSX Syntax Node: {context.template.name}")
        return self.nodelist.render(context)