const deliveryFee = {
    ikoyi: 2500,
    vi: 3500,
    marina: 3000,
    lekki: 6300,
    ajah: 7000,
    ikeja: 5000,
    apapa: 6000,
    festac: 8000,
    yaba: 4000,
    ikorodu: 15000,
}

let grandTotal;



function getDeliveryFee() {
    let subtotalString = document.querySelector('.subtotal').innerText.slice(1)
    let subtotalValue = parseInt(subtotalString.replace(/,/g, ''))
    let deliveryOption = document.getElementById('delivery-option').value
    let deliveryFees = document.querySelector('.delivery-fee')
    let deliveryFeeValue;
    let total = document.querySelector('.total')
    let pickup = document.getElementById('pickup')
    let delivery = document.getElementById('delivery')
    let button = document.querySelector('.submit-btn')
    let totalValue = document.querySelector('#id_total_price')
    if (pickup.checked) deliveryFeeValue = 0;
    if (delivery.checked) deliveryFeeValue = deliveryFee[deliveryOption]
    if (deliveryOption == 'neutral' && delivery.checked) {
        deliveryFeeValue = '0'
        deliveryFees.innerHTML = '&#8358;' + new Intl.NumberFormat().format(deliveryFeeValue);
        button.style.opacity = '0.5'
        button.style.pointerEvents = 'none'
        button.disabled = true
        grandTotal = Number(subtotalValue) + Number(deliveryFeeValue)
        total.innerHTML = '&#8358;' + new Intl.NumberFormat().format(grandTotal)
        totalValue.value = grandTotal
    }
    else {
        deliveryFees.innerHTML = '&#8358;' + new Intl.NumberFormat().format(deliveryFeeValue);
        button.style.opacity = '1'
        button.style.pointerEvents = 'auto'
        grandTotal = Number(subtotalValue) + Number(deliveryFeeValue)
        total.innerHTML = ' &#8358;' + new Intl.NumberFormat().format(grandTotal)
        totalValue.value = grandTotal
    }
   
    // total.innerHTML = Number(subtotalValue) + Number(deliveryFeeValue)
}

function saveValue() {
    sessionStorage.setItem('totalCartValue', grandTotal)
    window.location.assign('payment-page.html')
    // save input details
}

function fillForm() {
    let pickUp = document.querySelector('#pickup')
    let delivery = document.querySelector('#delivery')
    let pickupInputs = document.querySelector('.pickup-inputs')
    let deliveryInputs = document.querySelector('.delivery-inputs')

    let formValues = {}
    if(pickUp.checked){
        for(let i = 0; i < pickupInputs.children.length; i++){
            if((pickupInputs.children[i].tagName != 'LABEL') && (pickupInputs.children[i].tagName != 'DIV')){
                formValues[pickupInputs.children[i].getAttribute('name')] = pickupInputs.children[i].value
            }
        }
        formValues['options'] = 'pickup'
    }
    if(delivery.checked){
        for(let i = 0; i < deliveryInputs.children.length; i++){
            if((deliveryInputs.children[i].tagName != 'LABEL') && (deliveryInputs.children[i].tagName != 'DIV')){
                formValues[deliveryInputs.children[i].getAttribute('name')] = deliveryInputs.children[i].value
            }
        }
        formValues['options'] = 'delivery'
    }

    
    for(const [key, value] of Object.entries(formValues)){
        document.querySelector('form.order-form').elements[key].value = value
    }

    if(pickUp.checked){
        document.querySelector('form.order-form').elements['address'].value = ''
        document.querySelector('form.order-form').elements['lga'].value = ''
    }
    sessionStorage.setItem('grandTotalPrice', document.querySelector('#id_total_price').value)
    document.querySelector('form.order-form').submit()
}


function loadTotalValue(){
    let subtotalString = document.querySelector('.subtotal').innerText.slice(1)
    let subtotalValue = parseInt(subtotalString.replace(/,/g, ''))
    let totalValue = document.querySelector('#id_total_price')
    totalValue.value = subtotalValue
}
loadTotalValue()