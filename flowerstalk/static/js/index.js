function goToHomePage() {
    window.location.assign('/')

}

function goToCart() {
    window.location.assign('/cart/')
}

function clearCart() {
    window.location.assign('/cart/clear/')
}

function showMobileNav() {
    const mobileNav = document.querySelector('.mobile-nav')
    if (mobileNav.classList.contains('show-nav')) {
        mobileNav.classList.remove('show-nav')
        document.querySelector('body').classList.add('lock-scroll')
    }
        
    else {
        mobileNav.classList.add('show-nav')
        document.querySelector('body').classList.remove('lock-scroll')
    }
}

window.onclick = function(e) {
    let modal = document.querySelector('.modal')
    if (e.target == modal) {
        closeModal()
    }
}

function closeModal() {
    let modal = document.querySelector('.modal')
    if (modal.style.display == 'none')
        modal.style.display = 'flex'
    else modal.style.display = 'none'
}

function pickDeliveryMethod() {
    let pickUp = document.querySelector('#pickup')
    let delivery = document.querySelector('#delivery')
    let pickupInputs = document.querySelector('.pickup-inputs')
    let deliveryInputs = document.querySelector('.delivery-inputs')

    if(window.innerWidth > 760) {
        if(pickUp.checked) {
            pickupInputs.classList.remove('hide-inputs')
            deliveryInputs.classList.add('hide-inputs')
        }
        if(delivery.checked) {
            pickupInputs.classList.add('hide-inputs')
            deliveryInputs.classList.remove('hide-inputs')
        }
    }else {
        if(pickUp.checked) {
            pickupInputs.classList.remove('hide-inputs')
            deliveryInputs.classList.add('hide-inputs')
        }
        if(delivery.checked) {
            pickupInputs.classList.add('hide-inputs')
            deliveryInputs.classList.remove('hide-inputs')
        }
    }
}

// CART!!

function getCartDetails() {
    let cartDetails = JSON.parse(sessionStorage.getItem('cartDetails'))
    if (cartDetails === null) {
        sessionStorage.setItem('cartDetails', JSON.stringify({cartValue: 0, cartItems: []}))
    }
}
getCartDetails();



// The idea here is that every item on the landing page or category page will have an id and when it is added to cart, we can use the id to know what to store in the session. Better ideas are welcome

const dummyData = [
    {
        type : 'flower',
        name : 'Flower box and chocolate',
        price : 3500,
        img : 'd1.jpg',
        id: 1,
        count: 1,
        stock: 105
    },
    {
        type : 'flower',
        name : 'Love box, chocolate and wine',
        price : 4500,
        img : 'd2.jpg',
        id: 2,
        count: 1,
        stock: 95
    },
    {
        type : 'gift',
        name : 'Happy Valentine',
        price : 4500,
        img : 'd3.jpg',
        id: 3,
        count: 1,
        stock: 165
    },
    {
        type : 'gift',
        name : 'I love you Bouqet',
        price : 3500,
        img : 'd4.jpg',
        id: 4,
        count: 1,
        stock: 20
    },
    {
        type : 'flower',
        name : 'Aquapack Bouqet',
        price : 4500,
        img : 'd5.jpg',
        id: 5,
        count: 1,
        stock: 10
    },
    {
        type : 'flower',
        name : 'Be Mine Bouqet',
        price : 6000,
        img : 'd6.jpg', 
        id: 6,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'Big Love Box',
        price : 4500,
        img : 'd7.jpg', 
        id: 7,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'Heart Shaped Box',
        price : 2500,
        img : 'd8.png', 
        id: 8,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'Love Flower Box',
        price : 4500,
        img : 'd9.jpg', 
        id: 9,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'Forza Speciale',
        price : 4000,
        img : 'd10.jpg', 
        id: 10,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'Love In The Air',
        price : 3000,
        img : 'd11.jpg', 
        id: 11,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'Love You Roses',
        price : 4000,
        img : 'd12.jpg', 
        id: 12,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'My Baby',
        price : 5000,
        img : 'd13.png', 
        id: 13,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'My Everything',
        price : 4000,
        img : 'd14.jpg', 
        id: 14,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'My Oasis',
        price : 5000,
        img : 'd15.jpg', 
        id: 15,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'My Sweet Valentine',
        price : 4500,
        img : 'd16.png', 
        id: 16,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'My Valentine',
        price : 4000,
        img : 'd17.jpg', 
        id: 17,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'My World',
        price : 2500,
        img : 'd18.jpg', 
        id: 18,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'Plant Tropical',
        price : 10500,
        img : 'd19.jpg', 
        id: 19,
        count: 1,
        stock: 70
    },
    {
        type : 'flower',
        name : 'Presentation Bouqet',
        price : 5500,
        img : 'd20.jpg', 
        id: 20,
        count: 1,
        stock: 70
    },
]

