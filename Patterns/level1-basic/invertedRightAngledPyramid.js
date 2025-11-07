console.log("Inverted Right Angled Pyramid");

/**
 * @param {number} rows - no of rows need to be printed
 * @returns {string[]} result- array of string with the maximum number of `*` in the first row and decreases by one `*` in each subsequent row
 * Time Complexity : O(n²)
 * Space Complexity : O(n²)
 */
function generateInvertedRightAngledPyramid(rows) {
  let result = [];
  for (let i = rows; i > 0; i--) {
    let line = "";
    for (let j = 0; j < i; j++) {
      line += "*";
    }
    result.push(line);
  }
  return result;
}

const pattern = generateInvertedRightAngledPyramid(5);
pattern.forEach(row => console.log(row));


/**
 * Output
*****
****
***
**
* 
 */