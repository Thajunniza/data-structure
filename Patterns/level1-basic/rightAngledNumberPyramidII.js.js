console.log("Right Angled Number Pyramid 2");

/**
 *
 * @param {number} rows - No of rows need to be printed
 * @returns {string[]} result - array of String where each row prints the current row number, repeated the same number of times as the row itself.
 * Time Complexity : O(n²)
 * Space Complexity : O(n²)
 */

function generateRightAngledNumberPyramid2(rows) {
  let result = [];
  for (let i = 1; i <= rows; i++) {
    let line = "";
    for (let j = 1; j <= i; j++) {
      line += i;
    }
    result.push(line);
  }
  return result;
}

const pattern = generateRightAngledNumberPyramid2(5);
pattern.forEach((row) => console.log(row));
