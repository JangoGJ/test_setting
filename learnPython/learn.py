import hashlib


class User(object):
    def __init__(self,username,password):
        self.username=username
        self.password=self._encrypt_pw(password)
        self.is_logged_in=False


    def _encrypt_pw(self, password):
        hash_string=(self.username+password)
        hash_string=hash_string.encode("utf8")
        return hashlib.sha512(hash_string).hexdigest()


    def check_password(self, password):
        encrypted=self._encrypt_pw(password)
        return encrypted==self.password


class AuthException(Exception):
    def __init__(self,username,user=None):
        super().__init__(username,user)
        self.username=username
        self.user=user


class usernameAlreadyExist(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class Authenticator(object):
    def __init__(self):
        self.users={}


    def add_user(self,username,password):
        if username in self.users:
            raise usernameAlreadyExist(username)
        if len(password)<6:
            raise PasswordTooShort(username)
        self.users[username]=User(username,password)


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


def login(self,username,password):
    try:
        user=self.users[username]
    except KeyError:
        raise InvalidUsername(username)
    if not user.check_password(password):
        raise InvalidPassword(username,user)
    user.is_logged_in=True
    return True


def is_logged_in(self,username):
    if username in self.users:
        return self.users[username].is_logged_in
    return False


authenticator=Authenticator()


class Authorizor(object):
    def __init__(self,authenticator):
        self.authenticator=authenticator
        self.permissions={}
    

    def add_permission(self,permission_name):
        try:
            permission_set=self.permissions[permission_name]
        except KeyError:
            self.permissions[permission_name]=set()
        else:
            raise PermissionError("Permission Exists")
        

    def permit_user(self,permission_name,username):
        try:
            permission_set=self.permissions[permission_name]
        except KeyError:
            raise PermissionError("Permission is not exist.")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            permission_set.add(username)
        

class PermissionError(Exception):
    pass


def check_permission(self,permission_name,username):
    if not self.authenticator.is_logged_in(username):
        raise NotLoggedInError(username)
    try:
        permission_set=self.permissions[permission_name]
    except KeyError:
        raise PermissionError("Permission is not exist.")
    else:
        if username not in permission_set:
            raise NotPermittedError(username)
        else:
            return True
class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass


authorizor=Authorizor(authenticator)


import auth
auth.authenticator.add_user("joe", "joepassword")
auth.authorizor.add_permission("paint")
auth.authorizor.check_permission("paint", "joe")