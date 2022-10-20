$("form[name=signup_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/client/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/dashboard/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/client/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      if(resp.role == "admin"){
        window.location.href = "/userdashboard/";
      }
      else{
        window.location.href = "/userdashboard/";
      }
      
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});