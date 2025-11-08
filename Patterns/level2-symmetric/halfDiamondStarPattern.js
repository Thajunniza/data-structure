console.log("Half Diamond Star Pattern");

/**
 * Half Diamond Star Pattern
 * @param {number} n
 * @return {result}
 * Time Complexity : O(n²)
 * Space Complexity: O(n²)
 */
function generateHalfDiamondStarPattern(n) {
  let result = [];
  let rows = 2 * n - 1;
  for (let i = 1; i <= rows; i++) {
    let line = "";
    let k = i;
    if (i > n) {
      k = 2 * n - i;
    }
    for (let j = 0; j < k; j++) {
      line += "*";
    }
    result.push(line);
  }
  return result;
}

const pattern = generateHalfDiamondStarPattern(5);
pattern.forEach((line) => console.log(line));


/**
 * Output

*
**
***
****
*****
****
***
**
*
 */
