from multiply import mult

def test_case1(): 
    result = 10
    assert mult(5,2) == result
    

def test_case2():
    result = 1
    assert mult(0.2,5) == result
    
    
def test_case3():
    result = 12
    assert mult(4,3) == result