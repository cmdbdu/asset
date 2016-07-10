$(document).ready(function(){
  $('.col-sm-10').click(function(e){
    var el = e.target;
    el.removeAttribute("disabled")
  });
});
function change_to_input(arg){
  alert('1');
  alert(arg.attr);
}
