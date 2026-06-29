/**
 * @return {Function}
 */
var createHelloWorld = function() {
    return function(...args) {
        let hel = "Hello World";
        return hel;
    }
};


  const f = createHelloWorld();
  f(); // "Hello World"
 