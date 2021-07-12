// Question1
let article = document.getElementsByTagName("article")[0]
let lastart = document.getElementsByTagName("p")[3]
article.removeChild(lastart)
let h2 = document.getElementsByTagName("h2")[0]
h2.addEventListener("click",changeColor)
function changeColor(event){
    event.target.style.background = "red"
}
let h1 = document.getElementsByTagName("h1")[0]
function changeFont(){
   let rand = Math.floor(Math.random() * 101);
   h1.style.fontSize = `${rand}px`;
} 
changeFont()
let h3 = document.getElementsByTagName("h3")[0]
h3.addEventListener("click",disapear)
function disapear(){
    h3.style.display = "none";
}
let p = document.getElementsByTagName("p")
let button = document.getElementsByTagName("button")[0]
button.addEventListener("click",bold)
function bold(){
    for (const i of p) {
        i.style.fontWeight = "bold";
    }
}
let form = document.forms[0]; 
form.addEventListener("submit", changeInput)

function changeInput(event){
    for (const elem of event.target.elements) {
        if(elem.value == ""){
            return
        }
        else if (elem.name == 'fname' || elem.name == 'lname'){
            let newTextNode = document.createTextNode(elem.value);
            let div = document.getElementsByTagName("div")[0]
            div.appendChild(newTextNode)
       console.log( elem.value)
        }
    }
    event.preventDefault()
}
h2.addEventListener("mouseover",fade)
function fade(){
    h2.style.opacity= "0.5"
}

// // Question 2
// let strong = document.getElementsByTagName("strong")
// function getBold_items(){
//     for (const iterator of strong) {
//         console.log(iterator.textContent)
//     }
// }
// getBold_items()
// function highlight() {
//     for (const iterator of strong) {
//         iterator.style.color = "blue"
//     }
// }
// highlight()
// function return_normal() {
//     for (const iterator of strong) {
//         iterator.style.color = "black"
//     }
// }
// return_normal()
// let strong1 = document.getElementsByTagName("strong")[0]
// strong1.addEventListener("mouseover",highlight)
// strong1.addEventListener("mouseout",return_normal)
// let strong2 = document.getElementsByTagName("strong")[1]
// strong2.addEventListener("mouseover",highlight)
// strong2.addEventListener("mouseout",return_normal)
// let strong3 = document.getElementsByTagName("strong")[2]
// strong3.addEventListener("mouseover",highlight)
// strong3.addEventListener("mouseout",return_normal)
// let strong4 = document.getElementsByTagName("strong")[3]
// strong4.addEventListener("mouseover",highlight)
// strong4.addEventListener("mouseout",return_normal)
// let strong5 = document.getElementsByTagName("strong")[4]
// strong5.addEventListener("mouseover",highlight)
// strong5.addEventListener("mouseout",return_normal)
// let strong6 = document.getElementsByTagName("strong")[5]
// strong6.addEventListener("mouseover",highlight)
// strong6.addEventListener("mouseout",return_normal)

// // question 3 and 4
// let form = document.forms[0]; 
// form.addEventListener("submit", changeInput)
// function changeInput(event){
//     sum = 0
//     let elem1 = form.elements[0];
//     sum = 4/3 * 3.14 *(elem1.value* elem1.value* elem1.value)
//     form.elements[1].value = `${sum}`
//     console.log(sum)
    
//     event.preventDefault()
// }

// // question 4
// let p = document.getElementsByTagName("p")[0]
// p.addEventListener("keyup",colorchange)
// function colorchange(){
//     p.style.color = "red";
// }
// p.addEventListener("keydown",fontsize)
// function fontsize(){
//     p.style.fontsize = "30px";
// }
// p.addEventListener("mouseout",fontsize)
// function fontsize(){
//     p.style.opacity = "1";
// }
// p.addEventListener("mouseover",fade)
// function fade(){
//     p.style.opacity= "0.5"
// }
