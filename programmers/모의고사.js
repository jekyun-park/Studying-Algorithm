function solution(answers) {
  let answer = [];

  let firstMan = [1, 2, 3, 4, 5];
  let secondMan = [2, 1, 2, 3, 2, 4, 2, 5];
  let thirdMan = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let firstManNum = 0;
  let secondManNum = 0;
  let thirdManNum = 0;

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === firstMan[i % 5]) {
      firstManNum += 1;
    }
    if (answers[i] === secondMan[i % 8]) {
      secondManNum += 1;
    }
    if (answers[i] === thirdMan[i % 10]) {
      thirdManNum += 1;
    }
  }

  let scores = [firstManNum, secondManNum, thirdManNum];
  let max = Math.max(firstManNum, secondManNum, thirdManNum);

  if (max === firstManNum) {
    answer.push(1);
  }
  if (max === secondManNum) {
    answer.push(2);
  }
  if (max === thirdManNum) {
    answer.push(3);
  }

  return answer;
}
