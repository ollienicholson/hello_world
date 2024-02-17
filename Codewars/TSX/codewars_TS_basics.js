"use strict";
//
// Learning TS basics
//
Object.defineProperty(exports, "__esModule", { value: true });
exports.noSpace = exports.var15NeverFunction_1 = exports.var14Undefined_1 = exports.var13Null_1 = exports.var12VoidFunction_1 = exports.var11ArrayOfAny_1 = exports.var10Enum_1 = exports.var9Tuple_1 = exports.var8NumericArray_1 = exports.var7Array_1 = exports.var6String_1 = exports.var5Octal_1 = exports.var4Binary_1 = exports.var3Hex_1 = exports.var2Decimal_1 = exports.var1Boolean_1 = exports.var15NeverFunction = exports.var14Underfined = exports.var13Null = exports.var12VoidFunction = exports.var11ArrayOfAny = exports.var10Enum = exports.var9Tuple = exports.var8NumericArray = exports.var7Array = exports.var6String = exports.var5Octal = exports.var4Binary = exports.var3Hex = exports.var2Decimal = exports.var1Boolean = exports.Color = void 0;
// 1. Learning TS: basic types
var Color;
(function (Color) {
    Color[Color["Red"] = 1] = "Red";
    Color[Color["Green"] = 2] = "Green";
    Color[Color["Blue"] = 4] = "Blue";
})(Color || (exports.Color = Color = {}));
exports.var1Boolean = true;
exports.var2Decimal = 13;
exports.var3Hex = 0xf00d;
exports.var4Binary = 63;
exports.var5Octal = 484;
exports.var6String = "Hello, world!";
exports.var7Array = [1, 'test', { a: 3 }, 4, 5];
exports.var8NumericArray = [1, 2, 3, 4, 5];
exports.var9Tuple = ['key', 12345];
exports.var10Enum = Color.Blue;
exports.var11ArrayOfAny = [1, 'test', { a: 3 }, 4, 5];
var var12VoidFunction = function () { };
exports.var12VoidFunction = var12VoidFunction;
exports.var13Null = null;
exports.var14Underfined = undefined;
// Lance has never used this
var var15NeverFunction = function () { throw new Error(''); };
exports.var15NeverFunction = var15NeverFunction;
//alts
var var12VoidFunction_1 = function () { }, var15NeverFunction_1 = function () { throw new Error(); };
exports.var1Boolean_1 = true, exports.var2Decimal_1 = 13, exports.var3Hex_1 = 0xf00d, exports.var4Binary_1 = 63, exports.var5Octal_1 = 484, exports.var6String_1 = 'Hello, world!', exports.var7Array_1 = [1, 'test', { a: 3 }, 4, 5], exports.var8NumericArray_1 = [1, 2, 3, 4, 5], exports.var9Tuple_1 = ['key', 12345], exports.var10Enum_1 = Color.Blue, exports.var11ArrayOfAny_1 = [1, 'test', { a: 3 }, 4, 5], exports.var12VoidFunction_1 = var12VoidFunction_1, exports.var13Null_1 = null, exports.var14Undefined_1 = undefined, exports.var15NeverFunction_1 = var15NeverFunction_1;
// remove all white space from a string
function noSpace(x) {
    x = x.replace(/\s+/g, '');
    return x;
}
exports.noSpace = noSpace;
var hello = "h e l l o p e  o p   l e";
console.log(noSpace(hello));
