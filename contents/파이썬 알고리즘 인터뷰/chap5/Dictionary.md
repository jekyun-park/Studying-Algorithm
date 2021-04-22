# Dictionary 딕셔너리

파이썬의 **딕셔너리**는 **키/값** 쌍으로 이루어진 딕셔너리를 말한다. 내부적으로 해시테이블로 구현되어 있다.

각 언어별 해시테이블을 이용한 키/값 자료형은 다음과 같다.

|언어|해시 테이블|
|:--:|:--:|
|파이썬|dict()|
|C++|std::unordered_map|
|자바|HashMap|

인덱스를 숫자로만 지정할 수 있는 리스트와 달리 **딕셔너리**는 문자를 포함해 다양한 타입을 키로 사용할 수 있다. 특히, 파이썬의 딕셔너리는 해시할 수만 있다면 숫자뿐만 아니라, 문자, 집합까지 불변 객체를 모두 키로 사용할 수 있다. 이 과정을 해싱이라고 하며, 해시 테이블을 이용해 자료를 저장한다. 무엇보다 해시 테이블은 다양한 타입을 키로 지원하면서도 입력과 조회 모두 O(1)에 가능하다. 최악의 경우 O(n)이 된다.

|연산|시간 복잡도|설명|
|:--:|:--:|:---:|
|len(a)|O(1)|요소의 개수를 리턴|
|a[key]|O(1)|키를 조회하여 값을 리턴|
|a[key]=value|O(1)|키/값을 삽입|
|key in a|O(1)|딕셔너리에 키가 존재하는지 확인|

이처럼 딕셔너리는 대부분의 연산이 O(1)에 처리 가능한 매우 우수한 자료형이며, 리스트 만큼이나 매우 빈번하게 쓰인다.

- 파이썬 3.7+ 딕셔너리 입력 순서 유지
- 파이썬 3.6+ 딕셔너리 메모리 사용량 20% 감소

## 딕셔너리의 활용 방법

```python

# 딕셔너리 선언

>>> a = dict()

# 혹은

>>> a = {}

# 초기값 선언 및 키/값 추가

>>> a = {'key1':'value1','key2':'value2'}

>>> a
{'key1':'value1','key2':'value2'}

>>> a['key3'] = 'value3'

>>> a
{'key1':'value1','key2':'value2','key3':'value3'}

# 키를 지정함으로 값 조회 / 존재하지 않는 키 조회시 에러 발생

>>> a['key1']
'value1'

>>> a['key4']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'key4'

# try 구문으로 예외 처리

try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

# del을 이용하여 삭제

>>> del a['key1']

>>> a
{'key2':'value2','key3':'value3'}

# 존재하지 않는 키 삭제시에도 KeyError 발생 

>>> del a['key4']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'key4'

# 키가 존재하는지 미리 확인하는 logic 도 있다.

>>> 'key4' in a
False

>>> if 'key4' in a:
        print('존재하는 키')
    else:
        print('존재하지 않는 키')

존재하지 않는 키

# 딕셔너리의 items() 메소드를 사용하여 키와 값을 모두 조회 가능

>>> for k,v in a.items():
        print(k,v)

key1 value1
key2 value2
key3 value3
```

## 딕셔너리 모듈

딕셔너리와 관련된 특수한 형태의 컨테이너 자료형인 defaultdict,Counter,OrderedDict 등이 있다.

### defaultdict 객체

defaultdict 객체는 존재하지 않는 키를 조회할 경우, 에러 메시지를 출력하는 대신 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성해준다. 실제로는 collections.defaultdict 클래스를 갖는다.

```python

>>> a = collections.defaultdict(int)

# A와 B에 5와 4를 할당

>>> a['A'] = 5
>>> a['B'] = 4

>>> a
defaultdict(<class 'int'>, {'A': 5, 'B': 4})

# 존재하지 않는 C에 +1 연산

>>> a['C'] += 1

# 디폴트인 0을 기준으로 자동생성 후 1을 더함.

>>> a
defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})
```

### Counter 객체

Counter 객체는 아이템에 대한 개수를 계산해 딕셔너리로 리턴해준다.collections.Counter 클래스를 갖는다.

```python

# 키에는 아이텝의 값이, 값에는 아이템의 개수가 들어간 딕셔너리를 생성한다.

>>> a = [1,2,3,4,5,5,5,6,6]
>>> b = collections.Counter(a)
>>> b
Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})

# collections.Counter 클래스를 가짐.

>>> type(b)
<class 'collections.Counter'>

# 빈도가 가장 높은 2개 요소를 추출함. 5는 3개, 6은 2개임.

>>> b.most_common(2)
[(5, 3), (6, 2)]
```

### OrderedDict 객체

```python

>>> collections.OrderedDict({'banana':3,'apple':4,'pear':1,'orange':2})
OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])
```

파이썬 3.6 이하에서는 딕셔너리의 입력 순서가 유지되지 않았으나, 3.7부터는 딕셔너리의 내부적으로 인덱스를 이용하여 입력 순서가 유지되도록 개선되었다. 따라서 더이상 OrderedDict를 사용할 필요는 없으며 기본 딕셔너리를 이용해도 입력 순서가 유지된다.
