$("#answer").hide();
var check_task_IntervId;
var server_status_IntervId;

function server_status() {
  $.ajax({
    type: "get",
    url: "server_status",
    processData: false,
    contentType: false,
    success:function(data){
      if (data['server_status'] == "ok") {
        $('#server_status').css('color', 'green');
        $('#server_status').text('OK');
        $('#task_queue').css('color', 'green');
        $('#task_queue').text(data['task_queue']);
      }
      else {
        $('#server_status').css('color', 'red');
        $('#server_status').text('Error');
        $('#task_queue').css('color', 'red');
        $('#task_queue').text(data['task_queue']);
      };
    },
    error:function(jqXHR, textStatus, errorThrown) {
      $('#server_status').css('color', 'red');
      $('#server_status').text('Error');
      $('#task_queue').css('color', 'red');
      $('#task_queue').text(data['task_queue']);
    },
  });
};

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
        };
        if (data['result'].hasOwnProperty("filename")) {
          $('#image').prepend('<img class="pure-img" src="' + data['result']['filename'] + '" />');
        };
        clearInterval(check_task_IntervId);
      };
    },
  });
};


$(document).ready(function () {
  $("#form_1").on("submit", function(event){
    event.preventDefault();
    const form_data = new FormData(this);
    $("#answer").hide();
    $("#image").empty();
    $.ajax({
      type: "POST",
      url: form_data.get("url"),
      data: form_data,
      processData: false,
      contentType: false,
      success:function(data){
        if ('job_url' in data) {
          check_task_IntervId = setInterval(check_task, 1000, (data["job_url"]));
        };
      },
      error:function(jqXHR, textStatus, errorThrown) {
        $("#answer").html(jqXHR + textStatus + errorThrown);
      },
    });
  });
});

$(document).ready(function () {
  server_status_IntervId = setInterval(server_status, 5000);
});
