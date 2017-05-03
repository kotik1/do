 function getCookie(name) {
  var value = "; " + document.cookie;
  var parts = value.split("; " + name + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}
var csrftoken = getCookie('csrftoken');
 $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
    
 
var party_id;
var ticket_id;
var image_link_dialog;
var my_picture_dialog;
var first_name_dialog;
var event_title_dialog;

 $(function() {




// $(document).on('click','.send_ticket_button', function(){



// }) 


$(document).on('click','.dialog_back_span', function(){


 $('.profile').fadeIn();
  $('.dialog').hide()


}) 


function loadMessagesInitial(party_id){
    var height = $(".dialog_container")[0].scrollHeight;
						  $(".dialog_container").animate({scrollTop: $('.dialog_container').height() * 40 });



  $.ajax({
    url: '/load_dialog/',
    type:'POST',
    dataType: 'json',
    data: {'party_id':party_id,'ticket_id':ticket_id,'csrfmiddlewaretoken': getCookie('csrftoken') },
    success: function (data) {
     var sed = JSON.parse(data['messages']);
     var textbool = JSON.parse(data['sales']);

     if (textbool != 'show'){

     	$('.send_ticket_button').hide();
     }
       for (var i = 0; i < sed.length; i++) {
                       var item = sed[i];
                       if(item.fields.from_user == party_id){
                       // if (item.fields.from_user )
                           $('.dialog_container').append('<div class="level_container"><div class="message_container_blue">' + item.fields.text +'</div><img class="my_picture" src="' + my_picture_dialog +'" width="40px" height="40px" style="position:relative;background:red;border-radius:50%; dispaly:inline-block;vertical-align:middle;margin-left:20px;"/></div>')

                        }

                        else{

                        	  $('.dialog_container').append('<div class="level_container"><img class="my_picture" src="' + my_picture_dialog +'" width="40px" height="40px" style="position:relative;background:red;border-radius:50%; dispaly:inline-block;vertical-align:middle;margin-left:20px;"/><div class="message_container">' + item.fields.text +'</div></div>')

                        }

                   }

    
        openNav();
				      window.setInterval(function(){
				         updateMessages();
				}, 5000);
    },

    error:function(){

       alert('no');
    }
})


}  

function updateMessages(){


alert();


}

 function sendMessage(party_id){
			var number_of_message_containers = $('.level_container').length;

			var message = $('#message_input').val()

			
			

			if (message !== ''){

					                     $.ajax({
					    url: '/send_message/',
					    type:'POST',
					    dataType: 'json',
					    data: {'message': message, 'party_id':party_id, 'csrfmiddlewaretoken': getCookie('csrftoken') },
					    success: function (data) {
					       

					       if (number_of_message_containers > 0){



						$('.dialog_container').append('<div class="level_container"><img class="my_picture" src="' + my_picture_dialog +'" width="40px" height="40px" style="position:relative;background:red;border-radius:50%; dispaly:inline-block;vertical-align:middle;margin-left:20px;"/><div class="message_container">' + message +'</div></div>')
						$('#message_input').val("");
						 var height = $(".dialog_container")[0].scrollHeight;
						  $(".dialog_container").animate({
						  	scrollTop: height
						  })

						}

						else{
						    
							$('.dialog_container').append('<div class="level_container" style="margin-top:320px;"><img class="my_picture" src="' + my_picture_dialog +'" width="40px" height="40px" style="position:relative;background:red;border-radius:50%; dispaly:inline-block;vertical-align:middle;margin-left:20px;"/><div class="message_container" >' + message +'</div></div>').hide().fadeIn(400)
						    $('#message_input').val("");
						    
						}
					      
					    },

					    error:function(){

					       alert('no');
					    }
					})



						


						 }


			}

// 						$(document).keypress(function(e) {

// 						    if(e.which == 13) {
// 						        sendMessage(party_id);
// 						    }

			
// })  




$(document).on('click','.send_message_button', function(){

 sendMessage(party_id);

})   

$(document).on('click','.connect', function(){





    // open messages, on backend if there was a dialog - load a dialog, if there were no dialog - create one
$('.dialog').fadeIn();
party_id= $(this).data('party-id'); 
ticket_id = $(this).data('ticket-id'); 

first_name_dialog =  $(this).data('first-name'); 
event_title_dialog = $(this).data('event-title'); 
image_link_dialog = $(this).data('picture-url');
my_picture_dialog = $(this).data('my-picture');

$('.dialog_username').html(first_name_dialog);
$('.dialog_event').html(event_title_dialog);
 $(".party_picture").attr("src", image_link_dialog);

 $('#hide_group').hide();
 $('.profile').hide()

loadMessagesInitial(party_id,ticket_id);


    
 


 

    



  });




$(document).on('click','.send_ticket_button', function(){

$('.dialog').append('<div class="send_ticket_modal_shadow"></div>');
	$('.dialog').append('<div class="send_ticket_modal_window"><div style="height:157px;"><span style="font-family:20px;font-family:muse_bold">Увага</span><br/><br/><span style="margin-top:10px;">Надіславши квиток ви відмовляйтесь від володіння цим квитком і не зможете ім скористатися. Перевірте ще раз, що покупець цього квитка надіслав вам гроші за квиток</span></div><div style="width:434px;height:60px;background:#f8f9fb;margin-bottom:0px;margin-left:-17px;"><div class="yes_send">Так, надіслати</div><div class="cancel_send">Ні, не хочу</div></div></div>');
   $('.send_ticket_modal_window').fadeIn(300);

$('.cancel_send').click(function(){

$('.send_ticket_modal_window').remove()
	
$('.send_ticket_modal_shadow').fadeOut().remove()


})

$('.yes_send').click(function(){


$.ajax({
    url: '/change_ticket_owner/',
    type:'POST',
    dataType: 'json',
    data: {'ticket_id':ticket_id,'new_owner_id':party_id,'csrfmiddlewaretoken': getCookie('csrftoken') },
    success: function (data) {
       
     
$('.send_ticket_modal_window').fadeOut().remove()
$('.send_ticket_modal_shadow').remove()
$('.send_ticket_button').remove();
 $('.profile').fadeIn();
  $('.dialog').hide()



    },

    error:function(){

       alert('no');
    }
})


})


})




$(document).on('click','.dialog_view', function(){

$('.dialog').fadeIn();
party_id= $(this).data('party-id'); 
ticket_id = $(this).data('ticket-id'); 



first_name_dialog =  $(this).data('first-name'); 
event_title_dialog = $(this).data('event-title'); 
image_link_dialog = $(this).data('picture-url');
// my_picture_dialog = $(this).data('my-picture');
my_picture_dialog = $('.profilepicture').attr('src')

$('.dialog_username').html(first_name_dialog);
$('.dialog_event').html(event_title_dialog);
 $(".party_picture").attr("src", image_link_dialog);

 $('#hide_group').hide();
  $('.profile').hide();


loadMessagesInitial(party_id);

})








$('.navigation_profile_link').click(function(){

$.ajax({
    url: '/dialogs/',
    type:'POST',
    dataType: 'json',
    data: {'csrfmiddlewaretoken': getCookie('csrftoken') },
    success: function (data) {
       
     
$('.dialog_view').remove()

        var sed = JSON.parse(data['dialogs']);

        var tickets = JSON.parse(data['tickets']);
              var events = JSON.parse(data['events']);
               var parties = JSON.parse(data['parties']);
        
        
         for (var i = 0; i < sed.length; i++) {
                       var item = sed[i];
                        var ticket = tickets[i];
                         var event = events[i];
                         var party = parties[i]



                     $('.dialogs').append('<div  class="dialog_view"  data-ticket-id="' + ticket.pk +'" data-party-id="' + party.pk +'" data-first-name="' + party.fields.first_name + '" data-picture-url="' + party.fields.picture_link + '"><div class="dialog_view_title">' + event.fields.title +'</div><img class="dialog_view_img" align="left" src="' +  party.fields.picture_link + '"><div style="display:inline-block;width:400px;"><div style="text-align:left;margin-top:22px;color:black;font-family:muse_bold;font-size:20px;">' + party.fields.first_name + '</div><div style="margin-top:10px;opacity: 0.6;font-size:14px;text-align:left;color:black;">' + ticket.fields.comment + '</div></div></div>')

                   }
    },

    error:function(){

       alert('no');
    }
})

  $('#close_nav_trigger').hide();
  $('#hide_group').hide();
  $('.profile').show();
  $('.dialog').hide()
openNav();

})
 
 })



function openNav() {
    document.getElementById("mySidenav").style.width = "558px";
    document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
}


