
function insertRow() {
  var table = document.getElementById("sampleTable");

  var newRow = table.insertRow(1);

  var Row1cell1 = newRow.insertCell(0);
  var Row1cell2 = newRow.insertCell(1);

  Row1cell1.innerHTML = "Jane";
  Row1cell2.innerHTML = "30";

}
const div = document.getElementById('div');
const jsstyle = document.getElementById('jsstyle');

jsstyle.addEventListener("click", jsstyleRespondClick); 
div.addEventListener("click", divRespondClick); 

    function jsstyleRespondClick(e) { 
        alert("BTN is Clicked")
        // e.stopPropagation()
    }    

    function divRespondClick(e) { 
        alert("DIV is Clicked")
    }

jsstyle.addEventListener('click', () => {
    jsstyle.style.backgroundColor = 'yellow';
  });

div.addEventListener('click', () => {
    div.style.backgroundColor = 'red';
  });

// jsstyle.addEventListener('mouseout', () => {
//     jsstyle.classList.add('italic');
//   })