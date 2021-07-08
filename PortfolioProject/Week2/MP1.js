function playTheGame(){
    if(!confirm("Press a button!")){
        return alert(`No problem, Goodbye`)
    }else{
        var person = prompt("Please, give me a nuber 1-10.", "number")
        if(!person){
            return alert(`No problem, Goodbye`)
       }else if(person > 0  && person < 10){
        let computerNumber = Math.floor((Math.random() * 10) + 1);
        return test(person,computerNumber)
        }else{
            return alert(`No problem, Goodbye`)
        }
    }
}
function test(userNumber,computerNumber){
    for (let index = 0; index < 3; index++) {
        if(userNumber == computerNumber){
            return alert(`WINNER!!!`)
        } else if (userNumber > computerNumber){
            userNumber = prompt("Please, give me another number you's is too big", "number")
        } else{
            userNumber = prompt("Please, give me another number you's is too small", "number")
        }
    }
    return alert(`out of chances, you lose.`)
}