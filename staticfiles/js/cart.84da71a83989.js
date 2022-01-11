//Populate page with cart items from session storage

function manualInputOfNumber(e, id) {
    let cartDetails = JSON.parse(sessionStorage.getItem('cartDetails'))
    let cartItems = cartDetails.cartItems
    let cartItem = cartItems.filter(cartItem => cartItem.id === id)
    cartItem[0].count = e.value
    sessionStorage.setItem('cartDetails', JSON.stringify(cartDetails))
    fillCartPage()
}

function fillCartPage() {
    const cartContainer = document.querySelector('.cart-container')
    const cartItemsWrap = document.querySelector('.cart-items-wrap')
    cartItemsWrap.innerHTML = ''
    let stage = []
    let cartDetails = JSON.parse(sessionStorage.getItem('cartDetails'))
    let cartItems = cartDetails.cartItems
    if (cartItems.length === 0) {
        cartContainer.innerHTML = "No items in cart"
        cartContainer.style.height = "200px"
    }
    else {
        cartItems.map(item => {
            let div = document.createElement('div')
            div.innerHTML = `
            <div class="cart-item flex between">
                <div class="cart-info flex between">
                    <div class="item-name-wrap flex">
                        <img src="img/${item.img}" alt="">
                        <div class="item-name">
                            <p class="cart-text">${item.name}</p>
                            <p class="light-text">In stock - ${item.stock}</p>
                        </div>
                    </div>
                    <div class="price-wrap flex between">
                        <p>N${new Intl.NumberFormat().format(item.price)}</p>
                        <p>x</p>
                        <div class="count-wrap flex">
                            <i class="far fa-minus-circle" onclick="decreaseItemNumber(${item.id})"></i>
                            <input type="text" class="itemNumber" onchange='manualInputOfNumber(this, ${item.id});' value= ${item.count}>
                            <i class="far fa-plus-circle" onclick="increaseItemNumber(${item.id})"></i>
                        </div>
                    </div>
                </div>
                <div class="total one flex between">
                    <div class="total-text flex column ">
                        <p class="light-text">Sub total</p>
                        <p class="cart-text item-price">${item.price * item.count}</p>
                    </div>
                    <i class="far fa-trash" onclick="deleteCartItem(${item.id})"></i>
                </div>                
            </div>
            `
            stage.unshift(div)
        })
        stage.forEach(item => cartItemsWrap.appendChild(item))

        // Total of the cart items
        const vat = document.getElementById('vat')
        const totals = document.querySelectorAll('.item-price')
        totalsArray = []
        totals.forEach(total => totalsArray.push(Number(total.innerHTML)))
        const total = totalsArray.reduce((curr, acc) => curr + acc, 0)
        const vatValue = Math.floor(0.075 * total)
        vat.innerHTML = `N${new Intl.NumberFormat().format(vatValue)}`
        let subTotal = total + vatValue
        let subTotalStr = new Intl.NumberFormat().format(subTotal)
        document.getElementById('grand-total').innerHTML = `N${subTotalStr}`
        sessionStorage.setItem('totalCartValue', subTotal)
    }
}
fillCartPage()

function decreaseItemNumber(id) {
    let cartDetails = JSON.parse(sessionStorage.getItem('cartDetails'))
    let cartItems = cartDetails.cartItems
    item = cartItems.filter(item => item.id === id)
    if(item[0].count > 1)item[0].count--
    sessionStorage.setItem('cartDetails', JSON.stringify(cartDetails))
    fillCartPage()
}

function increaseItemNumber(id) {
    let cartDetails = JSON.parse(sessionStorage.getItem('cartDetails'))
    let cartItems = cartDetails.cartItems
    item = cartItems.filter(item => item.id === id)
    item[0].count++
    sessionStorage.setItem('cartDetails', JSON.stringify(cartDetails))
    fillCartPage()
}

function deleteCartItem(id) {
    let cartDetails = JSON.parse(sessionStorage.getItem('cartDetails'))
    let cartItems = cartDetails.cartItems
    const items = cartItems.filter(item => item.id !== id)
    const cartNumber = document.querySelector('.cart-number')
    let cartValue = cartDetails.cartValue
    cartValue--
    if (cartValue === 0) cartNumber.style.display = 'none'
    else {
        cartNumber.style.display = 'flex'
        cartNumber.innerHTML = cartValue
    }
    sessionStorage.setItem('cartDetails', JSON.stringify({...cartDetails, cartItems: items, cartValue: cartValue}))
    fillCartPage()
}

function clearCart() {
    // sessionStorage.removeItem('cartDetails')
    let cartDetails = JSON.parse(sessionStorage.getItem('cartDetails'))
    let cartItems = cartDetails.cartItems
    const cartNumber = document.querySelector('.cart-number')
    let cartValue = cartDetails.cartValue
    cartValue = 0;
    cartItems = [];
    cartNumber.style.display = 'none'
    sessionStorage.setItem('cartDetails', JSON.stringify({...cartDetails, cartItems: cartItems, cartValue: cartValue}))
    fillCartPage()
}

