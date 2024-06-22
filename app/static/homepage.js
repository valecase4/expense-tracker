const addExpenseBtn = document.getElementById("addExpenseBtn")

addExpenseBtn.addEventListener("click", () => {
    let addExpenseForm = document.querySelector('.add-expense-form')

    addExpenseForm.classList.add('show')

    addExpenseBtn.disabled = !addExpenseBtn.disabled
})

const closeAddExpenseFormBtn = document.getElementById("closeAddExpenseFormBtn")

closeAddExpenseFormBtn.addEventListener('click', (e) => {
    e.preventDefault()
    
    let addExpenseForm = document.querySelector('.add-expense-form')

    addExpenseForm.classList.remove('show')

    addExpenseBtn.disabled = !addExpenseBtn.disabled
})