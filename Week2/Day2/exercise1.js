let x = 2;
let y = 2;
if(x > y){
    console.log(`X is bigger`);
}else if (y > x){
    console.log(`Y is bigger`);
}else{
    console.log(`They are equal`);
}


let newDog = "Chihuahua";
console.log(newDog.length);
console.log(newDog.toLowerCase());
console.log(newDog.toUpperCase());
if(newDog = "Chihuahua"){
    console.log(`I love Chihuahuas, it’s my favorite dog breed`);
}else{
    console.log(`I dont care, I prefer cats`);
}


let nmbr = prompt('What is your number?', 'Number');

if(nmbr % 2 == 0){
    console.log(`this number is even`);
}else{
    console.log(`this number is odd`);
}

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
if (users.length == 0){
    console.log("no one is online");
}else if (users.length == 1){
    console.log(`${users[0]} is online`);
}else if (users.length == 2){
    console.log(`${users[0]} and ${users[1]} are online`);
}else if (users.length >= 3){
    console.log(`${users[0]}, ${users[1]} and ${users.length - 2} are online`);
}