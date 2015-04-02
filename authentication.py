# -*- coding: utf-8 -*-
from flask import session, redirect, url_for
from functools import wraps

DEFAULT_CALLBACK_URL = 'login'
DEFAULT_CALLBACK_PERMISSIONS_URL = 'erro_funcao'


class RequiresAuthentication(object):
    def __init__(self, permissions=None, callback_permissions=DEFAULT_CALLBACK_PERMISSIONS_URL, callback=DEFAULT_CALLBACK_URL):
        self.permissions = permissions
        self.callback = callback
        self.callback_permissions = callback_permissions

    def __call__(self, f):
        @wraps(f)
        def authentication_decorated(*args, **kwargs):
            if is_authenticated():
                if self.require_special_permissions():
                    if session['funcao'] in self.permissions:
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


def is_authenticated():
    return 'username' in session

