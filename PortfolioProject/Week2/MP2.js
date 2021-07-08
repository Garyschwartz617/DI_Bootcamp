let sum = "";

function number(num) {
    sum = sum + num;
    console.log(sum);
    return sum;
}
function operator(op) {
    if (sum == "") {
        return sum;
    } else {
        if (op == "+") {
            sum = sum + "+";
            console.log(sum);
            return sum;
        } else if (op == '-') {
            sum = sum + "-";
            console.log(sum);
            return sum;
        } else if (op == '*') {
            sum = sum + "*";
            console.log(sum);
            return sum;
        } else if (op == "/") {
            sum = sum + "/";
            console.log(sum);
            return sum;
        }
    }
}

function equal() {
    let total = eval(sum);
    alert(total);
    sum =""
    return total;
}
