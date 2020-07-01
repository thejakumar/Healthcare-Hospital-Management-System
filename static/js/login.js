 $(document).ready(function(){
        $("#submit").click(function(){
            var name= $("#name").val();
            var pass = $("#pass").val();
            if(name == '' || pass == ''){
                $("#Required").html('All Feild Are Required').css('color','red');
            }else if(name == 'admin' && pass == '123'){
                 $("#form").html('<h4>User Login Successfully</h4><a href="">Back</a>').css('color','green');
             }else{
                 $("#error").html('Invalid user');
             }
        });
    });