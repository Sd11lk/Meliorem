function validate() {
  if (document.getElementById("fname").value == "Morax" && document.getElementById("psw").value == "admin123") {
   alert("Success");
   var userid = document.getElementById("userid").value;
   setTimeout(function() {window.location = "#"});
}

else if (document.getElementById("fname").value == "Teacher" && document.getElementById("psw").value == "preach123") {
  alert("Success");
  var userid = document.getElementById("fname").value;
  setTimeout(function() {window.location = "/compute"});
      }

else if(document.getElementById("fname").value == "savio" && document.getElementById("psw").value == "savio122") {
  alert("Success");
  var userid = document.getElementById("fname").value;
  setTimeout(function() {window.location = "/student1"});
      }

else if(document.getElementById("fname").value == "Sakshi Chauhan" && document.getElementById("psw").value == "sakhan123") {
  alert("Success");
  var userid = document.getElementById("fname").value;
  setTimeout(function() {window.location = "/student2"});
     }


else {
	alert("Fail. Try Again.");


  }


}
