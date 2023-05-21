let paragr=document.querySelector('article h1')
console.log(paragr)
let article = document.querySelector('article');
let lastParagraph = article.lastElementChild;
article.removeChild(lastParagraph); 


let peace_topaint=document.querySelector('article h2')
peace_topaint.addEventListener('click', function() {
        peace_topaint.style.backgroundColor = 'red';  
})

let peace_tohide=document.querySelector('article h3')
peace_tohide.addEventListener('click', function() {
    peace_topaint.style.display = 'none';  
})


function bold(){
    let allparagr=document.getElementsByTagName('p')
    for(let i=0; i<allparagr.length; i++) {
    console.log(allparagr);   
    allparagr[i].style.fontWeight = 'bold';
}
}

paragr.addEventListener('mouseover', function() {
    let randomSize = Math.floor(Math.random() * 101);
    let fontsize=randomSize+'px'
    paragr.style.fontSize = fontsize;  })


paragr.addEventListener('mouseout', function() {
    paragr.style.fontSize = '';  
      });

let allparagr=document.getElementsByTagName('p');
let second=allparagr[1];

second.addEventListener('mouseover', function() {
    second.classList.add('fade')}
)

second.addEventListener('mouseout', function() {
    second.classList.remove('fade')}
)
