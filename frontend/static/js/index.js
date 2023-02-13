console.log("Helli")

let password = document.getElementById("password")
let confirmPassword = document.getElementById("password2")
let submitButton = document.getElementById("submit")

password.addEventListener('input', comparePassword)
confirmPassword.addEventListener('input', comparePassword)

function comparePassword(){
    console.log("Hello")
    if(password.value != confirmPassword.value){
        submitButton.disabled = true
        confirmPassword.style.border = "solid red 1px"
    }else{
        submitButton.disabled = false
        confirmPassword.style.border = "solid green 1px"
    }
}