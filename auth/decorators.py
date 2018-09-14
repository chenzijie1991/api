# encoding:utf-8

import json
from django.http.response import HttpResponseForbidden


def login_required():
    def _login_required(view):
        def __decorator(self, request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden(json.dumps({
                    "message": "Authorization failed"}))
            return view(self, request, *args, **kwargs)
        return __decorator
    return _login_required
