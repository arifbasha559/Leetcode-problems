/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
  function gcd(a, b) {
        return b === 0 ? a : gcd(b, a % b);
    }

    // If they don’t form the same repeated pattern → no gcd
    if (str1 + str2 !== str2 + str1) return "";

    // Otherwise gcd of lengths gives the answer
    let len = gcd(str1.length, str2.length);
    return str1.substring(0, len);
};