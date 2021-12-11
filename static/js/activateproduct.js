const ActivateProductLogic = {
    productManager(productId) {
        fetch('http://127.0.0.1:8000/main-api/activate-product', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'product_id': productId,
            })
        })
            // .then(response => response.json())
            .then(data => {
                getProductManager()
            });
    }
}

function activateProduct(button) {
    const productId = button.getAttribute('data-id')
    ActivateProductLogic.productManager(productId)
}



function getProductManager() {
    fetch('http://127.0.0.1:8000/main-api/activate-product', {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    })
        .then(response => response.json())
        .then(data => {
            products = document.getElementById('products');
            products.innerHTML = '';
            console.log(data);
            for (let i = 0; i < data.length; i++) {
                products.innerHTML += `<div class="card-item col-12 col-md-4 col-lg-4 col-xl-3 col-sm-6">
                    <div class="incard">
                        <i class="fas fa-heart"></i>
                        <img src="${data[i]['main_image']}" alt="">
                        <div class="d-flex">
                            <span>satici:</span>
                            <span style="color: red;">${data[i]['user']}</span>
                        </div>
                        <p>${data[i]['title']}</p>
                        <button>23</button>
                        <div class="activate-button">
                        <button data-id='${data[i]['id']}' class='mt-2 activate' onclick='activateProduct(this)'>Aktiv et</button>
                        </div>
                    </div>
                </div>`

            }
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    getProductManager()
});