function addItemToCart(id) {
    let cartDetails = JSON.parse(sessionStorage.getItem('cartDetails'))
    let cartItems = cartDetails.cartItems
    let cartValue = cartDetails.cartValue
    let existingCartItem = cartItems.filter(item => item.id === id)
    let notification = document.querySelector('.item-added')
    let cartNotification = document.querySelector('.item-in-cart')
    
    // Check if item is already in cart

    if (!existingCartItem.length) {
        cartValue++
        newCartItem = dummyData.filter(item => item.id === id)
        sessionStorage.setItem('cartDetails', JSON.stringify({...cartDetails, cartValue: cartValue, cartItems: [...cartItems, newCartItem[0]]}))

        setTimeout(() => {
            notification.classList.remove('show')
        }, 2000) 
        notification.classList.add('show')
    }
    else {
        setTimeout(() => {
            cartNotification.classList.remove('show')
        }, 2000) 
        cartNotification.classList.add('show')
    }
    
    getCartValue()
    getCartDetails()
}

function removeCartItem(id) {
    let cartDetails = JSON.parse(sessionStorage.getItem('cartDetails'))
    let cartItems = cartDetails.cartItems
    const items = cartItems.filter(item => item.id !== id)
    const cartNumber = document.querySelector('.cart-number')
    let cartValue = cartDetails.cartValue
    cartValue--
    if (cartValue <= 0) cartNumber.style.display = 'none'
    else {
        cartNumber.style.display = 'flex'
        cartNumber.innerHTML = cartValue
    }
    sessionStorage.setItem('cartDetails', JSON.stringify({...cartDetails, cartItems: items, cartValue: cartValue}))
}

function addItemToCartOnProductPage(id) {
    
    let button = document.querySelector('button')
    // console.log('button', button)
    if (button.innerHTML === 'Add to cart') {
        addItemToCart(id)
        button.style.backgroundColor = '#fd2929'
        button.innerHTML = 'Remove from cart'
    } 
    else if (button.innerHTML === 'Remove from cart') {
        removeCartItem(id)
        button.style.backgroundColor = '#001514'
        button.innerHTML = 'Add to cart'
    }
}

// Product details page

function goToProductPage(id) {
    sessionStorage.setItem('currentPageId', id);
    window.location.assign('product-details.html')
}

function checkIfProductIsInCart() {
    let button = document.querySelector('button')
    let currPage = sessionStorage.getItem('currentPageId')
    let cartDetails = JSON.parse(sessionStorage.getItem('cartDetails'))
    let cartItems = cartDetails.cartItems
    let existingCartItem = cartItems.filter(item => item.id == currPage)
    if (existingCartItem.length !== 0) {
        button.style.backgroundColor = '#fd2929'
        button.innerHTML = 'Remove from cart'
        
    } else console.log('Not in cart')
}


function fillFlowersPage() {
    let pageWrap = document.querySelector('.deals-wrap')
    let flowerItems = dummyData.filter(item => item.type === 'flower')
    flowerItems.map(item => {
        let itemWrap = document.createElement('div')
        itemWrap.classList.add('deals-item')
        itemWrap.innerHTML = `
        <img src="img/${item.img}" alt=""
        onclick="goToProductPage(${item.id});">
        <div class="deals-item-text-wrap">
            <div class="deals-item-text">
                <p class="light-text">Flower</p>
                <p>${item.name}</p>
                <p class="price"><b>N${new Intl.NumberFormat().format(item.price)}</b></p>
            </div>
            <img src="img/cart.svg" alt="" onclick="addItemToCart(${item.id})">
        </div>
        `
        pageWrap.appendChild(itemWrap)
    })
}

function fillGiftsPage() {
    let pageWrap = document.querySelector('.deals-wrap')
    let flowerItems = dummyData.filter(item => item.type === 'gift')
    flowerItems.map(item => {
        let itemWrap = document.createElement('div')
        itemWrap.classList.add('deals-item')
        itemWrap.innerHTML = `
        <img src="img/${item.img}" alt=""
        onclick="goToProductPage(${item.id});">
        <div class="deals-item-text-wrap">
            <div class="deals-item-text">
                <p class="light-text">Gift</p>
                <p class="item-name">${item.name}</p>
                <p class="price"><b>N${new Intl.NumberFormat().format(item.price)}</b></p>
            </div>
            <img src="img/cart.svg" alt="" onclick="addItemToCart(${item.id})">
        </div>
        `
        pageWrap.appendChild(itemWrap)
    })
}



function itemDetailsPage(url) {
    window.location = url
    return false;
}
