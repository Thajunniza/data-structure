console.log("Right Angle Triangle");

/**
 * 
 * @param {number} row 
 * @returns {string[]} result - array of string where each row increment one more '*' than other
 * Time Complexity : O(n²)
 * Space Complexity: O(n²)
 */
function generateRightAngleTriangleArr(row)
{
    let result = [];
    for( let i=0; i<row; i++){
        let rows = '';
        for(let j =0; j<=i; j++){
            rows += '*';
        }
        result.push(rows);
    }
    return result;
}

let patternArr = generateRightAngleTriangleArr(4);
console.log("Right Angle Triangle Array");
patternArr.forEach(data => console.log(data));

/**
 * 
 * @param {number} row 
 * @returns {string} result - String where each row increment one more '*' than other
 * Time Complexity : O(n²)
 * Space Complexity: O(n²)
 */
function generateRightAngleTriangleStr(row)
{
    let result = "";
    for( let i=0; i<row; i++){
        for(let j =0; j<=i; j++){
            result += '*';
        }
        result += "\n";
    }
    return result;
}

let patternStr = generateRightAngleTriangleStr(5);
console.log("Right Angle Triangle String");
console.log(patternStr);


/**
 * Output
Right Angle Triangle
Right Angle Triangle Array
*
**
***
****
Right Angle Triangle String
*
**
***
****
*****
 */




