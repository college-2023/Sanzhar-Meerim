function display(form) {
    if (form.username.value === "Ainazik") {
        if (form.password.value === "12345") {
            location = 'main/time_table.html'
        } else {
            alert("Invalid Password")
        }
    } else {
        alert("Invalid Username")
    }
}