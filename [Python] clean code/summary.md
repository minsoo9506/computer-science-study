### chapter01 코드 포매팅과 도구
- Docstrings 작성
- annotation 작성
- 검사 자동화
  - `Mypy` : 타입불일치 검사
  - `Pylint` : 코드의 구조 검사

### chapter02 파이썬스러운 코드
- 인덱스와 슬라이스
  - list, tuple, 문자열은 sequence 객체
  - `[]` 로 인덱싱과 슬라이싱 가능
  - 이는 `__len__`, `__getitem__` magic method 덕분에 가능
- 파이썬에서 밑줄
  - `self._var` 같이 밑줄을 써서 private (기능 x, 약속 o)
- 프로퍼티(`@property`)
  - 객체의 어떤 속성에 대한 접근을 제어하려는 경우 사용
  - 명령-쿼리 분리원칙
  - 예시 (chap02 property.py)
- 이터러블 객체
  - list, tuple, set, dictionary 모두 반복가능한 객체
  - 이런 내장 반복형 객체 이외에도 자체 iterable을 만들면 반복가능
  - iterable : `__iter__` 매직 메서드를 구현한 객체
    - for문에서 반복가능
    - 근데 `next()`함수는 사용 x, 사용하려면 iterator로 바꿔야함
  - iterator : `__next__` 매직 메서드를 구현한 객체
  - list, tuple, set, dictionary들은 iterable이지만 iterator는 아니다 (`next()`함수 씌우면 에러발생)
  - 예시 (chap02 iterable.py)
- 시퀀스 만들기
  - `iter()`함수는 객체에 `__iter__`가 없으면 `__getitem__`을 찾음
  - `__getitem__`만 잘 구현되어 있으면 반복가능 
  - 예시 (chap02 sequence.py)
- 컨테이너 객체
  - 컨테이너 : `__contains__` 메서드를 구현한 객체
  - 코드 `element in container` 를 `container.__contains__(element)`로 해석
  - 예시 (chap02 container.py)
- 객체의 동적인 속성
  - `__getattr__` 매직 메서드를 사용해 객체에서 속성을 얻는 방법을 제어할 수 있음 (chap02 getattr.py)
- 호출형(callable) 객체
  - `__call__`를 사용하여 객체를 일반 함수처럼 호출 
  - `object(*args, **kwargs)`와 같은 구문이 `object.__call__(*args, **kwargs)`로 변환됨
  - 예시 (chap02 callable.py)

### chapter03 좋은 코드의 일반적인 특징
- 방어적 프로그래밍
  - 예상할 수 있는 시나리오의 오류를 처리하는 방법 : 에러 핸들링 프로시저
  - 발생하지 않아야 하는 오류를 처리하는 방법 : assertion
  - 에러 핸들링
    - 값 대체
    - 예외처리
      - 적절한 추상화 단계에서 예외 처리
      - Traceback 노출 금지
      - 비어있는 except 블록 지양
      - 원본 예외 메시지 포함 by `raise {e} from {original_exception}`
  - 파이썬에서 assertion 사용하기
    - `assert` 문에 사용된 표현식은 불가능한 조건을 의미
- 관심사의 분리
  - high cohesion low coupling
  - 객체는 작고 잘 정의된 목적을 가지며 가능하면 작아야 한다
  - 서로 다른 객체는 서로 의존성이 적어야 한다

### chapter04 SOLID 원칙
- S : 단일 책임 원칙 (single responsibility principle, SRP)
  - 소프트웨어 컴포넌트(일반적으로 클래스)는 하나의 역할만 해야한다!
- O : 개방/폐쇄 원칙 (open/close principle)
  - 유지보수가 쉽도록 로직을 캡슐화하여 확장에는 개방되고 수정에는 폐쇄!
- L : 리스코프 치환 원칙 (Liskov substitution principle, LSP)
  - 안정성을 유지하기 위해 객체 타입이 유지해야하는 일련의 특성을 의미
- I : 인터페이스 분리 원칙 (interface segregation principle, ISP)
  - 다중 메서드를 가진 인터페이스가 있다면 더 적은 수의 메서드를 가진 여러 개의 메서드로 분할하자!
- D : 의존성 역전 원칙 (DIP)

### chapter05 데코레이터를 사용한 코드 개선
- 함수 데코레이터
- 클래스 데코데이터
- 패턴이 생기고 데코레이터에 대한 추상화가 명확해지면 그 때 리팩토링
- 데코레이터가 적어도 3회 이상 필요한 경우에만 구현
- 데코레이터 코드를 최소한으로 유지

### chapter07 제너레이터 사용하기
- 어떤 함수라도 `yield` 키워드를 사용하면 제너레이터 함수가 된다
- 모든 제너레이터 객체는 이터러블!