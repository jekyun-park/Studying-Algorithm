function solution(nums) {
  let answer = 0;

  const halfNums = nums.length / 2;
  const species = new Set(nums);
  const speciesArray = Array.from(species);

  if (speciesArray.length > halfNums) {
    answer = halfNums;
  } else {
    answer = speciesArray.length;
  }

  //   answer = speciesArray.length > halfNums ? halfNums : speciesArray.length 삼항연산자를 사용하여 코드 간결하게

  return answer;
}
