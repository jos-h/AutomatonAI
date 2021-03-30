$(document).ready(function() {
    $("#associate").click(function(){
        $("#myModal").modal('show');
    });

    $('#cancel').click(function(){
        $('#my_form').trigger('reset');
    });

    $('#submit').click(function(){
        var data = {
           'user': $('#user_name').val(),
           'goal': $('#goal').val(),
           'priority': $('#priority :selected').text(),
           'no_of_days': $('.days').val()
        }
        is_valid = validate_data(data);
        if (is_valid == false){
            return false;
        }
        $.ajax({
            url: 'ajax/submit_data/',
            method: "GET",
            data: data,
            dataType: 'json',
            success: function (data) {
              console.log(data)
              if (data.success==true) {
                alert("record added successfully!!")
                window.location.reload();
              }
            }
        });
    });

    function validate_data(data){
    if (!data.user){
        alert("User field is required")
        return false
    }
    if (!data.goal){
        alert("goal field is required")
        return false
    }
    if (!data.priority){
        alert("priority field is required")
        return false
    }
    if (!data.no_of_days){
        alert("days field is required")
        return false
    }
}

});


