
  
  $("#button").click(function(){
  $.ajax({
  url: "/request",
  dataType: "json",
	      data: {"search":$("#input").val()},
  success: function(result){
  }
  })
  return false;
  })
  
  