"""
function tripler(array) {
    const result = [];
    // return a new array
    // iterate through the array passed in x
    console.log('Inside of tripler function');
    for (let i = 0; i < array.length; i++) {
        let num = array[i]; // 3
        let multiple = num * 3; // 9
        result.push(multiple); // [3, 6, 9]
    }
    // multiply each element by 3
    // push that element into my result
    // return result x
    
    return result;
}

console.log(tripler([1,2,3]))
console.log(tripler([4, 1, 7]));
"""

def tripler(array):
    result = []
    for i in range(len(array)):
        num = array[i]
        multiple = num * 3
        result.append(multiple)
    return result

print(tripler([1,2,3]))
print(tripler([4,1,7]))