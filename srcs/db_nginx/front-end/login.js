import { getCsrfToken, EventNewPage} from "./utils.js";

document.addEventListener('DOMContentLoaded', async () => {
    const csrf_token = await getCsrfToken();
    EventNewPage('register-btn', '/register.html');
}, {once: true});