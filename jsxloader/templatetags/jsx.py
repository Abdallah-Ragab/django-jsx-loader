from django import template
from ..nodes import JsxNode


register = template.Library()

@register.tag(name="jsx")
def do_jsx(parser, token):
    nodelist = parser.parse(("endjsx",))
    parser.delete_first_token()
    return JsxNode(nodelist)



# TODO : Configuration option to choose output location. default: /static/
# TODO: Add option in tag declaration for naming the JSX Component instead of using random.
