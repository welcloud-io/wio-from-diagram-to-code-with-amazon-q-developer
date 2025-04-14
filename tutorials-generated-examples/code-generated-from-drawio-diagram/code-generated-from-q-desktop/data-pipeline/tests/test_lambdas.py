import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lambda.lambda1.app import handler as handler1
from lambda.lambda2.app import handler as handler2
from lambda.lambda3.app import handler as handler3

def test_lambda1():
    result = handler1({}, {})
    assert result['statusCode'] == 200
    assert result['body']['result'] == 2  # 1 + 1

def test_lambda2():
    result = handler2({}, {})
    assert result['statusCode'] == 200
    assert result['body']['result'] == 4  # 2 + 2

def test_lambda3():
    result = handler3({}, {})
    assert result['statusCode'] == 200
    assert result['body']['result'] == 6  # 3 + 3