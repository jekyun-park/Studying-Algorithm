function solution(board, moves) {
  let popnum = 0;
  let baguni = [];
  let score = 0;

  for (let i = 0; i < moves.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[j][moves[i] - 1] !== 0) {
        if (board[j][moves[i] - 1] === baguni[baguni.length - 1]) {
          baguni.pop();
          score += 2;
        } else {
          baguni.push(board[j][moves[i] - 1]);
        }
        board[j][moves[i] - 1] = 0;
        break;
      }
    }
  }
  return score;
}
