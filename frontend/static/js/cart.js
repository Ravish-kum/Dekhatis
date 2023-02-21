let priceDisplay = document.getElementById("priceDisplay")
let quantityDisplay = document.getElementById("quantity")
let price = priceDisplay.innerHTML
let quantity = quantityDisplay.innerHTML

priceDisplay.innerHTML = eval(price * quantity)