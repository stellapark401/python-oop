a = list()
b = tuple()
c = dict()
d = set()
print(type(a), type(b), type(c), type(d))
lst1 = ['python', 'anaconda', 'c++', 'java']
lst2 = ['c', 'c++', 'pycharm', 'pythone']
s = set(lst1)
print(s)
s1 = set(lst1)
s2 = set(lst2)
if (s1 - s2) == (s1 | s2) - s2:
    print('it does compute right.')
print(s1 - s2)
print(s1 | s2)
print((s1 | s2) & s1)
st = {1, 2, 3, 4}
print(type(st))
print(id(s2), id(b))
lst1[1] = 'Big snake'
print(s1)
print(s)

class foo:
    a = 0

    def instance_method(self):
        self.b = 10
        print("instance method called")

    @classmethod
    def class_method(cls):
        print("class method called")
        cls.a += 1
        return cls.a

    @staticmethod
    def static_method():
        print("static method called")


f = foo()
f.instance_method()
f.class_method()
f.class_method()
f.class_method()
f.class_method()
f.static_method()
print(f.a)
print(foo.a)
