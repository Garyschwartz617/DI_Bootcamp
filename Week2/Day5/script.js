function bottleOfBeer() {
    let num = prompt('How many bottles of beer?', 'Number');
    console.log(`${num} bottles of beer on the wall`);
    console.log(`${num} bottles of beer`);
    let x = 0;
    let rest = num;
    while (rest > x) {
        x = x + 1;
        rest = rest - x
        if (rest == 1) {
            console.log(`Take ${x} down, pass it around`)
            console.log(`${rest} bottle of beer on the wall`);
            console.log(`${rest} bottle of beer on the wall`);
            console.log(`${rest} bottle of beer`);
        } else {
            console.log(`Take ${x} down, pass them around`)
            console.log(`${rest} bottles of beer on the wall`);
            console.log(`${rest} bottles of beer on the wall`);
            console.log(`${rest} bottles of beer`);
        }
    }
    if (rest == 1) {

        console.log(`Take 1 down, pass it around`)
        console.log(`0 bottles of beer on the wall`);
        console.log(`0 bottles of beer on the wall`);
        console.log(`0 bottles of beer`);

    } else if (rest < x && rest != 0) {
        console.log(`Take ${rest} down, pass them around`)
        console.log(`0 bottles of beer on the wall`);
        console.log(`0 bottles of beer on the wall`);
        console.log(`0 bottles of beer`);

    }
    console.log(`Everyone go home!`)
}
bottleOfBeer()