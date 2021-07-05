let yr1 = prompt('year born?', 'year');
let yr2 = prompt('year born?', 'year');
yr1 = parseInt(yr1)
yr2 = parseInt(yr2)
if(yr1 > yr2){
    yr3 = (yr1 -yr2) + yr1
    console.log(yr3)
}else{
    yr3 = (yr2 -yr1) + yr2
    console.log(yr3)
}

let zip = prompt('your zipcode?', 'zipcode');
var patt1 = /[0-9]{5}/g;
var n = zip.search(patt1);
console.log(Boolean(n))
if (zip.length == 5 && !n){
    console.log("sucess")
}else{
    console.log("error")
}

let word = prompt('your word?', 'word');
var patt = /[a]/g;
var str = word.replace(patt,"1");
var patt = /[e]/g;
var str2 = str.replace(patt,"2");
var patt = /[i]/g;
var str3 = str2.replace(patt,"3");
var patt = /[o]/g;
var str4 = str3.replace(patt,"4");
var patt = /[u]/g;
var str5 = str4.replace(patt,"5");
console.log(str5)

let word = prompt('your word?', 'word');
var patt = /[a|e|i|o|u]/g;
var str = word.replace(patt,"");
console.log(str)