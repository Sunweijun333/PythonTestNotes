class Test(object):
    num_of_instance = 0
    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1

if __name__ == '__main__':
    print(Test.num_of_instance)
    t1 = Test('jack')
    print(Test.num_of_instance)
    t2 =Test('lucy')
    print(t1.name , t1.num_of_instance)
    print(t2.name , t2.num_of_instance) 
    print(Test('jacy').num_of_instance)
