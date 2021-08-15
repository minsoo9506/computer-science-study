- 저작권상 핵심내용을 모두 요약하지는 못함
- 모든 코드는 [여기](https://github.com/mynameisfiber/high_performance_python_2e)에 저자가 공개

## Chapter 01
- 기본적인 연산장치, 메모리장치, 통신계층까지 고려해야 고성능!
- 캐시를 잘 이용하자
- Python은 메모리를 자동으로 할당하고 배제하는 Garbage Collector(GC)를 사용한다
  - Python 객체가 메모리에 최적화 저장 x
- `pytest`, `black`, `flake8`

## Chapter 02 프로파일링으로 병목 지점 찾기
- 시간 측정 방법 : `print`, decorator
  - print를 이용하여 시간측정 [`code`](./Chapter%2002/01_julia_print.py)
  - decorator를 이용하여 시간측정 [`code`](./Chapter%2002/02_julia_deco.py)
- `cProfile` : 표준라이브러리에 내장된 프로파일링 도구
  -  `python -m cProfile -s cumulative "01_julia_print.py"` : 실행하면 아래와 같은 결과
  -  `percall`의 합과 `cumtime`의 차이는 `cProfile`의 오버헤드라고 할 수 있다.
  -  `python -m cProfile -o profile.stats "01 julia_print.py"` : 좀 더 자세한 통계지표 저장
  -  `python -m snakeviz profile.stats` : 시각화

```
Length of x: 1000
Total elements: 1000000
calculate_z_serial_purepython took 12.100432872772217 seconds
         36221997 function calls in 12.750 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   12.750   12.750 {built-in method builtins.exec}
        1    0.022    0.022   12.750   12.750 01 julia_print.py:1(<module>)
        1    0.471    0.471   12.729   12.729 01 julia_print.py:22(calc_pure_python)
        1    8.484    8.484   12.100   12.100 01 julia_print.py:8(calculate_z_serial_purepython)
 34219980    3.616    0.000    3.616    0.000 {built-in method builtins.abs}
  2002000    0.151    0.000    0.151    0.000 {method 'append' of 'list' objects}
        1    0.006    0.006    0.006    0.006 {built-in method builtins.sum}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method time.time}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
- `line_profiler` : 한 줄씩 프로파일
  - 프로파일하려는 함수에 `@profile`을 붙여야 한다.
  - `kernprof -l -v 04_julia_lineprof.py` : 실행하면 아래와 같은 결과
  - `-l` : 함수 단위가 아니라 한 줄씩 프로파일하겠다는 옵션
  - `-v`

```
Length of x: 1000
Total elements: 1000000
calculate_z_serial_purepython took 60.25175428390503 seconds
Wrote profile results to 04_julia_lineprof.py.lprof
Timer unit: 1e-06 s

Total time: 39.0277 s
File: 04_julia_lineprof.py
Function: calculate_z_serial_purepython at line 7  

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           @profile
     8                                           def calculate_z_serial_purepython(maxiter, zs, cs):    
     9                                               """Calculate output list using Julia update rule"""
    10         1       2052.8   2052.8      0.0      output = [0] * len(zs)
    11   1000001     272898.0      0.3      0.7      for i in range(len(zs)):
    12   1000000     263602.3      0.3      0.7          n = 0
    13   1000000     310543.1      0.3      0.8          z = zs[i]
    14   1000000     295027.4      0.3      0.8          c = cs[i]
    15  34219980   15696423.6      0.5     40.2          while abs(z) < 2 and n < maxiter:
    16  33219980   11758266.4      0.4     30.1              z = z * z + c
    17  33219980   10124578.0      0.3     25.9              n += 1
    18   1000000     304269.3      0.3      0.8          output[i] = n
    19         1          0.4      0.4      0.0      return output

Total time: 61.7465 s
File: 04_julia_lineprof.py
Function: calc_pure_python at line 22

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    22                                           @profile
    23                                           def calc_pure_python(draw_output, desired_width, max_iterations):
    24                                               """Create a list of complex co-ordinates (zs) and complex parameters (cs), build Julia set and display"""
    25         1          2.1      2.1      0.0      x_step = (x2 - x1) / desired_width
    26         1          0.8      0.8      0.0      y_step = (y1 - y2) / desired_width
    27         1          0.4      0.4      0.0      x = []
    28         1          0.3      0.3      0.0      y = []
    29         1          0.3      0.3      0.0      ycoord = y2
    30      1001        359.2      0.4      0.0      while ycoord > y1:
    31      1000        394.7      0.4      0.0          y.append(ycoord)
    32      1000        353.5      0.4      0.0          ycoord += y_step
    33         1          0.4      0.4      0.0      xcoord = x1
    34      1001        363.5      0.4      0.0      while xcoord < x2:
    35      1000        393.5      0.4      0.0          x.append(xcoord)
    36      1000        356.8      0.4      0.0          xcoord += x_step
    37
    38         1          0.4      0.4      0.0      zs = []
    39         1          0.3      0.3      0.0      cs = []
    40      1001        374.5      0.4      0.0      for ycoord in y:
    41   1001000     338450.3      0.3      0.5          for xcoord in x:
    42   1000000     557246.5      0.6      0.9              zs.append(complex(xcoord, ycoord))
    43   1000000     590025.7      0.6      1.0              cs.append(complex(c_real, c_imag))
    44
    45         1        150.8    150.8      0.0      print("Length of x:", len(x))
    46         1        172.5    172.5      0.0      print("Total elements:", len(zs))
    47         1          3.0      3.0      0.0      start_time = time.time()
    48         1   60251712.5 60251712.5     97.6      output = calculate_z_serial_purepython(max_iterations, zs, cs)
    49         1          3.2      3.2      0.0      end_time = time.time()
    50         1          0.8      0.8      0.0      secs = end_time - start_time
    51         1        164.9    164.9      0.0      print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")
    52
    53         1       5997.9   5997.9      0.0      assert sum(output) == 33219980
```
- `py-spy` : 샘플링 프로파일러
- `dis` : cpython의 바이트코드 프로파일러
- 단위 테스트는 꼭 하자
  - `pytest 05_test.py` 
  - prefix가 `test`인 함수만 인식하여 테스트 한다. [`code`](./Chapter%2002/05_test.py)

## Chapter03 List, Tuple
- 공통적으로 배열이라는 자료구조 이용
- 근데 리스트는 동적인 배열, 튜플은 정적인 배열
- 튜플은 런타임에서 캐시해서 GC가 메모리를 바로 회수 x -> 같은 크기의 튜플이 나중에 다시 필요해지면 기존 메모리 재사용 (OS를 skip하고)

## Chapter04 Dictionary, Set
  
## Chapter05 제너레이터
- 현잿값만 필요한 경우 메모리 사용 측면에서 유리
- 대용량 데이버 분석에 제너레이터를 사용하는 예제 [`code`]()

## Chapter06 행렬과 벡터 계산
- Python 리스트는 데이터를 저장하는게 아닌 포인터를 저장
  - 리스트 대신 `array` 모듈을 사용하면 데이터를 메모리에 순차적으로 저장
  - 근데 이 값들을 수학적으로 계산할 때는 `numpy` 사용이 더 좋은 것 같다
- `perf` 로 cache-misses 같은 것 분석할 수 있다
  - cache-misses를 개선하자
- 메모리 할당을 최소화, 메모리 지역성 고려
- `numpy` 등 좋은 라이브러리를 잘 활용하자
- `pandas`도 빠르게 쓸 수 있는 방법들이 다양하게 존재

## Chapter07 C언어로 컴파일하기
- `Cython`, `Numba`, `PyPy`
- 컴파일로 빨라지는 부분은 대부분 수학적인 부분 