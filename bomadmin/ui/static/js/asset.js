$('.asset-to').dblclick(function(e) {
  var value = e.target.innerText
  e.target.innerHTML = '<input class="asset-input" onblur="sub(event)" style="border:0px;" type="text" value=' + value + '>'
})

function sub(event) {
  var value = event.target.value;
  var obj = event.srcElement ? event.srcElement : event.target;
  var asset_id = location.href.split('/').pop();
  console.log(asset_id);
  var $obj = $(obj)
  $.ajax({
    url: 'edit',
    type: 'POST',
    data: {
      'value': value,
      'asset_id': asset_id,
    },
    success: function(result) {
      location.reload()
    }
  })
}
