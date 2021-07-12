
let select = document.getElementById("genres"); 
let chosen = document.getElementsByTagName("option")[1]
console.log(select.value)
let newOption = document.createElement('option')  
let newTextNode = document.createTextNode('Classic');
newOption.appendChild(newTextNode)
newOption.setAttribute("value", "classic")
newOption.setAttribute("selected","")
select.appendChild(newOption)
console.log(select.value)

// for (const iterator of select) {
//     if (iterator.hasAttribute("selected"){
//         console.log(iterator.value)
//     } 
// }
// select.addEventListener("submit", changeInput)
// function changeInput(event){
//     // for (const elem of event.target.elements) {
//     //     if (sele){
//     //    console.log( elem.value)
    //     }
//     // }
//     let elem1 = form.elements[0];
//     let elem2 = form.elements[1];
//     console.log(elem1)
//     console.log(elem2)
//     event.preventDefault()
// }