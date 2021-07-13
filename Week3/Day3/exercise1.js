// exercise 1
// let left = 0;
// let rbox = document.getElementById('animate')
// function myMove(){
//    x = setInterval(function(){
//         if(left <= 350){
//         left += 1
//         rbox.style.left =`${left}px`
//         } else{
//         }
//     },10)
// }

//exercise 2
let sbox = document.getElementById('move')
let bbox = document.getElementById('bigBox')

sbox.addEventListener('dragstart',dragst)
bbox.addEventListener('drop',drop)
bbox.addEventListener('dragover', drago)
function drago(e){
    e.preventDefault()
}
function dragst(e){
    e.dataTransfer.setData('text',e.target.id)
}
function drop(e){
    e.preventDefault()
    bbox.style.background = "red"
    let x = e.dataTransfer.getData('text')
    e.target.appendChild(document.getElementById(x))
}