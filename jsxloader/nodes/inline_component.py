from django import template
from django.template import Context
from .jsx import JSXNode


class JSXInlineComponentNode(JSXNode):
    def __init__(self, nodelist, *args, **kwargs):
        super(JSXInlineComponentNode, self).__init__(*args, **kwargs)
        self.nodelist = nodelist

    def render(self, context: Context) -> str:
        super(JSXInlineComponentNode, self).render(context)
        print(f"From JSX Inline Component Node: {self.get_index()}")
        return self.nodelist.render(context)
