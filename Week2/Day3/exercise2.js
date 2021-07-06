let building = {
    numberLevels : 4,
    numberOfAptByLevel : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        "Sarah": [3, 990],
        "Dan":  [4, 1000],
        "David": [1, 500],
    },
}
console.log(building["numberLevels"])
console.log(building["numberOfAptByLevel"]["1"],building["numberOfAptByLevel"]["3"])
console.log(building["nameOfTenants"][1],building["numberOfRoomsAndRent"]["Dan"][0])
console.log(building["numberOfRoomsAndRent"]["Sarah"][1],building["numberOfRoomsAndRent"]["David"][1])
if(building["numberOfRoomsAndRent"]["Sarah"][1] + building["numberOfRoomsAndRent"]["David"][1] > building["numberOfRoomsAndRent"]["Dan"][1]){
    building["numberOfRoomsAndRent"]["Dan"][1] = 2000
}
console.log(building["numberOfRoomsAndRent"]["Dan"][1])

let numbers = [123, 8409, 100053, 333333333, 7]
for(i in numbers){
    if(numbers[i] % 3 == 0){
        console.log(`${numbers[i]}  is divisable by 3`)
    }else {
        console.log(`${numbers[i]}  is not divisable by 3`)
    }
}

let age = [20,5,12,43,98,55];
let total = 0;
for(i of age) {
    total += i;
}
console.log(total)
let heighest = 0;
for(i of age){
    while(i >heighest){
        heighest = i;
    }
}
console.log(heighest)


let object = {
    firstName: "gary",
    lastName: "schwartz",
    number: "17"
}

object.firstName
console.log(typeof age)
