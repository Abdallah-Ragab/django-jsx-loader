from django.template.backends.django import DjangoTemplates, reraise
from django.template.context import make_context
from django.template import TemplateDoesNotExist


class JSXLoaderEngine(DjangoTemplates):
    def from_string(self, template_code):
        return JSXSupportedTemplate(self.engine.from_string(template_code), self)

    def get_template(self, template_name):
        try:
            return JSXSupportedTemplate(self.engine.get_template(template_name), self)
        except TemplateDoesNotExist as exc:
            reraise(exc, self)


class JSXSupportedTemplate:
    def __init__(self, template, backend):
        self.template = template
        self.backend = backend

    @property
    def origin(self):
        return self.template.origin

    def render(self, context=None, request=None):
        context = make_context(
            context, request, autoescape=self.backend.engine.autoescape
        )
        try:
            return self.template.render(context)
        except TemplateDoesNotExist as exc:
            reraise(exc, self.backend)