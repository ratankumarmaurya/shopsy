
     function validation(){
      var name=document.getElementById("name").value;
      var password=document.getElementById("password").value;
      var email=document.getElementById("email").value;


      if (name === "") {
                document.getElementById("nameError").innerHTML="Enter name";
                document.getElementById("name").focus();
                return false;
            }
            else{
                document.getElementById("nameError").innerHTML=""
            }

        if(email=== ""){
            document.getElementById("mailError").innerHTML="Email Blank";
            return false;
        }
        else{
            document.getElementById("mailError").innerHTML="";
        }
          if(password ===""){
            document.getElementById("passError").innerHTML="password Blank";
            document.getElementById("name").focus();
            return false;
        }
        else{
            document.getElementById("passError").innerHTML="";
        }

        }

function validate(){
       var email=document.getElementById("email").value;
       var password=document.getElementById("password").value;
       if(email=== ""){
            document.getElementById("mailError").innerHTML="Email Blank";
            return false;
        }
        else{
            document.getElementById("mailError").innerHTML="";
        }
          if(password===""){
            document.getElementById("passError").innerHTML="password Blank";
            return false;
        }
        else{
            document.getElementById("passError").innerHTML="";
        }
      }