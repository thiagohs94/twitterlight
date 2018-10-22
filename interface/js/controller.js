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
			if($('#txtMensagem').length){
				carregarTimeline(id);
			}
			else{
				carregarPosts(id);
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

function carregarTimeline(id){
	console.log("carregarTimeline");
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

function carregarPosts(id){
	console.log("carregarPosts");
    $.ajax({
    	type: "GET",
        url: "http://twitterlight-timelines.herokuapp.com/posts?usuario_id=" + id,
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

function enviarMensagem(id_usuario, texto){
	console.log("enviarMensagem");
    $.ajax({
    	type: "GET",
        url: "http://twitterlight-mensagens.herokuapp.com/enviar?usuario_id=" + id_usuario + "&texto=" + texto,
    	dataType: "json"
    })
	.done(function(data) {
		esconderLoading();
		console.log(data);
		
		if(data.status == 1){
			location.reload(); 	
			/*
			mensagens = data.mensagens;
			console.log("mensagens"); 
			console.log(mensagens);

			for(i=0;i<mensagens.length;i++){
				exibirMensagem(mensagens[i]);
			}*/
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
	template.find("#msg-link-perfil-usuario").attr("href", "./perfil.html?id_usuario="+mensagem.usuario.id);
	template.find("#msg-username").html("@" + mensagem.usuario.username);
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

function botaoEnviarMensagemClick(){
	var id_usuario = localStorage.getItem("user_id");
	var texto = $("#txtMensagem").text();
	
	console.log("enviar mensagem");
	console.log(id_usuario);
	console.log(texto);
	
	enviarMensagem(id_usuario, texto);
}

$(document).ready(function() {
	console.log("start")
	
	$("#txtMensagem" ).click(function() {
		$("#txtMensagem").text("");
	});
	
	//teste
	localStorage.setItem("user_id", 11);
	var user_id = localStorage.getItem("user_id");

	if(!$('#txtMensagem').length && window.location.search != ""){
		var id = window.location.search.substr(1).split("=")[1];
		if(Math.floor(id) == id && $.isNumeric(id)){
			console.log("perfil do user" + id); 
			user_id = id
		}
	}	

	if (user_id != null){
		carregarUsuario(user_id);
	}
})