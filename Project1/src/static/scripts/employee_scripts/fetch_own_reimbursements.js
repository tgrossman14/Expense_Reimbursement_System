async function get_own_reimbursements(){

    let url = 'http://localhost:5000/employee_dashboard/reimbursement'
    console.log(url)
    let response = await fetch(url)
    let reimbursements = await response.json()
    let tbody = document.getElementById('reimbursement_sheet')
    Object.entries(reimbursements).forEach((reimbursement) =>{
        let tr = document.createElement('tr')
        var td = document.createElement('td')
        td.innerText = reimbursement[1]._reimbursement_id
        tr.append(td)
        var td = document.createElement('td')
        td.innerText = reimbursement[1]._reimbursement_approval
        tr.append(td)
        var td = document.createElement('td')
        td.innerText = reimbursement[1]._reimbursement_amount
        tr.append(td)
        var td = document.createElement('td')
        td.innerText = reimbursement[1]._reimbursement_reason
        tr.append(td)
        tbody.append(tr)
    })
}

window.onload = function(){
    this.get_own_reimbursements()
}