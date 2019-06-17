/**
 * @param {string} digits
 * @return {string[]}
 */

function letterCombinationsRecur(lookup, digits, results, acc , n){
  if (n === digits.length){
    results.push(acc);
  } else {
    for (var i = 0; i < lookup[parseInt(digits[n])].length; i++){
      var c = lookup[digits[n]][i];
      letterCombinationsRecur(lookup, digits, results, acc + c, n + 1);
    }
  }
}


var letterCombinations = function(digits) {
	var lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"];
  results = [];
  letterCombinationsRecur(lookup, digits, results, "", 0);
  return results;
};

letterCombinations("23");
