let form = document.forms[0]; 
form.addEventListener("submit", changeInput)

function changeInput(event){
   for (let index = 0; index < form.length -1 ; index++) {
       
       if (form.elements[index].value == ""){
           return
       }
   }
    let elem1 = form.elements[0];
    let elem2 = form.elements[1];
    let elem3 = form.elements[2];
    let elem4 = form.elements[3];
    let elem5 = form.elements[4];
    let p = document.getElementsByTagName("p")[0]
    let newTextNode = document.createTextNode(`I was with my ${elem1.value} when suddenly the ${elem2.value} ${elem1.value} hit me over the head. But really my friend ${elem3.value} was playing a joke on me. So we both went ${elem4.value} at the ${elem5.value}`);
    p.appendChild(newTextNode)
    event.preventDefault()
}