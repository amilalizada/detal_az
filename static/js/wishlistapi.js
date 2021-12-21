let hearts = []
hearts = document.querySelectorAll('.fa-heart');
console.log(hearts);


hearts.forEach(element => {
    element.addEventListener('click', async (e) => { 
        e.preventDefault();
        
        if(element.classList.contains("wish")){
            element.classList.remove('wish')
            let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
            
            element.style = 'color: #C70E0E;'
        
            
            let yaxin = element.nextElementSibling
            let product = element.nextElementSibling.innerHTML
            let user = yaxin.nextElementSibling.innerHTML
            
            
            console.log(product);
            let obj = {
                user,
                product
                
            }
            
            let data = await fetch('http://127.0.0.1:8000/main-api/wishlist/', {
                method: 'POST',
                headers: {
                    "Content-type": "application/json",
                    "X-CSRFToken": csrf_token
                },
                body: JSON.stringify(obj)
            })
        
            let response = await data.json();
            console.log(response);
            element.classList.add('unwish')
        }
        else if(element.classList.contains("unwish")){
            let product = element.nextElementSibling.innerHTML
            console.log(element , 'budi')
            element.classList.remove('unwish')
            element.classList.add('wish')
            let csrf_token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
            console.log(product);
            let obj = {
                product
            }
            element.style = 'color: grey;'
            console.log(obj);
            let data = await fetch('http://127.0.0.1:8000/main-api/wishlist/', {
                method: 'DELETE',
                headers: {
                    "Content-type": "application/json",
                    "X-CSRFToken": csrf_token
                },
                body: JSON.stringify(obj)
            })
        
            let response = await data.json();
            console.log(response);
        }
    })
})