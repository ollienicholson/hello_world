// You need to double the integer and return it.

export const doubleInteger = (i: number): number => i * 2

export function doubleInteger2(i: number): number {
    return i*2;
    // 2137
  }

  // The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).
  // Note! The input is a Real number (actual type is language dependent) and is >= 0. The result should be an Integer.

  export function cockroachSpeed(kmh: number): number {
    const cms: number = kmh * 100000 / 3600;
    return Math.floor(cms);
  }

  // alternatives
  export function cockroachSpeed2(s: number): number{
    return Math.floor(s * 1000 * 100 / 60 / 60);
  }

