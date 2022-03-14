import functools

from django import template

register = template.Library()


@register.tag
def prepare_attrs(parser, token):
    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError(
            "prepare_attrs tag takes at least 1 argument")

    if 'as' not in args:
        raise template.TemplateSyntaxError("add 'as' to get data")

    return PrepareAttrsNode(args[1:-2], args[-1])


class PrepareAttrsNode(template.Node):

    def prepare_args(self, context):
        result = []
        for attr in self.args:
            pos = attr.find('=')
            name = attr[pos+1:]
            variable = template.Variable(name)
            result.append('{}:{}'.format(name, variable.resolve(context)))

        self.args = result

    def __init__(self, args, c_varname):
        self.args, self.c_varname = args, c_varname

    def render(self, context):
        self.prepare_args(context)
        context[self.c_varname] = functools.reduce(lambda result, attr_val: result + attr_val + ' ', [''] + self.args)
        return ''


@register.tag
def annotate_form_field(parser, token):
    """
    Set an attribute on a form field with the widget type

    This means templates can use the widget type to render things differently
    if they want to.  Django doesn't make this available by default.
    """
    args = token.split_contents()
    if len(args) < 2:
        raise template.TemplateSyntaxError(
            "annotate_form_field tag requires a form field to be passed")
    return FormFieldNode(args[1])


class FormFieldNode(template.Node):
    def __init__(self, field_str):
        self.field = template.Variable(field_str)

    def render(self, context):
        field = self.field.resolve(context)
        if hasattr(field, 'field'):
            field.widget_type = field.field.widget.__class__.__name__
        return ''
