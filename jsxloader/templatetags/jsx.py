from django import template
from ..nodes import JsxNode, JSXFileComponentNode, JSXInlineComponentNode, JSXSyntaxNode


register = template.Library()

@register.tag(name="JSX")
def do_jsx(parser, token):
    nodelist = parser.parse(("endJSX",))
    parser.delete_first_token()
    return JSXSyntaxNode(nodelist)

@register.tag(name='JSXComponentFile')
def do_jsx_component_file(parser, token):
    try:
        tag_name, path = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(f"{token.contents} tag requires a Component path.")

    # Ensure the path is properly quoted
    if not (path[0] == path[-1] and path[0] in ('"', "'")):
        raise template.TemplateSyntaxError(f"Component path must be enclosed in quotes: {path}")

    # Strip the quotes from the path
    path = path[1:-1]

    return JSXFileComponentNode(path)

@register.tag(name="JSXComponent")
def do_jsx_component(parser, token):
    nodelist = parser.parse(("endJSXComponent",))
    parser.delete_first_token()
    return JSXInlineComponentNode(nodelist)


# TODO: Add option in tag declaration for naming the JSX Component instead of using random.
