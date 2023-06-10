        let form = document.getElementById("registerForm");

            form.addEventListener('submit', registerUser);
        
            function registerUser(e) {
                e.preventDefault(); 
        
                let dataUser = {
                    firstName: form.firstName.value,
                    lastName: form.lastName.value,
                    email: form.email.value,
                    username: form.username.value,
                    password: form.password.value,
                };
        
                console.log(dataUser);}
