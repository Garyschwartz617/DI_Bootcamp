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
let listBooks = document.getElementsByClassName("listBooks")
for (let index = 0; index <= allBooks.length; index++) {
    const element = allBooks[index];
    let newDiv = document.createElement('div')
    let newTextNode = document.createTextNode(`${element.title} written by ${element.author}`);
    console.log(newTextNode)
    newDiv.appendChild(newTextNode);
    listBooks[0].appendChild(newDiv)
    let newImg = document.createElement('img')
    newImg.setAttribute("src",element.image)
    newDiv.appendChild(newImg);
    newImg.style.width = "100px"
    newImg.style.height = "100px"
    if(!element.alreadyRead){
        newDiv.style.background = "red"
    }
}