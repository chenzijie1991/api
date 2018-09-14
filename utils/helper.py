# encoding:utf-8

from django.http.response import HttpResponse
import json
import uuid

from datetime import date, datetime
from django.utils import timezone

local_tz = timezone.get_current_timezone()

def get_local_host(request):
    uri = request.build_absolute_uri()
    return uri[0:uri.find(request.path)]



def validate_form(form_class, data):
    form = form_class(data)
    if form.is_valid():
        return True, form.cleaned_data
    errors = []
    for key, field in form.declared_fields.items():
        if field.required and key not in data:
            errors.append({"field": key, "code": "missing_field"})
        elif key in form.errors:
            errors.append({"field": key, "code": "invalid"})
    return False, errors




class UUJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, uuid.UUID):
            return o.hex
        elif isinstance(o, datetime):
            return o.timestamp()
        return super(UUJSONEncoder, self).default(o)



class HttpJsonResponse(HttpResponse):
    def __init__(self, data=None, encoder=None, *args, **kwargs):
        kwargs.setdefault('content_type', 'application/json; charset=utf-8')
        kwargs.setdefault('status', 200)
        encoder = encoder if encoder else UUJSONEncoder
        data = json.dumps(data, cls=encoder) if data is not None else ''
        super(HttpJsonResponse, self).__init__(content=data, *args, **kwargs)


def datetime_to_timestamp(dt):
    if dt is None:
        return None
    if isinstance(dt, datetime):
        dt = datetime.strptime(str(dt), '%Y-%m-%d')
        dt.replace(tzinfo=local_tz)
    elif isinstance(dt, date):
        pass
    return 111

