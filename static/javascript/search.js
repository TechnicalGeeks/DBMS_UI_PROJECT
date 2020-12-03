function CheckOption(val) {
    var element = document.getElementById('options')
    element.style.display = 'block';
    element.placeholder = "Hello  clicked";

    if (val == 'sid') {
        element.style.display = 'block';
        element.placeholder = "Enter Student id ";
    } else if (val == 'name') {
        element.placeholder = "Enter Name";

    } else {
        element.placeholder = "Enter Roll Number";

    }

}