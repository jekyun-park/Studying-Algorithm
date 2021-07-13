# 타겟 넘버

## 문제 설명

n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

```javascript

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

```
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

## 제한사항
- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

## 입출력 예

numbers|target|return
|:---|:---|:---|
|[1,1,1,1,1]|3|5

## 풀이

```javascript
function solution(numbers, target) {
    var answer = 0;
    recursion(0,0);
    return answer;
    
    function recursion(cnt,sum){
        if(cnt === numbers.length){
            if(sum === target){
                answer ++;
            }
            return
        }
        recursion(cnt+1,sum+numbers[cnt]);
        recursion(cnt+1,sum-numbers[cnt]);
    }
}
```

## 설명

재귀를 이용하였다. 숫자는 numbers에서 받은것을 사용하고 부호만 결정하여서 계산하여 타겟값을 만드는 방법이 몇가지인지 알아내는 문제이다. cnt는 현재 보고있는 숫자의 index를 나타내고, sum은 각각의 숫자를 더하거나 뺀 결과를 저장한다. 마지막 자리까지 다 돌고 난 후, sum이 타겟값과 같다면 answer에 1을 더해주고 리턴한다.
