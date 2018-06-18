class Base(object):
   def test(self):
        print('---base test---')
class B(Base):
    def test(self):
        print('-A--test--')
class A(Base):
    def test(self):
         print('-B--test--')
class C(A,B):
    pass

obj_c=C()
obj_c.test()
print(C.__mro__)


