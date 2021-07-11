let planets = ["mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
let colors = ["red","blue","green","yellow","brown","lightblue","white","pink"]

for (let index = 0; index < planets.length; index++) {
    const element = planets[index];
    let newDiv = document.createElement('div')  
    let newTextNode = document.createTextNode(element);
    newDiv.appendChild(newTextNode)
    newDiv.classList.add("planet","planetColor")
    let section = document.querySelector("section")
    section.appendChild(newDiv)
}
let planetColor = document.getElementsByClassName("planetColor")
for (let index = 0; index < planetColor.length; index++) {
    planetColor[index].style.background = colors[index]
    
}