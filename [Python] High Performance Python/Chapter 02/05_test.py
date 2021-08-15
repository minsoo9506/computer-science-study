import time

def test_some_fn():
    """Check basic behaviours for our function"""
    assert some_fn(2) == 4
    assert some_fn(1) == 1
    assert some_fn(-1) == 1

# 아래에서 @profile를 사용했기 때문에
# a dummy @profile decorator) 를 만들어줘야 에러가 나지 않는다.
if 'line_profiler' not in dir() and 'profile' not in dir():
    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner

@profile
def some_fn(useful_input):
    """An expensive function that we wish to both test and profile"""
    # artificial 'we're doing something clever and expensive' delay
    time.sleep(1) 
    return useful_input ** 2


if __name__ == "__main__":
    print(f"Example call `some_fn(2)` == {some_fn(2)}")
