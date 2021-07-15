
// str = "hdjjydyfkufiku"
// str.replace(4, "W3Schools");
// console.log(str)
let st = "*"
//let fr = st.split("") 
function hangMan() {
    var person = prompt("Please, give me a wordof atleast 8 letters", "wordwords")
    if (!person || person.length < 8) {
        return hangMan()
    } else {
        let st = "*"
        st = st.repeat(person.length);
        console.log(st)
        return playTwo(person,st)
    }
}
let count = 0;
let y = ""
//let t = y.split("") 
function playTwo(person,st) {
    if (count < 10) {
        var let = prompt("Please, give me a letter", "letter")
        for (let index = 0; index < person.length; index++) {
            for (const key of person) {
                if (let == key) {
                    y = y + let
                    console.log(y)
                    return vis(person,st,y)
                    break;
                }  
            }
            count++;
            return playTwo(person,st)
        }
        
        
        // console.log(y)
        // console.log(st)
        // vis(person,st,y)
        // return playTwo(person,st)
        
    } else {
        return alert(`You LOOSE!`)
    }
}
let c = ""
function vis(person,st,y){
    // let fr = st.split("") 
    // let t = y.split("") 
    // let per = person.split("")
    console.log(y)
    // console.log(person)
    // console.log(fr)
    for (const x in person) {
        for (const i  in y) {
            if (y[i] == person[x]){
                //console.log (t[i])

                // String.prototype.replaceAt = function(index, replacement) {
                //     if (index >= this.length) {
                //         return this.valueOf();
                //     }
                 
                //     return this.substring(0, index) + replacement + this.substring(index + 1);
                // }
                 
                
                // st = st.replaceAt(i, y[i]);
                
                // let re = new RegExp( i , 'i')
                // var str2 = st.replace("*","person")

                // console.log(x)
                let end = st.substring(x + 1,st.length)
                let strt = st.substring(0,x)
                st = strt + y[i] + end


                // let a = fr.splice(x,1,t[i]).join().replace(",", "")
                // let b = a.join()
                // c = b.replace(",", "")
                alert(st)
                //t = t.join()
                //let person = per.join() const i  in 

            }
        }
    }
    alert(st)
    if (st.includes("*")){
        playTwo(person,st)
    }
    else{
        return alert(`You WIN`)
    }
    
}

hangMan()