class DemoClass:
    @staticmethod
    def name():
        return 'demo'

    @classmethod
    def get_class_name(cls):
        return 'demo'

    @classmethod
    def get_instance(cls):
        return cls()

    def hello(self, name):
        return 'hello ' + name
