let alpha = document.querySelectorAll(".alpha")
let alpha1 = document.getElementsByClassName("alpha")[0]
alpha1.addEventListener('dragstart',function(e){
    console.log("start dragin",e.target.id)
})
alpha1.addEventListener('drag',function(e){
    let x = e.clientX
    let y = e.clientY
    console.log(" dragin away",e.target.id,x,y)
})
alpha1.addEventListener('dragend',function(e){
    let x = e.clientX
    let y = e.clientY
    console.log(" drag end",e.target.id,x,y)
    alpha1.style.left = `${x}px`;
    alpha1.style.top = `${y}px`;
})
for (const iterator of alpha) {
    iterator.addEventListener('dragstart',function(e){
            console.log("start dragin",e.target.id)
        })
        iterator.addEventListener('drag',function(e){
            let x = e.clientX
            let y = e.clientY
            console.log(" dragin away",e.target.id,x,y)
        })
    iterator.addEventListener('dragend',function(e){
            let x = e.clientX
            let y = e.clientY
            console.log(" drag end",e.target.id,x,y)
            iterator.style.left = `${x}px`;
            iterator.style.top = `${y}px`;
        })
        
}