# -*- coding: utf-8 -*-
from flask import session, redirect, url_for
from functools import wraps

CALLBACK_METHOD_NAME = 'login'
CALLBACK_PERMISSIONS_METHOD_NAME = 'erro_funcao'
AUTHENTICATED_FUNCTION = True
CURRENT_PERMISSION_FUNCTION = []


class RequiresAuthentication(object):
    def __init__(self, required_permissions=None, callback_permissions=CALLBACK_PERMISSIONS_METHOD_NAME, callback=CALLBACK_METHOD_NAME, authenticated=AUTHENTICATED_FUNCTION, permission=CURRENT_PERMISSION_FUNCTION):
        self.required_permissions = required_permissions
        self.permission = permission
        self.callback = callback
        self.callback_permissions = callback_permissions
        self.authenticated = authenticated

    def __call__(self, f):
        @wraps(f)
        def authentication_decorated(*args, **kwargs):
            if self.authenticated:
                if self.require_special_permissions():
                    if self.permission in self.required_permissions:
                        return f(*args, **kwargs)
                    else:
                        return redirect(url_for(self.callback_permissions))
                else:
                    return f(*args, **kwargs)
            else:
                return redirect(url_for(self.callback))

        return authentication_decorated

    def require_special_permissions(self):
        return self.permissions is not None and self.callback_permissions is not None




