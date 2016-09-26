$(document).ready(function(){
  $('.select').change(function(){
      var url = "/business/?page="
      window.location.href= url+$(".select").val()
      });
  $("#btn_bind_property").on('click', function(){
    var bid = $(this).data('bid')
    var pid = $(this).data('pid')
    var prid = $(this).data('prid')
    var data = {'bid':bid,'pid':pid, 'prid':prid}
    window.location.href="/business/bind_property/?bid="+bid+"&pid="+pid+"&prid="+prid 
    });
  $(".a_bind_property").on('click',function(){
    var prid = $(this).data("prid")
    $("#bind_property").on("shown.bs.modal",function (){
      $("#btn_bind_property").data("prid",prid);
      })
    })
  $(".a_delay").on('click',function(){
    var prid = $(this).data("prid")
    var bid = $(this).data("bid")
    $("#delay").on("show.bs.modal",function(){
      $(".btn_create_delay").data("prid",prid)
      $(".btn_create_delay").data("bid",bid)
      })
    })
  $('.btn_create_delay').on('click',function(){
    var prid = $(this).data('prid')
    var bid = $(this).data("bid")
    var start_time = $('#id_delay_start_time').val()
    var end_time = $('#id_delay_end_time').val()
    var remark = $('#id_remark').val()
    var url = '/business/create_delay/'
    var data ={'prid':prid,
                'bid':bid,
                'start_time':start_time,
                'end_time':end_time,
                'remark':remark}
    $.ajax({
      type:'GET',
      url:url,
      data:data,
      cuccess:function(){
        alert('sucess')
        }
      })
    $('#delay').modal('hide')
    })
  $('#id_product_name').change(function(){
    select_product_type()})
  $('.unbind_property').on('click',function(){
    var pid = $(this).data('pid')
    var prid = $(this).data('prid')
    window.location.href="/business/unbind_property/?prid="+prid+"&pid="+pid
    })
})

function select_product_type(){
  var product = $('#id_product_name').val()
  var product_waf_type = {'P300S': 'P300S', 'P600S': 'P600S', 'P1000S': 'P100S',
                            'P2500S': 'P1500S', 'P2000S': 'P2000S', 'P6000S': 'P6000S'};
  var product_websoc_type = {'P100':'P100','P300':'P300'}
  var websoc_model = "监控网站数量:100 \n用户数量：12 \n\n1.默认模块：可用性检测，综合报表数据分析模块，多用户，\n安全事件[暗链，挂马，关键词，变更],漏洞[应用漏洞]，\nWEB漏洞自动验证模块。\n2.付费模块：二次开发，短信模块，集群模块，截图模块，站点发现"
  if(product == 'WAF'){
    var content;
    for (var type in product_waf_type){
      content += '<option>'+type+'</option>'
      };
    $('#id_product_type').html(content)
    $('#id_active_model').html('无可用模块')
    }else if(product == 'WebSOC'){
      var content;
      for (var type in product_websoc_type){
        content += '<option>'+type+'</option>'
        };
    $('#id_product_type').html(content)
    $('#id_active_model').html(websoc_model)
    }else if(product == 'WebSaber'){
    $('#id_product_type').html('<option>--</option>')
    $('#id_active_model').html('none')
    }else{alert('产品名称错误')}
}

function count_server_days(){
  var begin_date = $('#id_start_time').val(),
      end_date = $('#id_end_time').val(),
      period;
  if(end_date !== ''){
    if(begin_date === ''){
      $('#id_start_time').focus();
      }
    b_date = new Date(begin_date);
    e_date = new Date(end_date);
    period = parseInt((e_date.getTime() - b_date.getTime()) / parseInt(1000 * 3600 * 24, 10), 10);
    if (period <= 0){
      alert('起始日期小于截止日期');
      $('#id_end_time').focus();
      return;
    }
  }
}

function search_business(){
  var search_value =  $('#searchword').val()
  var host = window.location.host,
      pathname = window.location.pathname,
      protocol = window.location.protocol,
      url = protocol+'//'+host+pathname;

  window.location.href = url+'?search_value='+search_value
}

function search_property(){
  var table = $('#bind_property_table tr')
  var searchword = $('#searchword').val()
  for(var i=0;i<table.length;i++){
    var cell_val = table[i].cells[0].innerHTML
    if( cell_val.indexOf(searchword) <= 0 ){
      $('#bind_property_table tr:eq('+i+')').hide()
      }
    }
}
