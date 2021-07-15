let colorType = ["red", "orange", "green", "blue", "yellow", "brown", "black", "white", "lightblue", "purple", "darkgreen", "cyan", "coral", "grey", "pink", "goldenrod", "indigo", "lime", "maroon", "navy", "salmon"]
let palet = document.getElementsByClassName("palet")[0]
let canvas = document.getElementsByClassName("canvas")[0]
let button = document.getElementsByClassName("butt")[0]

let colVar = ""
let mouse = false;
for (let index = 0; index < colorType.length; index++) {
    const element = colorType[index];
    let newDiv = document.createElement('div')
    let newTextNode = document.createTextNode(element);
    newDiv.appendChild(newTextNode)
    newDiv.style.backgroundColor = element;
    newDiv.classList.add("color")
    palet.appendChild(newDiv)
    newDiv.addEventListener("click", saveColor)
}

for (let index = 0; index < 1440; index++) {
    let newDiv = document.createElement('div')
    newDiv.style.border = "solid gray .2px";
    canvas.appendChild(newDiv)
    newDiv.addEventListener("click", assignColor)
    newDiv.addEventListener("mousedown", function () {
        mouse = true;
    })
    newDiv.addEventListener("mouseup", function () {
        mouse = false;
    })
    newDiv.addEventListener("mouseover", function (e) {
        if (mouse) {
            assignColor(e)
        } 
    })
    button.addEventListener("click", clearAll)
    function clearAll(e) {
        newDiv.style.backgroundColor = "white"
    }
}
function hoverColor(e) {
    newDiv.addEventListener("mouseover", assignColor)
}
function saveColor(e) {
    let y = e.target
    colVar = y.style.backgroundColor
}

function assignColor(e) {
    let y = e.target
    y.style.backgroundColor = colVar
}