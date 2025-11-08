console.log("Diamond Star Pattern");

//Its a combination of pyramid and inverted pyramid so
// you need two fuction

/**
 * @param {number} row - no of rows
 * @returns {string[]} result
 * Time Complexity : O(n²)
 * Space Complexity: O(n²)
 */
function generateFullStarPyramid(rows) {
  let result = [];
  for (let i = 0; i < rows; i++) {
    let line = "";
    // for space
    let k = rows - i;
    for (let j = 1; j < k; j++) {
      line += " ";
    }
    // for *
    k = 2 * i + 1;
    for (let j = 0; j < k; j++) {
      line += "*";
    }
    result.push(line);
  }
  return result;
}

/**
 * @param {number} rows - no of rows
 * @param {string[]} return
 */
function generateInvertedStarPyramid(rows) {
  let result = [];
  for (let i = rows ; i > 0; i--) {
    let line = "";
    // for space
    let k = rows - i ;
    for (let j = 0; j < k; j++) {
      line += " ";
    }
    // for *
    k = 2 * i - 1;
    for (let j = 0; j < k; j++) {
      line += "*";
    }
    result.push(line);
  }
  return result;
}

const pattern = generateFullStarPyramid(4);
pattern.forEach((line) => console.log(line));
const pattern1 = generateInvertedStarPyramid(4);
const pattern2 = pattern1.slice(1);
pattern2.forEach(line => console.log(line));

/** Output
   *
  ***
 *****
*******
 *****
  ***
   *

 */

