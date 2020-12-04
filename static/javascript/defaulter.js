function CheckOption(val) {
    var element = document.getElementById('options')
    var divsion = document.getElementById('division2')

    if (val == 'subject') {
        element.style.display = 'block';
        element.placeholder = "Enter Subject ";
        divsion.style.display = 'none';
    }
    if (val == 'overall') {
        element.style.display = 'none';
        divsion.style.display = 'block';
    }
}