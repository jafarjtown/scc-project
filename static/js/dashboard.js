const toggler = document.querySelector('[data-toggler]')
const aside = document.querySelector('[data-aside]')

toggler.addEventListener('click', ()=>{
    aside.classList.toggle('show')
})