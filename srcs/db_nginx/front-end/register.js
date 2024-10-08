import { getCsrfToken, submitForm } from "./utils.js";

document.addEventListener('DOMContentLoaded', async () => {
    const csrf_token = await getCsrfToken();
    const ids = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2'];
    let first = faker.name.firstName();
    let last = faker.name.lastName();
    document.getElementById('first_name').value = first;                     //to autofill
    document.getElementById('last_name').value = last;                       //to autofill
    document.getElementById('username').value = faker.internet.userName(first, last);//to autofill
    document.getElementById('email').value = faker.internet.email(first, last);      //to autofill
    const pass = faker.internet.password();                                                  //to autofill
    document.getElementById('password1').value = pass;                                       //to autofill
    document.getElementById('password2').value = pass;                                       //to autofill
    
    document.getElementById('submit-btn').addEventListener('click', ()=>{
        submitForm('/api/register/', ids, csrf_token);
    });

    document.addEventListener('keydown', (event) => {
        if (event.key == 'Enter')
            submitForm('/api/register/', ids, csrf_token);
    });
}, {once: true});




















// /****** register form ** */
// const password = document.getElementById("password");
// const confirmPassword = document.getElementById("confirm_password");

// confirmPassword.addEventListener("input", () => {
//   if (password.value !== confirmPassword.value) {
//     confirmPassword.setCustomValidity("Passwords does not  match.");
//   } else {
//     confirmPassword.setCustomValidity("");
//   }
// })
