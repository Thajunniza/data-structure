console.log("Solid Rectangle");

/**
 * @param {number} row - number of rows
 * @param {number} column - number of columns
 * @returns {string[]} result - array of string , where each string is a row of *
 * Time Complexity: O(row * column)
 * Space Complexity: O(row * column)
 */
function generateSolidRectangleArray(row, column) {
  let result = [];
  for (let i = 0; i < row; i++) {
    let rows = "";
    for (let j = 0; j < column; j++) {
      rows += "*";
    }
    result.push(rows);
  }
  return result;
}

const patternArray = generateSolidRectangleArray(4, 5);
console.log("Solid Rectangle Array");
console.log(patternArray);
patternArray.forEach((row) => console.log(row));

/**
 * @param {number} row - number of rows
 * @param {number} column - number of columns
 * @returns {String} result - String with line for each row
 * Time Compexity: O(row * column)
 * Space Complexity: O(row * column)
 */
function generateSolidRectangleString(row, column) {
  let result = "";
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < column; j++) {
      result += "*";
    }
    result += "\n";
  }
  return result.trim();
}

const patternStr = generateSolidRectangleString(5, 6);
console.log("Solid Rectangle String");
console.log(patternStr);

/** Solid Rectangle - Output
 *[ '*****', '*****', '*****' ]
 *****
 *****
 *****
 */
