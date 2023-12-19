$(document).ready(function () {
  $("#form").on("submit", function(event){
    event.preventDefault();
    const form_data = new FormData(this);
    $("#answer").html("");
    $.ajax({
      type: "POST",
      url: form_data.get("url"),
      data: form_data,
      processData: false,
      contentType: false,
      success:function(data){
        $("#answer").html(data);
      },
      error: function(jqXHR, textStatus, errorThrown) {
        console.error(textStatus, errorThrown);
        $("#answer").html(textStatus + errorThrown);
      },
    });
  });
});
