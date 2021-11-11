
const btn = document.getElementById('contact-button');
console.log(btn);

document.getElementById('contact-button').addEventListener('click', async (e) => {
    e.preventDefault();
    let name = document.getElementById('name').value;
    let phone_number = document.getElementById('number').value

    let obj = {
        name,
        phone_number
    }

    
    let data = await fetch('http://127.0.0.1:8000/contact-api/contact/', {
        method: 'POST',
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(obj)
    })

    let response = await data.json();
    console.log(response);
    

    // console.log(name);
    name.value = ''
    phone_number.value=''
    console.log("hey");
})