
var clear_inputs=function(){
  $("#input1").val('');
  $("#input2").val('');
  $("#input3").val('');
  $("#input4").val('');
  $("#input5").val('');

}
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
	  clear_inputs();
	  $("#real-result").fadeOut();
  $("#prediction-result").fadeOut();
  })

  /*  $('.selectpicker').selectpicker(function(){
  $.ajax({
  url: "/request",
  dataType: "json",
  data: {"category":$('.selectpicker').val()},
  success: function(result){
  $("#input1").text(result.statement);
  $("#input2").text(result.service_request_title_description);
  $("#input3").text(result.sr_customer_symptom);
  $("#input4").text(result.sr_problem_description);
  $("#input5").text(result.problem_description);}
  })
  return false;
  });*/

$("select").change(function(){
	console.log($(this).val());
	if ($(this).val()=="-1"){
	    clear_inputs();
	    $("#prediction-result").fadeOut();
	    $("#real-result").fadeOut();
	    return;
	}
  $.ajax({
  url: "/request",
  dataType: "json",
  data: {"category":$('.selectpicker').val()},
  success: function(result){
  $("#input1").val(result.statement);
  $("#input2").val(result.service_request_title_description);
  $("#input3").val(result.sr_customer_symptom);
  $("#input4").val(result.sr_problem_description);
  $("#input5").val(result.problem_description);
  $("#fa-number").text(result.fa_number);
  $("#real-CPN").text(result.real_CPN);
  $("#real-DESC").text(result.real_DESC);
  $("#real-result").fadeIn();
  $("#prediction-result").fadeOut();}
  })
    });