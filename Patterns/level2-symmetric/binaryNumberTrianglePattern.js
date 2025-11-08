console.log("Binary Number Triangle Pattern");

/**
 * Solution
 * rows is equal to n
 * no of columns of each row is equal to the index +1 so start i with 1
 * it should start with 1 so start when the i is odd start with 1 else 0
 * set a condition if start is 1 then next number 0 else 1
 */
/**
 *
 * @param {number} n - no of rows
 * @return {string[]} - result
 * Time Complexity : O(n²)
 * Space Complexity: O(n²)
 */
function generateBinaryNumberTrianglePattern(n) {
  let result = [];
  for (let i = 1; i <= n; i++) {
    let line = "";
    let startNo = i % 2 == 0 ? 0 : 1;
    for (let j = 0; j < i; j++) {
      line += startNo;
      startNo = startNo == 0 ? 1 : 0;
    }
    result.push(line);
  }
  return result;
}

const pattern = generateBinaryNumberTrianglePattern(5);
pattern.forEach((line) => console.log(line));


/**
 * Output
1
01
101
0101
10101 
 */