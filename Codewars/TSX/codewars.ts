// You need to double the integer and return it.

export const doubleInteger = (i: number): number => i * 2;

export function doubleInteger2(i: number): number {
  return i * 2;
  // 2137
}

// The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).
// Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

export function cockroachSpeed(kmh: number): number {
  const cms: number = (kmh * 100000) / 3600;
  return Math.floor(cms);
}

// alternatives
export function cockroachSpeed2(s: number): number {
  return Math.floor((s * 1000 * 100) / 60 / 60);
}

// Clock shows h hours, m minutes and s seconds after midnight.
//Your task is to write a function which returns the time since midnight in milliseconds.

export function past(h: number, m: number, s: number): number {
  let hrs = h * 60 * 60 * 1000;
  let mins = m * 60 * 1000;
  let secs = s * 1000;
  let final = hrs + mins + secs;
  return final;
}

//alternatives
const seconds = (s: number) => s * 1000;
const minutes = (m: number) => m * seconds(60);
const hours = (h: number) => h * minutes(60);

export function past_2(h: number, m: number, s: number): number {
  return hours(h) + minutes(m) + seconds(s);
}

export function past_3(h: number, m: number, s: number): number {
  return (h * 3600 + m * 60 + s) * 1000;
}

export function past_4(h: number, m: number, s: number): number {
  h = h * 60 * 60 * 1000;
  m = m * 60 * 1000;
  s = s * 1000;
  return +(h + m + s);
}

export const past_5 = (h: number, m: number, s: number): number =>
  (h * 3600 + m * 60 + s) * 1000;

// return the correct boolean for setAlarm depending on if youre employed and/or on vacation
export function setAlarm(employed: boolean, vacation: boolean) {
  if (employed == true && vacation == false) {
    return true;
  } else return false;
}

export function setAlarm2(employed: boolean, vacation: boolean) {
  return employed && !vacation;
}

export const setAlarm3 = (employed: boolean, vacation: boolean) =>
  employed && !vacation;

// feasts of beasts:
//All of the animals are having a feast! Each animal is bringing one dish. There is just one rule: the dish must start and end with the same letters as the animal's name. For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.

// Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.

// Assume that beast and dish are always lowercase strings, and that each has at least two letters. beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numerals.

export function feast(beast: string, dish: string): boolean {
  return (
    beast[0] === dish[0] && beast[beast.length - 1] === dish[dish.length - 1]
  );
}

//alts
export function feast_2(beast: string, dish: string): boolean {
  return beast[0] === dish[0] && beast.slice(-1) === dish.slice(-1);
}

const first = (str: string) => str.charAt(0);
const last = (str: string) => str.charAt(str.length - 1);
export const feast_3 = (beast: string, dish: string) =>
  first(beast) === first(dish) && last(beast) === last(dish);

// Very simple, given an integer or a floating-point number, find its opposite.
export class Kata {
  static opposite(n: number) {
    return -1 * n;
  }
}

// alts
export class Kata_2 {
  static opposite = (n) => -n;
}

// Define.toAlternatingCase such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example: toAlternatingCase("HeLLo WoRLD") === "hEllO wOrld"

export function toAlternatingCase(s: string): string {
  return s
    .split("")
    .map((char) => {
      return char === char.toUpperCase()
        ? char.toLowerCase()
        : char.toUpperCase();
    })
    .join("");
}

// Write a function which calculates the average of the numbers in a given list.
// Note: Empty arrays should return 0.
export function findAverage(array: number[]): number {
  if (array.length === 0) {
    return 0;
  }
  const sum = array.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    0
  );
  return sum / array.length;
}

//alts
export function findAverage_2(array: number[]): number {
  return !array.length ? 0 : array.reduce((a, b) => a + b, 0) / array.length;
}

export function findAverage_3(array: number[]): number {
  if (array.length === 0) {
    return 0;
  }
  return array.reduce((prev, curr) => prev + curr, 0) / array.length;
}

// Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

export function smash(words: string[]): string {
  return words.join(" ");
}

// alts
export const smash_2 = (words: string[]): string => words.join(" ");
