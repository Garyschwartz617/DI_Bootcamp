 fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
 fruits = fruits.slice(1);
fruits.sort();
fruits.push("kiwi");
fruits.splice(0,1)
fruits.reverse();
console.log(fruits);


let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0])
let otherFruits = moreFruits[1]
let ourFruit = otherFruits[1]
console.log(ourFruit)


