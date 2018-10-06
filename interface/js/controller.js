$(document).ready(function() {
    $.ajax({
    	type: "GET",
        url: "http://twitterlight-timelines.herokuapp.com/posts?usuario_id=11",
    	dataType: "json"
    }).then(function(data) {
    	console.log(data); 	
       	//$('.greeting-id').append(data.id);
       	//$('.greeting-content').append(data.content);
    });
});