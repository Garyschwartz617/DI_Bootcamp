let colors = ["blue", "yellow", "red"];
for (let i in colors) {
     i = parseInt(i)
   console.log(`My number ${i + 1} choice of a color is ${colors[i]}`); 
}

let people = ["Greg", "Mary", "Devon", "James"]
people = people.slice(1,)
console.log(people);
people.splice(2,1,"Jason")
console.log(people);
people.push("Gary")
console.log(people);
for( i of people){
    console.log(i)
}
for (let i=0; i<people.length && people[i - 1] != "Jason"; i++) {
    console.log(people[i]);
}
let peoples = people.slice(1,)
peoples = peoples.slice(0,2)
console.log(peoples);
console.log(people.indexOf("Mary"))
console.log(people.indexOf("Foo"))
var last = people.length - 1
console.log(last)

do
{
    t =0;
    t = prompt('Give me a number more then 10', "your number");
   
}while(t < 10)

let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }
  let signIn = prompt('Your name', "your name");
  if (guestList[signIn]){
      console.log(`Hi! I'm ${signIn}, and I'm from ${guestList[signIn]}.`)
  }else{
      console.log(`Hi! I'm a guest.`)
  }


  let family = {
    father: "Dan",
    mother: "Jamie",
    son: "Gary",
    daughter: "Adina"
  }
  for(i in family){
      console.log(i)
  }
  for(i in family){
    console.log(family[i])
}

let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
  let sentence ="";
  for(i in details){ 
    sentence = sentence.concat(i).concat(" ").concat(details[i]).concat(" ");
  }
  console.log(sentence)

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
names = names.sort()
let password = ""
for(i in names){
    letter = names[i].slice(0,1)
    password = password.concat(letter)
}
console.log(password)