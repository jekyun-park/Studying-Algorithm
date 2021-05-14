function solution(numbers, hand) {
  let answer = "";

  const leftHand = [1, 4, 7, 10];
  const rightHand = [3, 6, 9, 11];
  const whichHand = [2, 5, 8, 0];

  let curL = 10;
  let curR = 11;
  let leftD;
  let rightD;

  for (let i = 0; i < numbers.length; i++) {
    if ((numbers[i] === 1) | (numbers[i] === 4) | (numbers[i] === 7)) {
      answer += "L";
      curL = numbers[i];
    } else if ((numbers[i] === 3) | (numbers[i] === 6) | (numbers[i] === 9)) {
      answer += "R";
      curR = numbers[i];
    } else {
      if (whichHand.indexOf(numbers[i]) === leftHand.indexOf(curL)) {
        leftD = 1;
      } else if (whichHand.includes(curL)) {
        leftD = Math.abs(
          whichHand.indexOf(numbers[i]) - whichHand.indexOf(curL)
        );
      } else if (!whichHand.includes(curL)) {
        leftD =
          Math.abs(whichHand.indexOf(numbers[i]) - leftHand.indexOf(curL)) + 1;
      }

      if (whichHand.indexOf(numbers[i]) === rightHand.indexOf(curR)) {
        rightD = 1;
      } else if (whichHand.includes(curR)) {
        rightD = Math.abs(
          whichHand.indexOf(numbers[i]) - whichHand.indexOf(curR)
        );
      } else if (!whichHand.includes(curR)) {
        rightD =
          Math.abs(whichHand.indexOf(numbers[i]) - rightHand.indexOf(curR)) + 1;
      }

      if (leftD === rightD) {
        if (hand === "right") {
          answer += "R";
          curR = numbers[i];
        } else if (hand === "left") {
          answer += "L";
          curL = numbers[i];
        }
      } else if (leftD > rightD) {
        answer += "R";
        curR = numbers[i];
      } else if (leftD < rightD) {
        answer += "L";
        curL = numbers[i];
      }
    }
  }
  return answer;
}
