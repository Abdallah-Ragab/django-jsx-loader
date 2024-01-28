from django import template
from django.template import Context
from .jsx import JSXNode

class JSXFileComponentNode(JSXNode):
    def __init__(self, path, *args, **kwargs):
        super(JSXFileComponentNode, self).__init__(*args, **kwargs)
        self.path = path

    def render(self, context: Context) -> str:
        super(JSXFileComponentNode, self).render(context)
        print(f"From JSX File Component Node: {self.id}")
        return self.path
