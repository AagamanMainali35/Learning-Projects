let user = Number(window.prompt("What is your purchase amount?"));
console.log(typeof user);
let result = user > 1000 ? `The discount  amount is is ${user * 0.25} off ${user} and you final price is ${user-(user * 0.25)}` : "No discount for that purchase";
console.log(result);
// a=12
// result=a>=12 ? "true":"false";
// console.log(result);