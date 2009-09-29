''' decorators '''
from django.shortcuts import render_to_response
from django.template import RequestContext

def render_to(tmpl):
    ''' render template with context decorator '''
    def renderer(func):
        ''' return wrapper '''
        def wrapper(request, *args, **kw):
            ''' wrapper to render_to_response '''
            output = func(request, *args, **kw)
            if not isinstance(output, dict):
                return output
            return render_to_response(tmpl, output,
                context_instance=RequestContext(request))
        return wrapper
    return renderer