from django import template
from django.template import Context


class JSXFileComponentNode(template.Node):
    def __init__(self, path, *args, **kwargs):
        super(JSXFileComponentNode, self).__init__(*args, **kwargs)
        self.path = path

    def render(self, context: Context) -> str:
        print(f"From JSX File Component Node: {context.template.name}")
        return self.path
