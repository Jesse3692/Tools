import pytest


@pytest.fixture  # 创建测试环境，可以用来做setUP和tearDown的工作
def setup_math():
    import math
    return math


@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print('teardown_function called')
    request.addfinalizer(teardown_function)  # 这个内嵌的函数做tearDown工作
    print('setup_function called.')

def test_func(setup_function):
    print('Test_func called.')

def test_setup_math(setup_math):
    # pytest中直接使用断言语句
    assert setup_math.pow(2, 3) == 8.0

class TestClass(object):
    def test_in(self):
        assert 'h' in 'hello'

    def test_two(self, setup_math):
        assert setup_math.ceil(10) == 10.0

def raise_exit():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):  # 用来测试抛出的异常
        raise_exit()

@pytest.mark.parametrize(
    'test_input, expected',
    [
        ('1+3', 4),
        ('2*4', 8),
        ('1 == 2', False),
    ]
)  # parametrize可以使用装饰器的方式集成多组测试样例
def test_eval(test_input, expected):
    assert eval(test_input)  == expected
