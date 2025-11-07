console.log("Right Angle Numbered Pyramid");

/**
 * @param {number} rows - No of rows need to printed
 * @returns {string[] } result - Array of strings where each row with seq of numbers increasing
 * Time Complexity : O(n²)
 * Space Complexity : O(n²)
 */
function generateRightAngleNumPyramidArr(rows){
    let result = [];
    for(let i=1;i<=rows;i++){
        let line = "";
        for(let j=1;j<=i;j++){
            line += j; 
        }
        result.push(line);
    }
    return result;
}

const patternArr = generateRightAngleNumPyramidArr(4);
console.log("Right Angle Numbered Pyramid Array");
patternArr.forEach(row => console.log(row));

/**
 * @param {number} rows - No of rows need to printed
 * @returns {string } result - String where each row with seq of numbers increasing
 * Time Complexity : O(n²)
 * Space Complexity : O(n²)
 */
function generateRightAngleNumPyramidStr(rows){
    let result = "";
    for(let i=1;i<=rows;i++){
        for(let j=1;j<=i;j++){
            result += j; 
        }
        result += '\n';
    }
    return result.trim();
}

const patternStr = generateRightAngleNumPyramidStr(5);
console.log("Right Angle Numbered Pyramid String");
console.log(patternStr);

/**
 * Output
 Right Angle Numbered Pyramid
Right Angle Numbered Pyramid Array
1
12
123
1234
Right Angle Numbered Pyramid String
1
12
123
1234
12345
 */