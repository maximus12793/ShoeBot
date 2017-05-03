/**
 * Created by xeyes on 4/24/17.
 */


//
// window.location="http://store.nike.com/us/en_us/pw/mens-shoes/7puZoi3?sortOrder=publishdate|desc&ipp=120";
// // history.pushState({},"URL Rewrite Example","http://store.nike.com/us/en_us/pw/mens-shoes/7puZoi3?sortOrder=publishdate|desc&ipp=120")
// window.onload = function(e) {
//     var shoes = document.getElementsByClassName('grid-item fullSize')
//     console.log(shoes);
//     // for(s : shoes)
//     // shoes[0].getAttribute("data-pdpurl")
// };

// var g = document.getElementsByClassName("exp-product-title nsg-font-family--platform")
// <h1 class="exp-product-title nsg-font-family--platform" itemprop="name">Air Jordan 13 Retro Low</h1>
// g[0].innerHTML


// first page

console.log("RUNNING");
var urlA = "http://store.nike.com/us/en_us/pw/mens-shoes/7puZoi3?sortOrder=publishdate|desc&ipp=120";
// var pageA = require('webpage').create();



// console.log("HERE2");
// pageA.open(urlA, function(status){
//     var url = pageA.url;
//     pageA.settings.loadImages = false;
//     pageA.settings.resourceTimeout = 30; //in secs
//     // if (status){
//     var shoes = document.getElementsByClassName('grid-item fullSize');
//     // console.log(shoes.length);
//     // console.log(shoes);
//     for (var shoe in shoes) {
//         console.log(shoe.getAttribute("data-pdpurl"));
//     }
//     // // setTimeout(openPageB, 100) // open second page call
//     // // } else{
//         console.log("WTF");
//     phantom.exit(1);
//     // }
// })


var page = require('webpage').create();
page.open(urlA, function(status) {
    page.settings.loadImages = false;
    console.log("Status: " + status);
    if(status === "success") {
        console.log("on page...");
        do { phantom.page.sendEvent('mousemove'); } while (page.loading);
        var shoes = document.getElementsByClassName('grid-item fullSize');
        console.log(shoes.lenght);
    }
    phantom.exit();
});


// var page = require("webpage").create();

// function onPageReady(page) {
//     var htmlContent = page.evaluate(function () {
//         console.log(page.url, "SWAG");
//     });

//     console.log(htmlContent);

//     phantom.exit();
// }

// page.open(urlA , function (status) {
//     page.settings.loadImages = false;
//     function checkReadyState() {
//         setTimeout(function () {
//             var readyState = page.evaluate(function () {
//                 return document.readyState;
//             });

//             if ("complete" === readyState) {
//                 onPageReady();
//             } else {
//                 checkReadyState();
//             }
//         });
//     }

//     checkReadyState();
// });
