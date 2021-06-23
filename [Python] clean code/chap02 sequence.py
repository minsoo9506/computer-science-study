from datetime import timedelta

# 반복가능
# 특정 위치의 날짜를 가져오는 것도 O(1) 라서 빠름
# 근데 메모리는 더 많이 먹음

class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, days_idx):
        return self._range[days_idx]

    def __len__(self):
        return len(self._range)