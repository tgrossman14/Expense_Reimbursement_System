// Async keyword tells functions to return a promise instead of a value

function get_characters(){

    let xhr = new XMLHttpRequest() // ready state 0
    let url = 'http://hp-api.herokuapp.com/api/characters'

    xhr.onreadystatechange = async function(){

        if (xhr.readyState === 4 && xhr.status === 200){
            // Await used only in async functions
           let characters = await JSON.parse(xhr.response)
        
        console.log(characters)
        
        let dropdown = document.getElementById('favorite_character')

        for (let character of characters){
            let option = document.createElement('option')
            option.innerText = character['name']
            dropdown.append(option)
            }
        }
    }
    // Put open and close outside of the callback function, or the readyState will never change.
    xhr.open('GET', url)
    xhr.send()
}

// Window object has onload property that can be used to perform operations when the window loads
// IIFE (Immediately Invoked Function Expressions)- Anonymous functions that avoid cluttering the global namespace.
window.onload = function(){
    this.get_characters()
}