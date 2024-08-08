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
        fetch('/api/42/data/').then(response =>{
            return response.json();
            console.log(response);
        }).then( data => {
            const url = new URLSearchParams(data.app);
            window.location.href = data.base_url + "?" + url.toString();
            console.log(url.toString());
        }).catch(error => {
            console.log(error);
        });
    });
}, {once: true});