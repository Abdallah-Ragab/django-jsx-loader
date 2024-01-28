from django import template
from django.template import Context
from .jsx import JSXNode
from ..utils import clean_js_variable_name, hash_string

class JSXSyntaxNode(JSXNode):

    def __init__(self, nodelist, *args, **kwargs):
        super(JSXSyntaxNode, self).__init__(*args, **kwargs)
        self.nodelist = nodelist

    def generate_component_id(self, template_name, jsx):
        pass


    def wrap_jsx_in_component(self) -> str:
        # component_name = clean_js_variable_name(hash_string())
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
        super(JSXSyntaxNode, self).render(context)
        print(f"From JSX Syntax Node: {self.get_index()}")

        self.jsx = self.nodelist.render(context)
        return self.wrap_jsx_in_component()
