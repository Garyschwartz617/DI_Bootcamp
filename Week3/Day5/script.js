let box = document.getElementById("box")
let x = "*"

for (let index = 0; index < 49; index++) {
    let newDiv = document.createElement('div')
    if(index == 2 || index == 3 || index == 4 ||index == 8 ||index == 12 ||index == 15 ||index == 19 ||index == 22 ||index == 23 ||index == 24 ||index == 25 ||index == 26 ||index == 29 ||index == 33 ||index == 36 ||index == 40 ||index == 43 ||index == 47 ){
    let newTextNode = document.createTextNode("*");
    newDiv.appendChild(newTextNode)
    }
    box.appendChild(newDiv)    
}
