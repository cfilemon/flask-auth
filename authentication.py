from flask import session, redirect, url_for


class requires_authentication(object):

    def __init__(self, permissions=None, callback_permissions=None, callback='index'):
        self.permissions = permissions
        self.callback = callback
        self.callback_permissions = callback_permissions

    def __call__(self, f):
        def wrapped_f():
            if self.is_authenticated():
                if self.require_permissions() and session.funcao in self.permissions:
                    print "pode entrar, tem a permissao"
                    #return redirect(url_for(self.callback_permissions))
                    return f
                else:
                    print "requer permissao mas o usuario nao a tem"
                    return f
            else:
                print "requer que esteja logado e nao esta"
                #return redirect(url_for(self.callback))
                return f

        return wrapped_f

    def is_authenticated(self):
        return 'username' in session

    def require_permissions(self):
        return self.permissions is not None and self.callback_permissions is not None
