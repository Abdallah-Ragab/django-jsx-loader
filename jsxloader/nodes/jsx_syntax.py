from django import template
from django.template import Context
from ..utils import clean_js_variable_name

class JSXSyntaxNode(template.Node):

    def __init__(self, nodelist, *args, **kwargs):
        super(JSXSyntaxNode, self).__init__(*args, **kwargs)
        self.nodelist = nodelist


    def wrap_jsx_in_component(self) -> str:
        # component_name = clean_js_variable_name(component_name)
        component_name = ""

        return """
        import React from 'react';
        import ReactDOM from 'react-dom';

        const """ + component_name + """ = () => {
            return (
                """ + self.jsx + """
            );
        }
        """

    def render(self, context: Context) -> str:
        print(f"From JSX Syntax Node: {context.template.name}")
        self.jsx = self.nodelist.render(context)
        self.wrap_jsx_in_component()