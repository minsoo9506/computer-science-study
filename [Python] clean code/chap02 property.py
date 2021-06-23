# 객체의 어떤 속성에 대한 접근을 제어하려는 경우 사용
# 명령-쿼리 분리

def is_valid_num(num: str):
    return len(num) == 10

class User:
    def __init__(self, username):
        self.username = username
        self._num = None # private하게 하고 싶다

    @property
    def personal_num(self):
        return self._num

    @personal_num.setter
    def personal_num(self, new_num):
        if not is_valid_num(new_num):
            raise ValueError(f"숫자의 길이가 잘못되었습니다.")
        self._num = new_num

me = User('song')
me.personal_num = '1234567890'
print(me.personal_num)