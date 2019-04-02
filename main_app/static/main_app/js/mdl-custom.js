
$(document).ready(function(){
  $("#footer").load("footer.html");

  $('#people_menu').hover(
    function () {
      $("#people_items").show(250);
    }, 
    function () {
     $("#people_items").hide();
    });
  
  $('#program_menu').hover(
    function () {
      $("#program_items").show(250);
    }, 
    function () {
     $("#program_items").hide();
    });

  $('#curr_studs_menu').hover(
    function () {
      $("#curr_studs_items").show(250);
    }, 
    function () {
     $("#curr_studs_items").hide();
    });

});

function delete_resume($this){
    
    var resume = $this.id;
    var csrf = document.getElementById($this.id).parentNode.firstChild.nextElementSibling.value;
    console.log(csrf);
    
    console.log("Resume to delete: " + resume)
    $.post( "/delete-resume/",{ 'resume' : resume, 'csrfmiddlewaretoken': csrf },function(json) {
        alert("Resume deleted.");
        location.reload();
    })
    .fail(function(){
        alert("ERROR: Failed to delete resume. Contact the site administrator.");
    })
};

function check_pass_match() {
    var oldpass = $("input[name='old_password']")[0]
    var newpass1 = $("input[name='new_password']")[0]
    var newpass2 = $("input[name='repeat_new_password']")[0]

    if (oldpass.value.length == 0 || newpass1.value.length == 0 || newpass2.value.length == 0) {
        alert("ERROR: All password fields are required to be non-empty")
    }
    else if (oldpass.value == newpass1.value || oldpass.value == newpass2.value) {
        alert("ERROR: Old password and new password must not match")
    }
    else if (newpass1.value != newpass2.value) {
        alert("ERROR: New password and the repeated password does not match")
    }
    else {
        $("form[name='change-pass']")[0].submit();
    }
}
