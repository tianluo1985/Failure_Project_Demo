
  
  $("#button").click(function(){
  $.ajax({
  url: "/classify",
  dataType: "json",
  data: {"input1":$("#input1").val(),
  "input2":$("#input2").val(),
  "input3":$("#input3").val(),
  "input4":$("#input4").val(),
  "input5":$("#input5").val()},
  success: function(result){
  $("#CPN").text(result.CPN);
  $("#DESC").text(result.DESC);
  $("#img1").attr('src',result.img_file);
  $("#prediction-result").fadeIn();}
  })
  return false;
  })
  
  $("textarea").focus(function(){
  $("#prediction-result").fadeOut();
  })