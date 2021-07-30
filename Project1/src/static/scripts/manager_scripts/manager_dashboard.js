async function get_reimbursements(){
    const url = 'http://localhost:5000/manager_dashboard/reimbursement'
    let response = await fetch(url)
    let reimbursements = await response.json()
    let tbody = document.getElementById('reimbursement_sheet')
    Object.entries(reimbursements).forEach((reimbursement) => {
        let tr = document.createElement('tr')
        tr.className = 'reimbursement_row'
        var td = document.createElement('td')
        td.setAttribute('id', 'id')
        td.innerText = reimbursement[1]._reimbursement_id
        tr.append(td)
        var td = document.createElement('td')
        td.setAttribute('id', 'approval')
        td.innerText = reimbursement[1]._reimbursement_approval
        tr.append(td)
        var td = document.createElement('td')
        td.setAttribute('id', 'amount')
        td.innerText = reimbursement[1]._reimbursement_amount
        tr.append(td)
        var td = document.createElement('td')
        td.setAttribute('id', 'reason')
        td.innerText = reimbursement[1]._reimbursement_reason
        tr.append(td)
        tbody.append(tr)
    })
    table_selection()
}


function table_selection(){
    document.querySelectorAll('.reimbursement_row').forEach(reimbursement_row => {
        reimbursement_row.addEventListener('click', () => {
            if (document.querySelector('#selected')) {
                document.querySelector('#selected').removeAttribute('id')
            }
            remove_displayed_selection()
            reimbursement_row.setAttribute('id', 'selected')
            display_selection()
            approve_button()
            deny_button()
            confirm_button()
        })
    })
}


function display_selection(){
    let selection = document.getElementById('selected')
    let selection_amount = selection.querySelector("#amount")
    let selection_reason = selection.querySelector("#reason")
    let tr_amount = document.getElementById('selected_amount')
    let tr_reason = document.getElementById('selected_reason')
    tr_amount.innerText = selection_amount.innerText
    tr_reason.innerText = selection_reason.innerText
}


function remove_displayed_selection(){
    let tr_amount = document.getElementById('selected_amount')
    let tr_reason = document.getElementById('selected_reason')
    tr_amount.innerText.replace('')
    tr_reason.innerText.replace('')
}


function approve_button(){
    let button = document.getElementById('approve_btn')
    button.removeAttribute('disabled')
    button.addEventListener("click", ()=>{
        let selection = document.getElementById('selected')
        document.querySelector("#selected").setAttribute('temp', 'temp_approved')
        selection.children[1].innerText = "approved (uncomfirmed)"
    })
}


function deny_button(){
    let button = document.getElementById('deny_btn')
    button.removeAttribute('disabled')
    button.addEventListener("click", ()=>{
        let selection = document.getElementById('selected')
        document.querySelector("#selected").setAttribute('temp', 'temp_denied')
        selection.children[1].innerText = "denied (unconfirmed)"
    })
}

function confirm_button(){
    let button = document.getElementById('confirm_btn')
    button.removeAttribute('disabled')
    button.addEventListener("click", ()=>{
        document.querySelectorAll("[temp]").forEach(altered_reimbursement => {
            if (altered_reimbursement.firstElementChild.nextSibling.innerText == 'denied (unconfirmed)'){
                altered_reimbursement.firstElementChild.nextSibling.innerText = 'denied'
                console.log(altered_reimbursement)
            }
            else {
                altered_reimbursement.firstElementChild.nextSibling.innerText = 'approved'
            }
        })
        let my_json = {}
        let i = 0
        document.querySelectorAll("[temp]").forEach(altered_reimbursement => {
            altered_reimbursement.removeAttribute('temp')
            altered_reimbursement = {'reimbursement_id' : altered_reimbursement.firstElementChild.innerText,
                                    'new_approval' : altered_reimbursement.firstElementChild.nextSibling.innerText}
            my_json[i].append(altered_reimbursement)
            i += 1
        })
        if (Object.keys(my_json).length){
            console.log(my_json)
            return my_json
        }
    })
}


window.onload = function(){
    this.get_reimbursements()
}