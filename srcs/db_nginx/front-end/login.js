import { getCsrfToken, EventNewPage, submitForm} from "./utils.js";

document.addEventListener('DOMContentLoaded', async () => {
    const csrf_token = await getCsrfToken();
    const ids = ['username', 'password'];

    EventNewPage('register-btn', '/register.html');

    document.getElementById('login-btn').addEventListener('click', ()=>{
        submitForm('/api/login/', ids, csrf_token);
    });

    document.addEventListener('keydown', (event) => {
        if (event.key == 'Enter')
            submitForm('/api/login/', ids, csrf_token);
    });

    document.getElementById('intra-btn').addEventListener('click', ()=>{
        console.log('clicked');
        fetch('/api/42/oauth/').then(response =>{
            if (response.redirected)
                console.log("you are redirected to the url:", response.url);
            console.log(response);
        }).catch(error => {
            console.log(error);
        });
    });
}, {once: true});