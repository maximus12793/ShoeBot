url = 'http://store.nike.com/us/en_us/pd/free-rn-flyknit-2017-mens-running-shoe/pid-11385099/pgid-12011507'


document.getElementById('buyingtools-add-to-cart-button').click()

document.getElementsByClassName('exp-pdp-size-container exp-pdp-dropdown-container nsg-form--drop-down')[0].classList.add('selectBox-open')


document.getElementsByClassName('exp-pdp-size-container exp-pdp-dropdown-container nsg-form--drop-down')[0].classList.add('is-selected')

// selectBox-open is-selected"


function sizeSelect(){
var sizeMenu = document.getElementsByClassName("exp-pdp-size-container exp-pdp-dropdown-container nsg-form--drop-down");
var size = document.getElementsByName("skuAndSize")[0];
for(var i = 0; i < size.options.length; i++) {
    console.log(size.options[i].index);
    if(size.options[i].index == shoesize){
        document.getElementsByName("skuAndSize")[0].options.selectedIndex = i; +
        //gets correct options but can't seem to change the size option on webpage
        break;
    }
}
