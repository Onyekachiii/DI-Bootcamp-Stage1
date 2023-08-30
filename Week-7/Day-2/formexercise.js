function getvalue() {
    alert('ok')
    var firstName = document.forms[0].elements.fname.value;
    var lastName = document.forms[0].elements.lname.value;
    alert(firstName +" "+ lastName)
    return firstName + " " + lastName;
  }

  let dropdown = document.getElementById('education')

  dropdown.options[2].selected = true;
  console.log(dropdown.value)

  var newOption = document.createElement("option");
  newOption.value = "Work";
  newOption.text = "Work";
  education .add(newOption)[3];

  var newOptionBeginning = document.createElement("option");
  newOptionBeginning.value = "Primary School";
  newOptionBeginning.text = "Primary School";
  education.add(newOptionBeginning, selectForm.options[0]);