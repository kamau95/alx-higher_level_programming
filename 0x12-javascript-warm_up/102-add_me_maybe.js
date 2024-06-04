#!/usr/bin/node
exports.addMeMaybe = function (nb, theFunction) {
  theFunction(++nb);
};
