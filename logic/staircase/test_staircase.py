from routine import StairCase

def test_down():
    staircase = StairCase(100, 3, 1, 13, lambda x: x - 10, lambda x: x + 10)
    for _ in range(2):
        staircase.correct()
        assert staircase.current == 100
    staircase.correct()
    assert staircase.current == 90
    
def test_up():
    staircase = StairCase(100, 3, 1, 13, lambda x: x - 10, lambda x: x + 10)
    staircase.wrong()
    assert staircase.current == 110
    staircase.wrong()
    assert staircase.current == 120

def test_combine():
    staircase = StairCase(100, 3, 1, 13, lambda x: x - 10, lambda x: x + 10)
    for _ in range(2):
        staircase.correct()
        assert staircase.current == 100
    staircase.wrong()
    assert staircase.current == 110
    assert len(staircase.turning_points) == 0
    for _ in range(2):
        staircase.wrong()
    staircase.current = 130
    assert len(staircase.turning_points) == 0
    staircase.correct()
    assert staircase.current == 130
    staircase.correct()
    assert staircase.current == 130
    assert len(staircase.turning_points) == 0
    staircase.correct()
    assert staircase.current == 120
    assert len(staircase.turning_points) == 1

if __name__ == "__main__":
    test_down()
    test_up()
    test_combine()