# 빅오

빅오 ( O, big-O ) 란 입력값이 무한대로 향할때 함수의 상한을 설명하고,
**점근적 실행 시간(Asymptotic Running Time)** 을 표기할때 가장 널리 쓰이는 수학적 표기법 중 하나이다.

## 점근적 실행 시간 (Asymptotic Running Time)

 입력값 n 이 커질 때, 즉 입력값이 무한대를 향할 때 lim (n→∞) 함수의 실행 시간의 추이를 의미한다.

 > 알고리즘은 궁극적으로 컴퓨터로 구현되므로, 컴퓨터의 빠른 처리 능력을 감안하면 아무리 복잡한 알고리즘도 입력의 크기가 작다면 금방 끝나버린다. 따라서 관심의 대상은 입력의 크기가 충분히 클 때이다.

점근적 실행 시간은 달리 말하면 **_시간 복잡도_** 이다.

## 시간 복잡도 (Time Complexity)  

 어떤 알고리즘을 수행하는 데 걸리는 시간을 설명하는 _계산 복잡도_ ( Computational Complexity )를 의미하며, 계산 복잡도를 표기하는 대표적인 방법이 바로 **빅오**다.

- O(1) : 입력값이 아무리 크던 작던 일정한 실행 시간을 가진다. 최고의 알고리즘이지만 신중해야 한다. 상수 시간에 실행된다 해도 상수값이 상상을 넘을 정도로 매우 크다면 사실상 의미가 없기 때문이다. 대표적으로 *해시 테이블의 조회 및 삽입 알고리즘*이 이에 해당한다.

- O(logn) : 로그는 매우 큰 입력값에도 크게 영향을 받지 않는 편으로, 매우 견고하다. 대표적으로 *이진검색*이 이에 해당한다.

- O(n) : 입력값 만큼 실행 시간에 영향을 받는다. 이러한 알고리즘을 **선형 시간 알고리즘** 이라고 한다.*정렬되지 않은 리스트의 최대값 혹은 최솟값을 찾는 경우*가 이에 해당한다.

- O(n log n) : 대부분의 효율 좋은 정렬 알고리즘이 여기에 해당한다. 적어도 모든 수에 대해 한번 이상은 비교해야 하는 비교 기반 정렬 알고리즘은 아무리 좋은 알고리즘도 O(n log n) 보다 빠를 수 없다.

- O(n^2) : 버블 정렬과 같은 비효율적인 정렬 알고리즘이 이에 해당한다.

- O(2^n) : n^2 과 비슷해 보이지만 2^n 이 훨씬 크다. *피보나치 수를 재귀로 계산하는 알고리즘*이 이에 해당한다.

- O(n!) : 외판원 문제를 브루트 포스로 해결할때가 이에 해당하며, 가장 느린 알고리즘이다. 입력값이 조금만 커져도 웬만한 다항시간 내에는 계산이 어렵다.

## 상한, 최악

빅오 (O)는 상한(Upper Bound)를 의미한다. 이외에도 하한(Lower Bound)을 나타내는 빅오메가 (Ω), 평균을 의미하는 빅세타 (θ)가 있다.

중요한 점은, 상한과 최악의 경우를 혼동하지 않는 것이다.

> 빅오 표기법은 주어진(최선/최악/평균) 경우의 수행 시간의 상한을 나타낸다.

## 분할 상환 분석 (Amortized Analysis)

최악의 경우를 여러 번에 걸쳐 골고루 나눠주는 형태로 알고리즘의 시간 복잡도를 계산하여 분석하는 방법이다. 알고리즘 전체를 보지 않고 최악의 경우만을 살펴보는것은 비관적이기 때문에 최근에는 시간 복잡도를 분석할때 매우 보편적으로 널리 사용된다.

## 병렬화

일부 알고리즘들은 병렬화로 실행 속도를 높일 수 있다. 최근 딥러닝의 인기와 함께 병렬 연산을 위한 대표적인 장치인 GPU 또한 주목을 받고 있다. 알고리즘 자체의 시간 복잡도 이외에도 알고리즘이 병렬화가 가능한지는 근래 알고리즘 우수성을 평가하는 매우 중요한 척도 중 하나이다.
