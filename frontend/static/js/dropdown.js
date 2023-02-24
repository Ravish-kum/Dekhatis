let userDropdown = false
let dropdown = false

let userButton = document.getElementById("userButton")
let userDropdownBox = document.getElementById("dropdown")


userButton.addEventListener('click', userDropdownClicked)


function userDropdownClicked(){
    if(userDropdown){
        userDropdown = false;
        userDropdownBox.style.display = 'none'
    }
    else{
        userDropdown = true;
        userDropdownBox.style.display = 'block'
    }
}
console.log(userDropdownBox)