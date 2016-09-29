$(document).ready(function() {
  $('.glyphicon').click(function(e) {
    var input = $('#add_device .form-group:last').clone().val('')
    $("#add_device .form-group:last").after(
      input
    )
  });

  $('#add_asset,#add_device,#add_user').on('hide.bs.modal', function() {})
  $('a[name="export"]').on('click', function() {
    alert(2)
  })
  if ($('#add_asset').find('.errorlist').length != 0) {
    $('#add_asset').modal('show')
  }
  if ($('#add_user').find('.errorlist').length != 0) {
    $('#add_user').modal('show')
  }
});
