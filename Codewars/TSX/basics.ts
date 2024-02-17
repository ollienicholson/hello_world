// Your task is to create a function that does four basic mathematical operations.

// The function should take three arguments - operation(string/char), value1(number), value2(number).
// The function should return result of numbers after applying the chosen operation.

export function basicOp(
  operation: string,
  value1: number,
  value2: number
): number {
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

// alts
const ops = {
  "+": (l, r) => l + r,
  "-": (l, r) => l - r,
  "*": (l, r) => l * r,
  "/": (l, r) => l / r,
};
export const basicOp_2 = (
  operation: keyof typeof ops,
  value1: number,
  value2: number
): number => ops[operation](value1, value2);

// Given an array of integers.
// Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

// If the input is an empty array or is null, return an empty array.
export function countPositivesSumNegatives(input: any) {
  //   if input = null or input = 0
  if (!input || input.length === 0) {
    return [];
  }
  //   set variables = 0
  let countPositives = 0;
  let sumNegatives = 0;

  //   run a for loop
  for (const num of input) {
    if (num > 0) {
      //   add an accumulator for counting positives
      countPositives += 1;
    } else if (num < 0) {
      //   add an accumulator for summing negatives
      sumNegatives += num;
    }
  }

  return [countPositives, sumNegatives];
}

const exampleArr = [1, 2, 3, 4, -5];

const result = countPositivesSumNegatives(exampleArr);
//  that works!
console.log("heres your result -", result);

// alts
export function countPositivesSumNegatives_2(
  input: number[] | null
): [number, number] | [] {
  if (!input || input.length === 0) {
    return [];
  }

  const [countPositives, sumNegatives] = input.reduce(
    ([count, sum], num) => {
      if (num > 0) {
        count += 1;
      } else if (num < 0) {
        sum += num;
      }
      return [count, sum];
    },
    [0, 0]
  );

  return [countPositives, sumNegatives];
}

const result_2 = countPositivesSumNegatives_2(exampleArr);
console.log("heres your result -", result_2);

// Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them. Capitalise the first letter of each word.

function func(input: string): string {
  return input
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
}

const text = "this is a sentence";
const read_this = func(text);
console.log(read_this, " - - read this");

// in the case of codewars IDE - this works
String.prototype.toJadenCase = function (): string {
  // you have to replace 'input' with 'this'
  return this.split(" ")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(" ");
};

interface String {
  // Declaration needed, don't remove it
  toJadenCase(): string;
}
