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
    		success:function(data, textStatus, jqXHR){
    			$("#answer").html(data);
		    },
		});
	});
});
