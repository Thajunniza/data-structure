console.log("Number Crown Pattern");

/**
 * Problem Understanding:
 * -------------------------
 * The goal is to print a symmetric numeric "crown" pattern.
 * 
 * Example (for n = 5):
 * 1        1
 * 12      21
 * 123    321
 * 1234  4321
 * 1234554321
 *
 * The pattern grows outward on both sides while the spaces in the middle shrink.
 *
 * Pattern Structure:
 *  - Each row has ascending numbers on the left.
 *  - Spaces in the center (that decrease by 2 per row).
 *  - Descending numbers on the right.
 *
 * Formula:
 *  - Total columns = n * 2
 *  - For each position j in a row:
 *      - If j > i and j <= col - i → print space
 *      - Else if j <= i → print ascending number (j)
 *      - Else → print descending number (col - j + 1)
 */

/**
 * @param {number} n - no of row
 * @returns {string[]} result
 * Time Complexity : O(n²)
 * Space Complexity: O(n²)
 */
function generateNumberCrownPattern(n) {
  let result = [];
  const col = n * 2;
  for (let i = 1; i <= n; i++) {
    let line = "";
    for (let j = 1; j <= col; j++) {
      if (j > i && j <= col - i) {
        line += " ";
      } else if (j <= i) {
        line += j;
      } else {
        line += col - j + 1;
      }
    }
    result.push(line);
  }
  return result;
}

let pattern = generateNumberCrownPattern(5);
pattern.forEach((line) => console.log(line));


/**
 * Output
Number Crown Pattern
1        1
12      21
123    321
1234  4321
1234554321
 */