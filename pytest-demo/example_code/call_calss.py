from example_code.demo_class import DemoClass
class CallClass:
    def func1(self):
        return DemoClass.name()

    def func2(self):
        return DemoClass.get_class_name()

    def func3(self):
        return DemoClass.get_instance().hello("sam")