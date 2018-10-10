//timeline
var mensagens = [];

function carregarUsuario(id){
	console.log("carregarUsuario");
	exibirLoading();
    $.ajax({
    	type: "GET",
        url: "http://twitterlight-usuarios.herokuapp.com/perfil?usuario_id=" + id,
    	dataType: "json"
    })
	.done(function(data) {
		console.log(data);
		if(data.status == 1 && data.hasOwnProperty("usuario")){
			exibirInfoUsuario(data.usuario);
			carregarMensagens(id);
		}
		else{
			return null;
		}
	})
	.fail(function(data) {
		esconderLoading();
		console.log(data);
		return null;
	})
}

function carregarMensagens(id){
	console.log("carregarMensagens");
    $.ajax({
    	type: "GET",
        url: "http://twitterlight-timelines.herokuapp.com/home?usuario_id=" + id,
    	dataType: "json"
    })
	.done(function(data) {
		esconderLoading();
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
		esconderLoading();
		console.log(data);
		return null;
	})
}

function exibirInfoUsuario(usuario){
    $("#nome-usuario").append(usuario.nome);
    $("#username-usuario").append("@" + usuario.username);
    $("#bio-usuario").append(usuario.bio);
}

function exibirMensagem(mensagem){
	//$("#main-timeline").append("olar");
	var template = $("#template-mensagem").clone(true).attr("id", "msg-" + mensagem.id);
	template.find("#msg-usuario").html(mensagem.usuario.nome);
	template.find("#msg-texto").html(mensagem.texto);
    $("#main-timeline").append(template);
    $("#msg-" + mensagem.id).show();
}

function exibirLoading(){
	$('.overlay').show();
    $('.loading').show();
}

function esconderLoading(){
	$('.overlay').hide();
    $('.loading').hide();
}

$(document).ready(function() {
	console.log("start")
	var user_id = localStorage.getItem("user_id");

	if (user_id != null){
		carregarUsuario(user_id);
	}
})