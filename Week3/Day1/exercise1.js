// // first problem
// let newid = document.getElementById("navBar")
// newid.setAttribute("id","socialNetworkNavigation")
// let newLi = document.createElement('li')
// let newTextNode = document.createTextNode('Logout');
// // newLi.innerHTML = "logout"
// newLi.appendChild(newTextNode)
// let ul =document.querySelector("ul");
// ul.appendChild(newLi)

// // 2nd problem
// document.body.children[1].lastElementChild.textContent = "Richard"
// document.body.children[1].firstElementChild.textContent = "Gary"
// document.body.children[2].firstElementChild.textContent = "Adina"
// let firstLi = document.querySelectorAll("ul")
// console.log(firstLi)
// for (let index = 0; index < firstLi.length; index++) {
//     let newLi = document.createElement('li')  
//     let newTextNode = document.createTextNode('Hey Students');
//     newLi.appendChild(newTextNode)
//     const element = firstLi[index];
//     element.appendChild(newLi)
//     console.log(element) 
// }
// let sarah = document.body.children[2].firstElementChild.nextElementSibling 
// let parent = document.body.children[2]
// parent.removeChild(sarah);

//3rd problem
// let div = document.getElementsByTagName("div")[0]
let div = document.querySelector("div")
div.style.background = "lightblue";
div.style.padding = "3px";
let john = document.body.children[1].firstElementChild
let parent = document.body.children[1]
parent.removeChild(john);
let pete = document.body.children[1].firstElementChild
pete.style.border = "3px solid black"
document.body.style.fontSize = "50px"

