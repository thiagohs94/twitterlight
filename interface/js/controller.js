//timeline
var mensagens = [];

function carregarMensagens(id){
    $.ajax({
    	type: "GET",
        url: "http://0.0.0.0:5000/home?usuario_id=" + id,
    	dataType: "json"
    })
	.done(function(data) {
		console.log(data);
		if(data.status == 1 && data.hasOwnProperty("mensagens")){
			mensagens = data.mensagens;
			console.log("mensagens"); 
			console.log(mensagens);

			for(i=0;i<mensagens.length;i++){
				exibirMensagem(mensagens[i]);
			}
		}
		else{
			return null;
		}
	})
	.fail(function(data) {
		console.log(data);
		return null;
	})
}

function exibirMensagem(mensagem){
	//$("#main-timeline").append("olar");
	var template = $("#template-mensagem").clone(true).attr("id", "msg-" + mensagem.id);
	template.find("#msg-usuario").html(mensagem.usuario.nome);
	template.find("#msg-texto").html(mensagem.texto);
    $("#main-timeline").append(template);
    $("#msg-" + mensagem.id).show();
}

$(document).ready(function() {
	var user_id = localStorage.getItem("user_id");

	if (user_id != null){
		carregarMensagens(user_id);
	}
})