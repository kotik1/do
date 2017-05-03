
 var fb_api_app_id;
   if (in_production == false){
     
      fb_api_app_id = '394555824254104';
   }

   else{
       
        fb_api_app_id = '394391410937212';

   }


//vk auth beginning




VK.init({
  apiId: 5932984
});


VK.Auth.getLoginStatus(function(response) {

  if (response.session) {
  // alert();
// alert(JSON.stringify(response.session));
 VK.Api.call('users.get', {user_ids: response.session.mid, fields: 'photo,counters'}, function(r) {


    $(".profilepicture").attr("src", r.response[0].photo);
   $('.number_of_friends').append(r.response[0].counters.friends);


});
}
  });



function VKcheckLoginState(){

VK.Auth.getLoginStatus(function(response) {
  if (response.session) {
    // alert('Авторизованный в Open API пользователь');
    // alert(JSON.stringify(response));
  } else {
   // alert('Неавторизованный в Open API пользователь. Вызываем функцию залогиниться');
   VKlogin()

  }
});


}



function VKlogin(){


  VK.Auth.login(function(response) {
  if (response.session) {
    /* Пользователь успешно авторизовался */
    authVK(response.session.user.id,response.session.user.href);
    // alert(JSON.stringify(response))
  } else {
    /* Пользователь нажал кнопку Отмена в окне авторизации */
  }
}, 4194304);

}





function authVK(vk_user_id,link){

  // alert(vk_user_id);
  // alert(link)

$('.sidenav').append('<div class="loading_white_wall"><div class="sk-cube-grid"><div class="sk-cube sk-cube1"></div><div class="sk-cube sk-cube2"></div><div class="sk-cube sk-cube3"></div><div class="sk-cube sk-cube4"></div><div class="sk-cube sk-cube5"></div><div class="sk-cube sk-cube6"></div><div class="sk-cube sk-cube7"></div><div class="sk-cube sk-cube8"></div><div class="sk-cube sk-cube9"></div></div></div>');


  VK.Api.call('users.get', {user_ids: vk_user_id, fields: 'first_name,last_name,photo,counters'}, function(r) {
// if(r.response) {

// alert(r.response[0].counters.friends);
// alert(r.response[0].contacts);
// alert(JSON.stringify(r.response[0]));

var vk_first_name = r.response[0].first_name;
var vk_last_name = r.response[0].last_name;
var vk_id = vk_user_id
// var vk_email = r.response[0].email
// var vk_username = r.response[0].name
var vk_link = link
var vk_friends_number = r.response[0].counters.friends
var vk_picture = r.response[0].photo



// }


$.ajax({
    url: '/authvk/',
    type:'POST',
    dataType: 'json',
    data: {"vk_first_name": vk_first_name, "vk_last_name": vk_last_name,"vk_id":vk_user_id, "vk_link":vk_link,"vk_friends_number": vk_friends_number, "vk_picture": vk_picture, 'csrfmiddlewaretoken': getCookie('csrftoken') },
    success: function (data) {
  
      setTimeout(
  function() 
  {
    $('#hide_group').hide();
    $('#show_group').show();
    $('.loading_white_wall').fadeOut();
    $('.greeting_title_name').html(vk_first_name);
     $(".email_input").prop("placeholder", 'E-mail');
    // if(vk_email){ 
     
    //   $(".email_input").prop("value", vk_email);
    // }

    // else{

    //     $(".email_input").prop("placeholder", 'E-mail');
    // }


  }, 1000);

    
      
    },
    error : function(data) {
      
      $('#hide_group').hide();
      $('#error_group').show();
      $('.loading_white_wall').fadeOut();

    }


  })





});






}


// vk auth end



function statusChangeCallback(response) {
    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
      // Logged into your app and Facebook.
      // testAPI();
      authFB();
      // alert('connected');

    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      // document.getElementById('status').innerHTML = 'Please log ' +
      //   'into this app.';
          alert('2');
           loginDialogFB()

    } else {
      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      // document.getElementById('status').innerHTML = 'Please log ' +
      //   'into Facebook.';
           // alert('3');
            loginDialogFB()
    }
  }

  // This function is called when someone finishes with the Login
  // Button.  See the onlogin handler attached to it in the sample
  // code below.
  function checkLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }

function loginDialogFB(){

  FB.login(function(response){
   // alert(JSON.stringify(response))
   // alert(response.authResponse.userID)
  authFB();

      // alert(JSON.stringify(response))
},  {scope: 'email, user_friends'} );
}



  window.fbAsyncInit = function() {
  FB.init({
    // first one is test id
    appId      : fb_api_app_id,
    // appId      : '1174285602624484',
    // appId      : '1136272963092415',
    cookie     : true,  // enable cookies to allow the server to access
                        // the session
    xfbml      : true,  // parse social plugins on this page
    version    : 'v2.8' // use graph api version 2.8
  });

  // Now that we've initialized the JavaScript SDK, we call
  // FB.getLoginStatus().  This function gets the state of the
  // person visiting this page and can return one of three states to
  // the callback you provide.  They can be:
  //
  // 1. Logged into your app ('connected')
  // 2. Logged into Facebook, but not your app ('not_authorized')
  // 3. Not logged into Facebook and can't tell if they are logged into
  //    your app or not.
  //
  // These three cases are handled in the callback function.

  // FB.getLoginStatus(function(response) {
  //   statusChangeCallback(response);
  // });

  FB.getLoginStatus(function(response) {
       if (response.status === 'connected') {
              FB.api('/me?fields=friends,cover,picture.width(90).height(90)', function(response) {
                      var profile_picture_url_FB = response.picture.data.url;
                    // alert(JSON.stringify(response))
                  

                    
                     
                      if (response.cover.source != null){

                         var profile_cover_url_FB = response.cover.source;
                          var beginning = 'url('
                          var ending = ') no-repeat'
                          var tadam = beginning + profile_cover_url_FB  + ending;
                        $(".fb_cover").css({'background' : tadam, 'background-size': '100%', 'filter':'blur(4px)' })

                      }

                        
                      $(".profilepicture").attr("src", profile_picture_url_FB);
                      $('.number_of_friends').append(response.friends.summary.total_count)
                   

                     
                      
              });



       }
    });

  };

  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));




  // Here we run a very simple test of the Graph API after login is
  // successful.  See statusChangeCallback() for when this call is made.
  // function testAPI() {
  //   console.log('Welcome!  Fetching your information.... ');
  //   FB.api('/me', function(response) {
  //     console.log('Successful login for: ' + response.name);
  //     document.getElementById('status').innerHTML =
  //       'Thanks for logging in, ' + response.name + '!';
  //   });
  // }

