let xButtons = document.querySelectorAll('.x-button');

xButtons.forEach(element => {
    element.addEventListener('click', async (e) => { 
        e.preventDefault();
        
        
        let product = element.nextElementSibling.innerHTML
        console.log(element , 'fgf')
        
       
        console.log('mgcmgcvnv');
            console.log(product);
            let obj = {
                product
            }
            
            console.log(obj);
            let data = await fetch('http://127.0.0.1:8000/contact-api/wishlist/', {
                method: 'DELETE',
                headers: {
                    "Content-type": "application/json"
                },
                body: JSON.stringify(obj)
            });
        
            // let response = await data.json();
            console.log(data);
            window.location.reload()
            
        });
    });