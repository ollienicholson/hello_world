"use strict";
// Your task is to create a function that does four basic mathematical operations.
Object.defineProperty(exports, "__esModule", { value: true });
exports.countPositivesSumNegatives_2 = exports.countPositivesSumNegatives = exports.basicOp_2 = exports.basicOp = void 0;
// The function should take three arguments - operation(string/char), value1(number), value2(number).
// The function should return result of numbers after applying the chosen operation.
function basicOp(operation, value1, value2) {
    switch (operation) {
        case "+":
            return value1 + value2;
        case "-":
            return value1 - value2;
        case "*":
            return value1 * value2;
        case "/":
            return value1 / value2;
        default:
            return 0;
    }
}
exports.basicOp = basicOp;
// alts
var ops = {
    "+": function (l, r) { return l + r; },
    "-": function (l, r) { return l - r; },
    "*": function (l, r) { return l * r; },
    "/": function (l, r) { return l / r; },
};
var basicOp_2 = function (operation, value1, value2) { return ops[operation](value1, value2); };
exports.basicOp_2 = basicOp_2;
// Given an array of integers.
// Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
// If the input is an empty array or is null, return an empty array.
function countPositivesSumNegatives(input) {
    //   if input = null or input = 0
    if (!input || input.length === 0) {
        return [];
    }
    //   set variables = 0
    var countPositives = 0;
    var sumNegatives = 0;
    //   run a for loop
    for (var _i = 0, input_1 = input; _i < input_1.length; _i++) {
        var num = input_1[_i];
        if (num > 0) {
            //   add an accumulator for counting positives
            countPositives += 1;
        }
        else if (num < 0) {
            //   add an accumulator for summing negatives
            sumNegatives += num;
        }
    }
    return [countPositives, sumNegatives];
}
exports.countPositivesSumNegatives = countPositivesSumNegatives;
var exampleArr = [1, 2, 3, 4, -5];
var result = countPositivesSumNegatives(exampleArr);
//  that works!
console.log("heres your result -", result);
// alts
function countPositivesSumNegatives_2(input) {
    if (!input || input.length === 0) {
        return [];
    }
    var _a = input.reduce(function (_a, num) {
        var count = _a[0], sum = _a[1];
        if (num > 0) {
            count += 1;
        }
        else if (num < 0) {
            sum += num;
        }
        return [count, sum];
    }, [0, 0]), countPositives = _a[0], sumNegatives = _a[1];
    return [countPositives, sumNegatives];
}
exports.countPositivesSumNegatives_2 = countPositivesSumNegatives_2;
var result_2 = countPositivesSumNegatives_2(exampleArr);
console.log("heres your result -", result_2);
// Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them. Capitalise the first letter of each word.
function func(input) {
    return input
        .split(" ")
        .map(function (word) { return word.charAt(0).toUpperCase() + word.slice(1); })
        .join(" ");
}
var text = "this is a sentence";
var read_this = func(text);
console.log(read_this, " - - read this");
