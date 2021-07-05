let lang = prompt('What language?', 'Language');
lang = lang.toLowerCase()
switch(lang){
    case "french":
        console.log("Bonjour")
    break;
    case "english":
        console.log("Hello")
    break; 
    case "hebrew":
        console.log("Shalom")
    break;  
    default:
    console.log("01110011 01101111 01110010 01110010 01111001")
}

let grade = prompt('Y0ur grade?', 'grade');
if(grade > 90){
    console.log("A")
} else if( grade > 80){
    console.log("B")
}else if( grade > 70){
    console.log("C")
}else{
    console.log("D")
}

let verb = prompt('your verb?', 'Verb');

if (verb.length > 3){
    if(verb.endsWith("ing")){
        console.log(`${verb}ly`);
    }else{
        console.log(`${verb}ing`);
    }

} else {
    console.log(verb);
}
