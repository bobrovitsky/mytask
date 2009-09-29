''' admin_edit templatetag '''
from django import template
register = template.Library()


@register.inclusion_tag('admin_edit.html', takes_context=True)
def admin_edit(context, obj):
    ''' return link to admin edit '''
    return {
        'app': obj._meta.app_label,
        'module': obj._meta.module_name,
        'pk': obj.pk,
    }
