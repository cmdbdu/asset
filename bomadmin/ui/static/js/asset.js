$(document).ready(function(){
  $('.glyphicon').click(function(e){
    var input = $('#add_device .form-group:last').clone().val('')
    $("#add_device .form-group:last").after(
      input
      )
  });
});
