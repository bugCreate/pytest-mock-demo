import pytest
from example_code.call_calss import CallClass
from example_code.demo_class import DemoClass


class TestClassMock:

    @pytest.fixture(scope='function')
    def monkeypatch(self):
        return pytest.MonkeyPatch()

    def test_class_mock(self, monkeypatch):
        c = CallClass()
        result1 = c.func1()
        result2 = c.func2()
        result3 = c.func3()
        assert result1 == 'demo'
        assert result2 == 'demo'
        assert result3 == 'hello sam'
        excepted_name = 'sam'

        def mock_name():
            return excepted_name

        monkeypatch.setattr(DemoClass, 'name', mock_name)
        result1 = c.func1()
        c2 = CallClass()
        result2 = c2.func1()
        assert result1 == 'sam'
        assert result2 == 'sam'

        monkeypatch.setattr(DemoClass, 'get_class_name', mock_name)
        result1 = c.func2()
        c2 = CallClass()
        result2 = c2.func2()
        assert result1 == 'sam'
        assert result2 == 'sam'

        def hi(self,name):
            return 'hi '+name

        monkeypatch.setattr(DemoClass, 'hello', hi)
        result1 = c.func3()
        c2 = CallClass()
        result2 = c2.func3()
        assert result1 == 'hi sam'
        assert result2 == 'hi sam'