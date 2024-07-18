let amount = Number(window.prompt("What is your purchase amount?"));
switch(true) {
    case amount<10000:
        console.log(`Case 1: The discounted amount is $${0.10 * amount} off ${amount}`);
        break;
    case amount<5000:
        console.log(`Case 2: The discounted amount is $${0.06 * amount} off ${amount}`);
        break;
    case amount<2000:
        console.log(`Case 3: The discounted amount is $${0.02 * amount} off ${amount}`);
        break;
    default:
        console.log(`Default: No discount available`);
}
