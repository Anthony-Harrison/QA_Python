import pytest
import Modules as m
def test_ans1():
    assert m.blah() == 3.4641016151377544
    
def test_ans2():
    assert m.hmm(6) == 66
    
def test_ans3():
    assert m.hmm(123) == "Noooo"