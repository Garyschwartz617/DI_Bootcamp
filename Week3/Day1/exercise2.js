let allBooks = [
    {
       title: "Harry Potter", 
       author: "JK Rowling",
       image : "https://pbs.twimg.com/profile_images/632661885557411840/xolAfPEm_400x400.jpg" ,
       alreadyRead: true

},
{
       title: "Math Book", 
       author: "Clifford Pickover",
       image : "https://images-na.ssl-images-amazon.com/images/I/81OrIk+OffL.jpg" ,
       alreadyRead: false

} 
]

let listBooks = document.querySelector("listBooks")
for (const iterator of allBooks) {
    let newDiv = document.createElement('div')
    let newTextNode = document.createTextNode(`${title} written by ${author}`);
    newDiv.appendChild(newTextNode);
    listBooks.appendChild(newDiv)
    
}
// for (let index = 0; index < allBooks.length; index++) {
//     const element = allBooks[index];
//     let newDiv = document.createElement('div')
//     let newTextNode = document.createTextNode(`${title} written by ${author}`);
    
// }