'use strict'

let product = document.querySelectorAll('.one-product');
let now = new Date();

for (let i=0; i<product.length; i++) {
    let date = Number(product[i].childNodes.item(3).value.slice(5, 7))
    if (now.getMonth()+1 != date) {
        product[i].classList.add('no-check')
    } else {
        product[i].classList.add('check')
    }
}
// document.addEventListener('DOMContentLoaded', _ => {
//     test()
//     // 
//     function test() {
//         let mon = new Date()
//         mon = mon.toLocaleString().split('.')[1]
//         $('.input').each((i, el) => {
//             const val = el.value.split('-')[1] === mon ? '' : 'no-'            
//             el.classList.add(val + 'check')
//         })
//     }
// })