console.log("Full Star Pyramid");

/**
 * @param {number} row - no of rows
 * @returns {string[]} result
 * Time Complexity : O(n²)
 * Space Complexity: O(n²)
 */
function generateFullStarPyramid(rows) {
  let result = [];
  for (let i = 1; i <= rows; i++) {
    let line = "";
    for (let j = 0; j < rows - i; j++) {
      line += " ";
    }
    let k = 2 * i - 1;
    for (let j = 0; j < k; j++) {
      line += "*";
    }
    result.push(line);
  }
  return result;
}

const pattern = generateFullStarPyramid(5);
pattern.forEach((row) => console.log(row));

/**
 * Output
Full Star Pyramid
    *
   ***
  *****
 *******
*********
 */
