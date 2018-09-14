# -*- encoding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from auth.forms import LoginForm
from utils.helper import validate_form, HttpJsonResponse

class LoginView(View):
    def get(self, request):
        """登录"""
        is_valid, data = validate_form(LoginForm, request.GET)
        if not is_valid:
            return HttpJsonResponse({
                'message': '',
                'errors': data
            }, status=422)

        user = authenticate(**data)
        if user is not None and user.is_active:
            login(request, user)
            return HttpJsonResponse({ "username" : data['username']} , status=204)
        else:
            return HttpJsonResponse(status=403)


class LogoutView(View):
    def get(self, request):
        """退出登录"""
        logout(request)
        return HttpJsonResponse(status=204)
