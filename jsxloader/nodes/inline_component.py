from django import template
from django.template import Context


class JSXInlineComponentNode(template.Node):
    def __init__(self, nodelist, *args, **kwargs):
        super(JSXInlineComponentNode, self).__init__(*args, **kwargs)
        self.nodelist = nodelist

    def render(self, context: Context) -> str:
        print(f"From JSX Inline Component Node: {context.template.name}")
        return self.nodelist.render(context)
