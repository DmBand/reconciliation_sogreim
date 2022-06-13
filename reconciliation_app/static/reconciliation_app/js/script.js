'use strict'

let product = document.querySelectorAll('.one-product');
let now = new Date();

for (let i=0; i<product.length; i++) {
    let date = Number(product[i].childNodes.item(3).value.split('-')[1])
    if (now.getMonth()+1 !== date) {
        product[i].classList.add('no-check')
    } else {
        product[i].classList.add('check')
    }
}

const login = document.querySelector('.login');
const menu = document.querySelector('.menu');

function addMenu() {
    menu.classList.toggle('active')
}

login.addEventListener('click', addMenu)
