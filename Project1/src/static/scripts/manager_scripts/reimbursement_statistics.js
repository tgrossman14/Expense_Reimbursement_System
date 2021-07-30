async function calculate_statistics(){
    const url = 'http://localhost:5000/reimbursement_statistics/calculate'
    let response = await fetch(url)
    let stats = await response.json()
    let o_avg = document.getElementById('o_avg_amount_number')
    let a_rate = document.getElementById('approval_rate_number')
    let highest = document.getElementById('highest_amount_number')
    let a_avg = document.getElementById('a_avg_amount_number')
    
    o_avg.innerText = stats['average']
    a_rate.innerText = stats['rate']
    highest.innerText = stats['highest']
    a_avg.innerText = stats['approved_average']
}


window.onload = function(){
    this.calculate_statistics()
}