$("#answer").hide();
var nIntervId;

function check_task(task_url) {
  $.ajax({
    type: "get",
    url: task_url,
    processData: false,
    contentType: false,
    success:function(data){
      if (data['job_status'] == "finished") {
        $("#answer").show();
        for (var key in data['result']){
          var value = data['result'][key];
          $('#' + key).text(value);
        }
        clearInterval(nIntervId);
      }
    },
  });
}


$(document).ready(function () {
  $("#form").on("submit", function(event){
    event.preventDefault();
    const form_data = new FormData(this);
    $("#answer").hide();
    $.ajax({
      type: "POST",
      url: form_data.get("url"),
      data: form_data,
      processData: false,
      contentType: false,
      success:function(data){
        if ('job_url' in data) {
          nIntervId = setInterval(check_task, 1000, (data["job_url"]));
        }
      },
      error:function(jqXHR, textStatus, errorThrown) {
        console.error(textStatus, errorThrown);
        $("#answer").html(jqXHR + textStatus + errorThrown);
      },
    });
  });
});