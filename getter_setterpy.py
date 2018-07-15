class Silly(object):
    def _get_silly(self):
        print("You are getting silly.")
        return self._silly
    def _set_silly(self,value):
        print("You are making silly {}".format(value))
        self._silly=value
    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly
    silly=property(_get_silly,_set_silly,_del_silly,"This is silly property.")

s=Silly()
s.silly='funny'
s.silly
del s.silly


class Foo(object):
    @property
    def foo(self):
        "This is a foo property."
        print("You are getting foo.")
        return self._foo
    

    @foo.setter
    def foo(self,value):
        print("You are making foo {}".format(value))
        self._foo=value
    

    @foo.deleter
    def foo(self):
        print("Whoah, you killed foo!")
        del self._foo


f=Foo()
f.foo='foolish'
f.foo
del f.foo