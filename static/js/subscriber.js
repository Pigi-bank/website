$(document).ready(function(){
  $('#form').submit(function(event){
    event.preventDefault()
    form = $("form")


    $.ajax({
      'url':'/ajax/subscribe/',
      'type':'POST',
      'data':form.serialize(),
      'dataType': 'json',
      'success': function(data){
        alert(data['success'])
      },
    })// END of Ajax method
    $('#id_name').val('')
    $("#id_phone_number").val('')
    $("#id_email").val('')
    
  }) // End of submit event

}) // End of document ready function