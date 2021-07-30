// Query selector uses CSS. Selects em for manipulation

let flag = document.querySelector('#flag > img')
const color_arr = ['red', 'green', 'blue']
let i = 0

// Change color of border in response to uix
// Use event listener to respond to a particular event
flag.addEventListener('click', () => {
    i = (i + 1) % 3
    flag.style.borderColor = color_arr[i]
})
