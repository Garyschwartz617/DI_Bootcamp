let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
let fruit = fruits.slice(1);
fruit.sort();
fruit.push("kiwi");
fruit.splice(0,1)
fruit.reverse();
console.log(fruit);


let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
let otherFruits = moreFruits[1]
let ourFruit = otherFruits[1]
console.log(ourFruit)


