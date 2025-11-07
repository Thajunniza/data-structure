console.log("Solid Rectangle");

/**
 * 
 * @param {number} rows - number of rows
 * @param {number} cols - number of columns
 * @return {string[]} result - returns an array of strings,each string is a row of the pattern
 */
function generateSolidRectangle(rows, cols) {
  let result = [];
  for (let i = 0; i < rows; i++) {
    let row = "";
    for (let j = 0; j < cols; j++) {
      row += "*";
    }
    result.push(row);
  }
  return result;
}

const pattern = generateSolidRectangle(3, 5);
console.log(pattern);
pattern.forEach(line=>console.log(line));

/** Solid Rectangle - Output
*[ '*****', '*****', '*****' ]
*****
*****
*****
*/
