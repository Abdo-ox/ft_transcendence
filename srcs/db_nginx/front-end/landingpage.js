import { getCsrfToken, loadAnotherPage} from "./utils.js";

document.addEventListener('DOMContentLoaded', async () => {
    const csrf_token = await getCsrfToken();
    loadAnotherPage('login-btn', '/login.html');
}, {once: true});