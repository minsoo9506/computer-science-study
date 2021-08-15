from datetime import datetime
from itertools import count, filterfalse, groupby, islice
from random import normalvariate, randint

from scipy.stats import normaltest

def read_data(filename):
    with open(filename) as fd:
        for line in fd:
            data = line.strip().split(",")
            timestamp, value = map(int, data)
            yield datetime.fromtimestamp(timestamp), value

# 실제 data가 없으니까 아래처럼 만들자
def read_fake_data(filename):
    for timestamp in count():
        # 일주일에 1번은 이상치
        if randint(0, 7 * 60 * 60 * 24 - 1) == 1:
            value = normalvariate(0, 1)
        else:
            value = 100
        yield datetime.fromtimestamp(timestamp), value

def groupby_day(iterable):
    key = lambda row : row[0].day
    for day, data_group in groupby(iterable, key):
        yield list(data_group)

def is_normal(data, threshold=1e-3):
    _, values = zip(*data)
    _, p_value = normaltest(values)
    if p_value < threshold:
        return False
    return True

def filter_anomalous_groups(data):
    # data중에서 is_normal에 통과하지 못한 부분만 얻을 수 있다
    yield from filterfalse(is_normal, data) 


def filter_anomalous_data(data):
    data_group = groupby_day(data)
    yield from filter_anomalous_groups(data_group)


if __name__ == "__main__":
    data = read_fake_data("fake_filename")
    anomaly_generator = filter_anomalous_data(data)
    first_five_anomalies = islice(anomaly_generator, 5) # 이상치 5개 찾을 때까지 데이터 생성

    for data_anomaly in first_five_anomalies:
        start_date = data_anomaly[0][0]
        end_date = data_anomaly[-1][0]
        print(f"Anomaly from {start_date} - {end_date}")