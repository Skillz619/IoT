function Preview(form) {
    var number = form.number_upd.value;
    var dustbins = form.dustbins_upd.value;
    var date = form.date_upd.value;
    if (form.employee_upd.value != "Employee ID") {var employee = form.employee_upd.value} else {employee=""};
    if (form.dustbins_upd.value != "") {dustbins= '(' + dustbins + ')'};
    if (form.number_upd.value > 8000) {number=8000, form.number_upd.value=8000};

    document.getElementById("number-upd").innerHTML = '# ' + number;
    document.getElementById("employee-upd").innerHTML = 'Employee Id: ' + employee;
    document.getElementById("dustbins-upd").innerHTML = 'Dustbins: ' + dustbins;
    document.getElementById("date-upd").innerHTML = 'Harvest Date: ' + date;
}

function Rules(form) {
    if (form.find_order.value > 8000) {form.find_order.value=8000};
    if (form.find_dustbin.value > 100000) {form.find_dustbin.value=100000};
}
