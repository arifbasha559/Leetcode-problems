/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
  const maxCandies = Math.max(...candies);  // find the current max
    return candies.map(candy => (candy + extraCandies) >= maxCandies);

};