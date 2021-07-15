let listTasks = [];
let x = 0;
let form = document.forms[0]; 
let submit = document.getElementById("butt")
let lists = document.getElementById("lists")
submit.addEventListener("click",addTask)
console.log(form.elements[0])
function addTask(e){
    if(form.elements[0].value == ""){
        e.preventDefault()
    } else{
        e.preventDefault()
        console.log(form.elements[0].value)
        listTasks[x] = form.elements[0].value
        console.log(listTasks)
            const element = listTasks[x];
            let newDiv = document.createElement('div') 
            let newTextNode = document.createTextNode(element);
            let y = document.createElement('input') 
            y.setAttribute("type", "checkbox")
            newDiv.appendChild(y)
            newDiv.appendChild(newTextNode)
            lists.appendChild(newDiv)
            x++
    }
}
for (let index = 0; index < listTasks.length; index++) {
    const element = listTasks[index];
    let newDiv = document.createElement('div') 
    let newTextNode = document.createTextNode(element);
    newDiv.appendChild(newTextNode)
    lists.appendChild(newDiv)    
}