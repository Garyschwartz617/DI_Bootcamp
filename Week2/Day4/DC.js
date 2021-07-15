let words = prompt('Words seperated by commas', 'hello,world,in,a,frame');

function wor(words){
    const myArr = words.split(",");
    let len = "";
    let x ="*"
    for (const iterator of myArr) {
        if(len == ""){
           len = iterator;
        } else if(len.length < iterator.length){
            len = iterator;
        }
    }
    for (const iterator of myArr) {
        let y = " "
        let q = len.length  - iterator.length
        let f = y.repeat(q)
        console.log(`${x} ${iterator}${f} ${x}`)
    }
}

function border(words){
    const myArr = words.split(",");
    let w = "";
    for (const iterator of myArr) {
        if(w == ""){
           w = iterator;
        } else if(w.length < iterator.length){
            w = iterator;
        }
    }
    let sum = w.length
    let x = "*"
    console.log(x.repeat(sum+4))
    wor(words)
    console.log(x.repeat(sum+4))
}
border(words)

