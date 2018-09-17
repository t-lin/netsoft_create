
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
