from django.template.backends.django import DjangoTemplates, Template, reraise
from django.template import TemplateDoesNotExist


class JSXLoaderEngine(DjangoTemplates):
    def from_string(self, template_code):
        return JSXSupportedTemplate(self.engine.from_string(template_code), self)

    def get_template(self, template_name):
        try:
            return JSXSupportedTemplate(self.engine.get_template(template_name), self)
        except TemplateDoesNotExist as exc:
            reraise(exc, self)


class JSXSupportedTemplate(Template):
    def render(self, context=None, request=None):
        result = super(JSXSupportedTemplate).render(self, context, request)
        # build jsx scripts
        return result
