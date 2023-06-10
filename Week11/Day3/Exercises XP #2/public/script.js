fetch('/users')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        const userDataElement = document.getElementById('userData');
        userDataElement.textContent = `First Name: ${data.firstname}, Last Name: ${data.lastname}`;
    })
    .catch(error => {
        console.log('Error:', error);
    });