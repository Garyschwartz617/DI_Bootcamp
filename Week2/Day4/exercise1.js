// function infoAboutMe(){
//     console.log(`hi im gary I'm 27 and like having fun`)
// }
// infoAboutMe()

// function infoAboutPerson(personName, personAge, personFavoriteColor,personHobbies){
//     console.log(`your name is ${personName}, you are ${personAge} years old and your favorite color is ${personFavoriteColor}`)
//     for(let i of personHobbies){
//         console.log(`i like to play ${i}`)
//     }
// }
// // infoAboutPerson("David", 45, "blue")
// // infoAboutPerson("Josh", 12, "yellow")
// infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])

// // Number 2
// let age2 = prompt('What is your age?', 'age');
// function checkDriverAge(age){
//     if (age2 < 18) {
//         alert(`Sorry, you are too young to drive this car. Powering off`)
//     }else if (age2 == 18){
//         alert(`Congratulations on your first year of driving. Enjoy the ride!`)
//     }else{
//         alert(`You are old enough to drive, Powering On. Enjoy the ride!`)
//     }
// }
// checkDriverAge(age2)

// //number3
// function checkNumber(){
//     for (let i = 0; i <= 100; i++) {
//         if(i % 2 == 0){
//             console.log(`${i} is even`)
//         }else{
//             console.log(`${i} is odd`)
//         }
//     }
// }
// checkNumber()

//number4
// function isDivisible(){
//     let sum = 0;
//     for (let i = 0; i <= 500; i++) {
//         if(i % 23 == 0){
//             console.log(`${i} is divisable`)
//             sum += i
//         }
//     }
//     return sum;
// }
// let sum = isDivisible()
// console.log(sum)

// function isDivisible(arg){
//     let sum = 0;
//     for (let i = 0; i <= 500; i++) {
//         if(i % arg == 0){
//             console.log(`${i} is divisable`)
//             sum += i
//         }
//     }
//     return sum;
// }
// let sum = isDivisible(3)
// console.log(sum)
// let summ = isDivisible(45)
// console.log(summ)

// //number5
// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }
// let item = prompt('your item?', 'item');
// function checkBasket(item){
//     for (const key in amazonBasket) {
//         if (key == item){
//             alert (`${item} is in your basket`)
//             return
//         }else{
           
//         }
//     }
//     alert (`${item} is NOT in your basket`)
// }
// let check = checkBasket(item);

// //number6
// let amount = {
//     Quarters : 0.25,
//     Dimes : 0.10,
//     Nickels : 0.05,
//     Pennies : 0.01
// }
// function changeEnough(arr, total){
//     let sum = 0;
//     let i = 0;
//     console.log(sum)
//     for (const key in amount) {
//         sum = sum + (amount[key] * arr[i])
//         i = i + 1;
//     }  
//     if( sum > total){
//         return true;
//     }else {
//         return false;
//     }
// }
// console.log(changeEnough([2, 100, 0, 0], 14.11))
// console.log(changeEnough([0, 0, 20, 5], 0.75))

// //number7
// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  
// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// }
// let shoppingList = ["banana","orange","apple"]
// function myBill(){
//     let sum = 0;
//     for (const key in stock) {
//         for (const x in shoppingList) {
//             if(key == shoppingList[x] && stock[key] != 0){
//                 sum = sum + prices[key]
//             }
//         }
//     }
//     return sum;
// }
// let total = myBill()
// console.log(total)

// //number8
// function tip(amount){
//     let tip = 0;
//     if(amount < 50){
//         tip = amount * .2
//     } else if(amount < 200){
//         tip = amount * .15
//     } else{
//         tip = amount * .15
//     }
//     amount = amount + tip
//     let both = {
//         totTip : tip,
//         bill : amount 
//     }
//     return both;
// }
// let all = tip(170);
// console.log(all.totTip,all.bill)

//number9
let nights2 = prompt('How many nights you staying?', 'number');
function hotelCost(nights) {
    console.log(isNaN(nights))
    if (isNaN(nights)) {
        alert(`This is not a number`);
        let nights3 = prompt('How many nights you staying?', 'number');
        return hotelCost(nights3)
    }else{
    let cost = nights * 140;
    return cost;
    }
}
let cost = hotelCost(nights2)
console.log(cost)

let destination2 = prompt('Where are you staying?', 'place');
function planeRideCost(destination) {
    if (destination) {
        if (destination == "London") {
            return 183
        } else if (destination == "Paris") {
            return 220
        } else {
            return 300
        }
    } else {
        let destination2 = prompt('Where are you staying?', 'place')
        return planeRideCost(destination2)
    }
}
let dest =planeRideCost(destination2)
console.log(dest)

let rental2 = prompt('How many days of renting a car?', 'number');
function rentalCarCost(rental) {
    let sum = 0;
    if (!rental || isNaN(rental)) {
        alert(`This is not a number`);
        let rental3 = prompt('How many days of renting a car?', 'number');
        return rentalCarCost(rental3)
    }else if (rental <= 10){
        sum = 40 * rental;
        return sum;
    } else{
        sum = 40 * rental;
        sum = sum * .95
        return sum;
    }
}
let rentals =rentalCarCost(rental2)
console.log(rentals)

function totalVacationCost(){
    let sum = rentals + cost + dest
    console.log( `The car cost is$${rentals}, the hotel cost$${cost}, the plane ride is $${dest}. Total cost is $${sum}`)
}
totalVacationCost()