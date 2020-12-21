import example_code.ye_func
import pytest

# monkeypatch = pytest.MonkeyPatch()



class TestMock:
    # def __init__(self):
    #     self.

    @pytest.fixture(scope='function')
    def monkeypatch(self):
        return pytest.MonkeyPatch()

    def test_mock_ye(self,monkeypatch):
        excepted = 'i am mock func'

        def mock_func_no_param():
            return excepted

        monkeypatch.setattr(example_code.ye_func, 'no_param', mock_func_no_param)
        result = example_code.ye_func.no_param()
        assert result == excepted

        excepted2 = 'hi sam'
        def mock_func_with_param(name):
            return 'hi '+name

        monkeypatch.setattr(example_code.ye_func, 'with_param', mock_func_with_param)
        result = example_code.ye_func.with_param('sam')
        assert result == excepted2