// checkLoginState()

function authFB(fb_user_id){
 $(function() {

  
  $('.sidenav').append('<div class="loading_white_wall"><div class="sk-cube-grid"><div class="sk-cube sk-cube1"></div><div class="sk-cube sk-cube2"></div><div class="sk-cube sk-cube3"></div><div class="sk-cube sk-cube4"></div><div class="sk-cube sk-cube5"></div><div class="sk-cube sk-cube6"></div><div class="sk-cube sk-cube7"></div><div class="sk-cube sk-cube8"></div><div class="sk-cube sk-cube9"></div></div></div>');


  })

FB.api('/me?fields=first_name,last_name,email,name,link,friends,picture', function(response) {

var fb_first_name = response.first_name;
var fb_last_name = response.last_name;
var fb_id = response.id;
var fb_email = response.email
var fb_username = response.name
var fb_link = response.link
var fb_friends_number = response.friends.summary.total_count
var fb_picture = response.picture.data.url
// alert(fb_picture)

// alert(response.name)
 
// alert(JSON.stringify(response.first_name))
 
// ajaxPost('/authfb/', {'username': fb_first_name , 'fb_id': fb_id}, function(){ 
$.ajax({
    url: '/authfb/',
    type:'POST',
    dataType: 'json',
    data: {"fb_first_name": fb_first_name, "fb_last_name": fb_last_name, "fb_username": fb_username, "fb_email":fb_email, "fb_id":fb_id, "fb_link":fb_link,"fb_friends_number": fb_friends_number, "fb_picture": fb_picture, 'csrfmiddlewaretoken': getCookie('csrftoken') },
    success: function (data) {
      // alert(data['email']);
      if (data['email'] === '' || data['phone_number'] === '') {
       

       
     
      // alert(typeof(data['email']))
      // alert('succes');
      setTimeout(
  function() 
  {
    $('#hide_group').hide();
    $('#show_group').show();
    $('.loading_white_wall').fadeOut();
    $('.greeting_title_name').html(fb_first_name);
    if(fb_email){ 
     
      $(".email_input").prop("value", fb_email);
    }

    else{

        $(".email_input").prop("placeholder", 'E-mail');
    }


  }, 1000);

       }


     else{
         
         // alert('loged');
        closeNav();


     }  
      
    },
    error : function(data) {
      
      $('#hide_group').hide();
      $('#error_group').show();
      $('.loading_white_wall').fadeOut();

    }


  })



                                  });


                 }





var sendForm;
var tryLoginAgain;

 $(function() {


tryLoginAgain = function() {
      $('#error_group').hide()
      $('#hide_group').fadeIn()
}  

  
// sendForm = function(){

  $('.phone_mail_form_button_div').click(function(){ 

 if($('.phone_input').val() === ""){

         
        $('.phone_input').removeClass('phone_input').addClass('phone_input_error');
        // $( "<span class='validation_error_text'>Електронна адресса обов'язкове полє</span>" ).insertAfter( ".phone_input" );

        $('.span_after_phone_input').html("<span class='validation_error_text'>Телефоний номер обов'язкове полє</span>")
}

 else if($('.email_input').val() === ""){

         
        $('.email_input').removeClass('email_input').addClass('email_input_error');
        // $( "<span class='validation_error_text'>Електронна адресса обов'язкове полє</span>" ).insertAfter( ".phone_input" );

        $('.span_after_email_input').html("<span class='validation_error_text'>Електронна адресса обов'язкове полє</span>")
}

else{

var phone_number = $('.phone_input').val()
var email = $('.email_input').val() 


  $.ajax({
    url: '/authsteptwo/',
    type:"POST",
    dataType: 'json',
    data: { 'phone_number' : phone_number, 'email' : email, 'csrfmiddlewaretoken': getCookie('csrftoken')  },
    success: function () {
      
      // alert('succes');
      setTimeout(
  function() 
  {
     closeNav();

  }, 0);
      
    },
    error : function() {
      
    
        alert('fck');
    }
   })

   
}




})




$('.logout').click(function(){





FB.logout(function(response) {
 
 window.location.href = '/logout/';
});

  





    VK.Auth.logout(function(){
     window.location.href = '/logout/';
  });


    
  


})


  

$('.navigation_profile_link').click(function(){

  $('#close_nav_trigger').hide();
  $('#hide_group').hide();
  $('.profile').show();
  // $('.dialogs').hide()
 // $('#show_group').hide();

openNav();

})







  });


