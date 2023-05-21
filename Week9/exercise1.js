console.log(document.forms[0])
let form=document.forms[0]
console.log(form)
let newul = document.createElement('ul');


form.addEventListener('submit', function(event) {
    event.preventDefault(); 
    let fnameValue = form.elements.fname.value; 
    let fnameValue1 = form.elements[0].value; 
    let lnameValue = form.elements.lname.value;
    let lnameValue1 = form.elements[1].value;
    console.log('First Name:', fnameValue, ' or by ID', fnameValue1);
    console.log('Last Name:', lnameValue, ' or by ID ', lnameValue1 );

    fnameValue=fnameValue.replaceAll(' ', ' ')
    fnameValue=fnameValue.trim();
   lnameValue=lnameValue.replaceAll(' ', ' ')
    lnameValue=lnameValue.trim();

    if ((fnameValue.length<=0) || (lnameValue.length<=0)) {
        alert('give valid names');
    }
    form.submit 
    let li_n = document.createElement('li');
    li_n.textContent='first name of the user: '+ fnameValue
    newul.appendChild(li_n)
    let li_f = document.createElement('li');
    li_f.textContent='second name of the user: '+ lnameValue
    newul.appendChild(li_f)
  })
  newul.textContent="List of names: "
form.appendChild(newul);
//  ================exercise 3=============     


let par = document.querySelector('p')
function getBoldItems() {
  let allBoldItems = par.querySelectorAll('strong');
console.log(allBoldItems)

  return allBoldItems;

}

let allBoldItems=getBoldItems()
function highlight(){
  for (let i of allBoldItems) {
   i.style.color="blue"
  }
}
// highlight()

function return_normal() {
  for (let i of allBoldItems) {
    i.style.color="black"
   }
}
// return_normal()


par.addEventListener('mouseover', function() {
  highlight() })

  par.addEventListener('mouseout', function() {
    return_normal() })

