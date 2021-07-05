let sent = "This movie is not so bad!";
let wordNot = "not";
let wordBad = "bad";
let not = sent.search(wordNot);
let bad = sent.search(wordBad);
if( bad > not && not !== -1){
    let first = sent.slice(0,not);
    let second = sent.slice(bad +3,sent.length);
    console.log(`${first}good${second}`);
    // console.log(bad);
    // console.log(not);
}else{;
    console.log(sent);
}