export const getCsrfToken = async () => {
    return fetch("/api/csrf_token/")
        .then(response =>response.json())
        .then(data => data.csrf_token)
            .catch(error => {
            console.log("can't get the csrf token :", error);
        });
}

export const NewPage = (url) => {
    fetch(url)
    .then(response => response.text())
    .then(data => {
        let domparser = new DOMParser();
        const doc = domparser.parseFromString(data,'text/html');

        const event = new Event('DOMContentLoaded', {
            cancelable: true,
            bubbles: true,
        });

        document.head.innerHTML = doc.head.innerHTML;
        document.body.innerHTML = doc.body.innerHTML;

        let scripts = doc.querySelectorAll('script');
        document.querySelectorAll('script').forEach(script => script.remove());
        let j = 0;

        scripts.forEach(script => {
            let element = document.createElement('script');
            if (script.src) {
                element.src = script.src;
                element.type = 'module';
            }
            element.onload = () => {
                if (++j == scripts.length) 
                    document.dispatchEvent(event);
            };
            element.onerror = () => console.log("errrrrrrrrrrrror in on error ");
            console.log("before insert the element script");
            document.body.appendChild(element);
            console.log("after insert the element script");
        });
        history.pushState({}, '', url);
    }).catch(error => {
        console.log("can't load page :", error);
    });
}

export const EventNewPage = (id, url) => {
    document.getElementById(id).addEventListener('click', () => {
        NewPage(url);
    });
}

export const submitForm = (url, ids, csrf_token) => {
    let fields = {};
    for (const id of ids) {
        fields[id] = document.getElementById(id).value;
        if (fields[id].trim().length == 0) {
            alert(id ,' is required');
            return ;
        }
    }
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        body:JSON.stringify(fields)
    }).then(response => {
        if (response.redirected) {
            NewPage(response.url);
            return ;
        }
        return response.json();
    }).then(data => {
        console.log(data);
    }).catch(error => {
        console.log("can't submit data error:", error);
    })
}