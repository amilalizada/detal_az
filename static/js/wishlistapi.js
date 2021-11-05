let hearts = document.querySelectorAll('.wish');


hearts.forEach(element => {
    element.addEventListener('click', async (e) => { 
        e.preventDefault();
        
        console.log(element.nextElementSibling);
        let yaxin = element.nextElementSibling
        let product = element.nextElementSibling.innerHTML
        let user = yaxin.nextElementSibling.innerHTML
        console.log(user,'userid');
        
        console.log(product);
        let obj = {
            user,
            product
            
        }
        console.log(obj);
        let data = await fetch('http://127.0.0.1:8000/contact-api/wishlist/', {
            method: 'POST',
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(obj)
        })
    
        let response = await data.json();
        console.log(response);
    })

})