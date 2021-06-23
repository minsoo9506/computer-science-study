from datetime import timedelta

class DateRangeIterable:
    """자체 iterator를 갖고 있는 iterable"""
    
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_date = start_date

    def __iter__(self):
        return self 
        # 자기자신이 iterable!
        # for 문에서 사용하면 next함수를 실행할 것
        # __next__ 안만들고자 한다면 __iter__에서 반복가능하도록 만들어야함

    def __next__(self):
        if self._present_date >= self.end_date:
            raise StopIteration
        today = self._present_date
        self._present_date += timedelta(days=1)
        return today