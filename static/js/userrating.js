userRatingUrl = location.href.split('/')
userSlug = userRatingUrl[userRatingUrl.length - 2]

const RateUserLogic = {
    ratingManager(rating) {
        fetch(`http://127.0.0.1:8000/main-api/user-rating/${userSlug}`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({
                'rating': rating
            })
        })
            // .then(response => response.json())
            .then(data => {
                getUserRating()
            });
    }
}


rate_button = document.getElementById('rate-button')
if (rate_button) {
    
    rate_button.addEventListener('click', function () {
        rating = rate_button.getAttribute('data-rating')
        RateUserLogic.ratingManager(rating)
    })
    
    rate_stars = document.getElementById('rate-stars')
    for (let i = 0; i < rate_stars.children.length; i++) {
        rate_stars.children[i].addEventListener('click', function () {
            for (let j = 0; j < rate_stars.children.length; j++) {
                rate_stars.children[j].classList.remove('text-warning')
                if (j <= i) {
                    rate_stars.children[j].classList.add('text-warning')
                }
            }
            rate_button.setAttribute('data-rating', i + 1)
        })
    }
}
    
    

function getUserRating() {
    fetch(`http://127.0.0.1:8000/main-api/user-rating/${userSlug}`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    })
        .then(response => response.json())
        .then(data => {
            avg_rating = Math.ceil(data['avg_rating'])
            market_star = document.getElementById('market-star')
            for (let i = 0; i < market_star.children.length; i++) {
                market_star.children[i].classList.remove('text-warning')
                if (i < avg_rating) {
                    market_star.children[i].classList.add('text-warning')
                }
            }
        });
}

window.addEventListener('DOMContentLoaded', (event) => {
    getUserRating()
});
