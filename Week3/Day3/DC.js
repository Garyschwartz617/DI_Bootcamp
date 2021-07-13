let word = document.getElementById('letters')

 word.addEventListener('keydown',onlyLetters)
 function onlyLetters(event){
     if(/[A-z]/i.test(event.key) ){
     }else{
        event.preventDefault()
     }
 }
// let str = ""
// function onlyLetters(e){
//     // console.log(word.value)
//     // let patt2 = /\W/
//     // let patt = /[A-z]/;
//     // if( word.value == patt){
//     //     word.value = word.value
//     // }else{
//     //     word.value = ""
//     // }
//     // let patt = /[A-z]/;
//     // let result = word.value.matches(patt)
//     // let result = patt.exec(word).value
//     // word.value = result
//     // let wor = word.value
//     // let num = e.keycode
//     var x = e.which || e.keyCode;
//     // console.log(x)
//     // console.log(e)
//     console.log(word.value)
//     // str = str + word.value

//     // let str = word.value
//     // console.log(str.length)
//     // str.slice(0,2)
//     // console.log(str.length)
//     // console.log(str)
//     // for (let index = 0; index < str.length; index++) {
//     //     // const element = str[index];
//     //     // console.log(element)
//     //     // var x = e.which || e.keyCode;
//     //     if ( x <=65 || x >= 122){
//     //         console.log(x)
//     //         str.slice(0,index)
//     //     }
//     // }
//     // word.value = str
//     // checkWord(word.value)
//     // let y = checkWord(word.value)
//     // console.log(y)
//     // let y =word.value = y

//     let z = word.value
//     if (x <=65 || x >= 122){
//         console.log(z.length)
//         z.substring(0,z.length-1)
//         console.log(z)
//         word.value = z
//     }

//     // if (x <=65 || x >= 122){
//     //     wor
//     //     // str = str + word.value
//     //     console.log(str.length)
//     // }else{
//     //     out.value = word.value;
//     // }
//     // out.value = word.value;
// }

// function checkWord(str){
//     for (let index = 0; index < str.length; index++) {
//         const element = str[index];
//         var x = e.which || e.keyCode;
//         if ( x <=65 || x >= 122){
//             console.log(x)
//             str.slice(0,index)
//         }
//     }
// return str
        
    
// }