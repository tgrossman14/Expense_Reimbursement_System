// AJAX allows http requests to the api
// AJAX- Asynchronous JavaScript and XML


// Promise- Built-in type. Representation of an eventual completeion/failure of an async operation and its resulting value. Essentially a proxy for a value that is not known when the promise is created. Allows the association of handlers with the eventual success or failure or async actions.

let a_promise = new Promise((resolve, reject) => {
    resolve('not HP characters')
})

// If promise is resolved
a_promise.then(
    // In promises, the returned value can only be accessed within the context of the promise. (.this)
    (data) => {console.log("Promise resolved");
    console.log(data)
    }
)
// Can chain .then() statements, but can get very difficult to read.

// =====================================================================

let new_promise = new Promise((resolve, reject) => {
    let xhr = new XMLHttpRequest() // ready state 0
    let url = 'http://hp-api.herokuapp.com/api/characters'

    xhr.onreadystatechange = function(){

        if (xhr.readyState === 4 && xhr.status === 200){
            // If ready state is 4 and status code is 200, perform DOM manipulation
           let characters = resolve(JSON.parse(xhr.response))
           console.log(characters)
        } else if (xhr.readyState === 4 && xhr.status !== 200){
            reject('characters not retrieved')
            }  
        }

    xhr.open('GET', url) // ready state 1
    xhr.send() // ready state 2
})

// DOM manipulation
new_promise.then(characters => {
    console.log(characters)
    let dropdown = document.getElementById('favorite_character')

    for (let character of characters){
        let option = document.createElement('option')
        option.innerText = character['name']
        dropdown.append(option)
    }
})