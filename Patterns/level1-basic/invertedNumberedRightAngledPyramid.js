console.log("Inverted Numbered Right Pyramid");

/**
 * Inverted Numbered Right Pyramid
 * @param {number} rows - no of rows to be printed
 * @return {string} result - string
 * Time Complexity : O(n²)
 * Space Complexity : O(n²)
 */
function generateInvertedNumberedRightAngledPyramid(rows) {
  let result = "";
  for (let i = rows; i > 0; i--) {
    for (let j = 1; j <= i; j++) {
      result += j;
    }
    result += "\n";
  }
  return result.trim();
}

const pattern = generateInvertedNumberedRightAngledPyramid(5);
console.log(pattern);
