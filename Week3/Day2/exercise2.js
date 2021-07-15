
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

