const numbers = [5,0,9,1,7,4,2,6,3,8];
// console.log(numbers.toString())
// console.log(numbers.join(" "))
// let num = []
// for ( let i of numbers) {
//     if(num = []){
//         num.push(i)
//     }else if (i > num{

//     }
//     num.push(i)
// }
// let ans = ""
// console.log(num)

// for (let i = num.length - 1; i >= 0; i--) {
//    ans.push(i)
// }
// console.log(ans)



// let ans = []
// let num = []
// for (let i = 0; i < numbers.length -1; i++) {
//     for (let p = 1; p < numbers.length -1; p++){
//         if(ans == []){
//             ans.push(numbers[i])
//             console.log(ans)
//         }else if (numbers[p] > ans[0]){
//             ans.pop()
//             ans.push(numbers[p])
//         }
//     }
//     num.push(ans)
// }
// console.log(num)

// let ans = []
// let num = []
// for (let i = 0; i < numbers.length -1; i++) {
//     for (let p = 1; p < numbers.length -1; p++){
//         ans.push[numbers[i]]
//         if (numbers[p] > ans[0]){
//             ans.pop()
//             ans.push(numbers[p])
//         }
//     }
//     num.push(ans)
// }
// console.log(num)
let num = []
let ans = []
for (let i = 0; i < numbers.length -1; i++){
    ans.push(numbers[i])
for (let p = 0; p < numbers.length -1; p++){
    // if(ans.length < 1){
    // ans.push(4)
    // }
     if (numbers[p] < ans[i]){
        ans.pop()
        ans.push(numbers[p])
        
        
    }
    //numbers.splice(numbers.indexOf(ans[i]),1)
}
//console.log(ans)
numbers.splice(numbers.indexOf(ans[i]),1)
}
console.log(ans)