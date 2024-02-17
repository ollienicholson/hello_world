//
// Learning TS basics
//

// 1. Learning TS: basic types
export enum Color {
  Red = 1,
  Green = 2,
  Blue = 4,
}
export const var1Boolean: boolean = true;
export const var2Decimal: number = 13;
export const var3Hex: number = 0xf00d;
export const var4Binary: number = 0b111111;
export const var5Octal: number = 0o744;
export const var6String: string = "Hello, world!";
export const var7Array: any[] = [1, "test", { a: 3 }, 4, 5];
export const var8NumericArray: number[] = [1, 2, 3, 4, 5];
export const var9Tuple: [string, number] = ["key", 12345];
export const var10Enum: Color = Color.Blue;
export const var11ArrayOfAny: Array<any> = [1, "test", { a: 3 }, 4, 5];
export const var12VoidFunction = (): void => {};
export const var13Null: null = null;
export const var14Underfined: undefined = undefined;

// Lance has never used this
export const var15NeverFunction = (): never => {
  throw new Error("");
};

//alts
export var var1Boolean_1: boolean = true,
  var2Decimal_1: number = 13,
  var3Hex_1: number = 0xf00d,
  var4Binary_1: number = 0b111111,
  var5Octal_1: number = 0o744,
  var6String_1: string = "Hello, world!",
  var7Array_1: any[] = [1, "test", { a: 3 }, 4, 5],
  var8NumericArray_1: Array<number> = [1, 2, 3, 4, 5],
  var9Tuple_1: [string, number] = ["key", 12345],
  var10Enum_1: Color = Color.Blue,
  var11ArrayOfAny_1: Array<any> = [1, "test", { a: 3 }, 4, 5],
  var12VoidFunction_1 = function (): void {},
  var13Null_1: null = null,
  var14Undefined_1: undefined = undefined,
  var15NeverFunction_1 = function (): never {
    throw new Error();
  };

// remove all white space from a string
export function noSpace(x: string): string {
  x = x.replace(/\s+/g, "");
  return x;
}
// alts
export function noSpace_1(x: string): string {
  return x.replace(/\s/g, "");
}

export const noSpace_2 = (x: string) => x.split(" ").join("");

// Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
export const summation = (num: number) => {
  return (num * (num + 1)) / 2;
};
// alts
export const summation_1 = (num: number) => (num * (num + 1)) / 2;

// Write a function findNeedle() that takes an array full of junk but containing one "needle"
export function findNeedle(haystack: any[]): string {
  const index: number = haystack.indexOf("needle");
  return "found the needle at position " + index.toString();
}

// alts
export function findNeedle_2(haystack: any[]): string {
  return "found the needle at position " + haystack.indexOf("needle");
}

export function findNeedle_3(haystack: any[]): string {
  return `found the needle at position ${haystack.indexOf("needle")}`;
}
