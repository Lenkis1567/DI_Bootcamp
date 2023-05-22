function insertRow(){
let tb=document.getElementById('sampleTable').firstElementChild;
//     let row=document.createElement('tr')
let row=tb.firstElementChild;
const rownum=tb.children.length;

const newRow =row.cloneNode(true);
newRow.firstElementChild.InnerText = `Row${rownum+1}, cell1`;
newRow.firstElementChild.InnerText = `Row${rownum+1}, cell2`;
tb.appendChild(newRow)
}



const div1=document.getElementById('div1') 
const div1=document.getElementById('div2')
const div1=document.getElementById('but')

div1.addEventListener('click', function(e){
    alert('div1!')}, true)   
// меняет порядок//


div1.addEventListener('click', function(e)){
    alert('div2!')
}
but.addEventListener('click', function(e)){
    alert('but!')
}

function handleSubmit(e) {
    let const_form=document.forms.form_one;
    let username=const_form.elements.username.value
    let pass=const_form.elements.username.value
    username=username.replaceAll(' ', ' ')
    username=username.trim();
    if (username.length<=0) {
        alert('give a valid name');
      frm.submit()  
    }}

    