
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
    
    console.log("data: " + resume)
    $.post( "/delete-resume/",{ 'resume' : resume, 'csrfmiddlewaretoken': csrf },function(json) {
      alert("success");
      location.reload();
    })
      .fail(function(){
      alert("failed");
    })
};
