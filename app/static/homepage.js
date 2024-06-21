const addExpenseBtn = document.getElementById("addExpenseBtn")

addExpenseBtn.addEventListener("click", () => {
    let addExpenseForm = document.querySelector('.add-expense-form')

    addExpenseForm.classList.add('show')

    addExpenseBtn.disabled = !addExpenseBtn.disabled
})