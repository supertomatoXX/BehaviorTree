# -*- coding: utf-8 -*

class Test(object):
    def __init__(self):
        self.y = 10


    def __getattr__(self, name):
        print('__getattr__')


    def __setattr__(self, name, value):
        print('__setattr__')
        self.__dict__[name]=value

    #def __delattr__(self, name):
    #    print('__delattr__')



class TestSub(Test):
    def __init__(self):
        self.sub_y = 10

if __name__ == "__main__":
    t=Test()
    ts = TestSub()

    print("111111111")
    print(Test.__dict__)
    print(TestSub.__dict__)

    setattr(t, "x", 10)
    setattr(ts, "sub_x", 10)
    setattr(t, "y", 5)
    setattr(ts, "sub_y", 5)

    print("222222222")
    print(t.__dict__)
    print(ts.__dict__)

    print("333333333")
    print(t.y, t.x)
    print(ts.sub_y, ts.sub_x)

    #delattr(t, "x") 
    #delattr(t, "y")
    #delattr(ts, "sub_x")
    #delattr(ts, "sub_y")

    print("444444444444")
    print(t.x, t.y)
    print(ts.sub_x, ts.sub_y)

    print("55555555555")
    print(t.__dict__)
    print(ts.__dict__)

    print("66666666666")
    getattr(t, "x") 
    getattr(t, "y")
    getattr(ts, "sub_x")
    getattr(ts, "sub_y")
