import nose
from temperature import *

def test_above_freezing():
    assert above_freezing(89.4)
    assert  not above_freezing(-43)
    assert not above_freezing(0)


#在终端输入
#$nosetest -v test_freezing.py
