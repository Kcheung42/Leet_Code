/**
 * @param {number[][]} A
 * @return {number}
 */

function minFallRecur(A, row, col, sum){
  //base case 1
  if(row === A.length){
    // console.log('sum:' + sum);
    return sum;
  }
  //base case 2

  var indexes = [col-1, col, col + 1].filter((i) => i >= 0);
  // console.log('row:' + row);
  // console.log('next-inddexes' + indexes);

  var minSum = Number.MAX_VALUE;
  var x = indexes.forEach((c) => {
    minSum = Math.min(minSum, minFallRecur(A, row + 1, c, sum + A[row][col]));
  }
                         );
  return minSum;
}

var minFallingPathSum = function(A) {
  return (minFallRecur(A, 0, 0, 0));
};

minFallingPathSum([[1,2,3], [4,5,6],[7,8,9]]);
