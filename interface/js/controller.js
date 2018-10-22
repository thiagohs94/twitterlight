//timeline
var mensagens = [];

function cadastrar(nome, bio, usuario, senha){
	console.log("cadastrar");
	exibirLoading();
    $.ajax({
    	type: "GET",
        url: "http://twitterlight-usuarios.herokuapp.com/cadastro?username=" + nome + "&senha=" + senha + "&nome=" + nome + "&bio=" + bio, 
    	dataType: "json"
    })
	.done(function(data) {
		console.log(data);
		if(data.status == 1 && data.hasOwnProperty("usuario")){
			esconderLoading();
			alert("Usuário Cadastrado");
			localStorage.setItem("user_id", data.usuario.id);
			window.location.replace("./timeline.html");
		}
		else{
			esconderLoading();
			alert("Ocorreu um erro ao cadastrar o usuario")
		}
	})
	.fail(function(data) {
		esconderLoading();
		console.log(data);
		return null;
	})
}

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
			if($('#txtMensagem').length){
				console.log("salvar seguindo")
				localStorage.setItem("seguindo", JSON.stringify(data.seguindo));
				console.log(localStorage.getItem("seguindo"));
			}
			exibirInfoUsuario(data.usuario);
			if($('#txtMensagem').length){
				carregarTimeline(id);
			}
			else{
				carregarPosts(id);
			}
		}
		else{
			esconderLoading();
			alert("Conta não encontrada");
			window.location.replace("./index.html");  	
		}
	})
	.fail(function(data) {
		esconderLoading();
		alert("Conta não encontrada");
		window.location.replace("./index.html");  	
		console.log(data);
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

function seguir(id_seguidor, id_seguido){
	console.log("enviarMensagem");
	exibirLoading();
    $.ajax({
    	type: "GET",
        url: "http://twitterlight-usuarios.herokuapp.com/seguir?seguidor=" + id_seguidor + "&seguido=" + id_seguido,
    	dataType: "json"
    })
	.done(function(data) {
		esconderLoading();
		console.log(data);
		
		if(data.status == 1){
			alert("Você está seguindo o usuário");
			window.location.replace("./timeline.html");  	
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

function pararSeguir(id_seguidor, id_seguido){
	console.log("enviarMensagem");
	exibirLoading();
    $.ajax({
    	type: "GET",
        url: "http://twitterlight-usuarios.herokuapp.com/pararseguir?seguidor=" + id_seguidor + "&seguido=" + id_seguido,
    	dataType: "json"
    })
	.done(function(data) {
		esconderLoading();
		console.log(data);
		
		if(data.status == 1){
			alert("Você parou de seguir o usuário");
			window.location.replace("./timeline.html"); 	
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

function excluirConta(id_usuario){
	console.log("excluirConta");
	exibirLoading();
    $.ajax({
    	type: "GET",
        url: "http://twitterlight-usuarios.herokuapp.com/remover?usuario_id=" + id_usuario, 
    	dataType: "json"
    })
	.done(function(data) {
		console.log(data);
		if(data.status == 1){
			esconderLoading();
			alert("Conta excluída");
			window.location.replace("./index.html");
		}
		else{
			esconderLoading();
			alert("Ocorreu um erro ao excluir a conta")
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

    if(localStorage.getItem("user_id") != usuario.id){
		//verificar se usuario segue ou nao
    	var seguindo = JSON.parse(localStorage.getItem("seguindo"));
    	var seg = false;

    	console.log("seguindo");
    	console.log(seguindo);
    	for(var i=0;i<seguindo.length;i++){
    		console.log(seguindo[i].id);
    		if(seguindo[i].id == usuario.id){
    			seg = true;
    			break;
    		}
    	}

    	if(seg == true){
    		console.log("seguindo" + usuario.id);
			$("#btn-follow").hide();
    		$("#btn-unfollow").show();
    	}
    	else{
    		console.log("não seguindo" + usuario.id);
    		$("#btn-follow").show();
    		$("#btn-unfollow").hide();
    	}
    	
    }
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

function botaoLoginClick(){
	var usuario = $("#usuario-login").val();
	if(usuario != "" && $.isNumeric(usuario)){
		localStorage.setItem("user_id", usuario);
		window.location.replace("./timeline.html");	
	}
	else{
		alert("Identifique o usuário");
	}
}

function botaoCadastroClick(){
	window.location.replace("./cadastro.html");		
}

function botaoCadastrarClick(){
	var nome = $("#nome-cadastro").val();
	var bio = $("#bio-cadastro").val();
	var usuario = $("#usuario-cadastro").val();
	var senha = $("#senha-cadastro").val();

	if(nome != "" && bio != "" && usuario != "" && senha != ""){
		cadastrar(nome, bio, usuario, senha);	
	}
	else{
		alert("Todos os campos são obrigatórios");
	}	
}

function botaoEnviarMensagemClick(){
	var id_usuario = localStorage.getItem("user_id");
	var texto = $("#txtMensagem").text();
	
	console.log("enviar mensagem");
	console.log(id_usuario);
	console.log(texto);
	
	enviarMensagem(id_usuario, texto);
}

function botaoSeguirClick(){
	var id_seguidor = localStorage.getItem("user_id");
	var id_seguido = localStorage.getItem("id_usuario_perfil");

	seguir(id_seguidor, id_seguido);
}

function botaoPararSeguirClick(){
	var id_seguidor = localStorage.getItem("user_id");
	var id_seguido = localStorage.getItem("id_usuario_perfil");

	pararSeguir(id_seguidor, id_seguido);
}

function excluirContaClick(){
	var id = localStorage.getItem("user_id");

	if(confirm('Tem certeza que deseja excluir a conta?')){
		excluirConta(id);
	}
}

$(document).ready(function() {
	console.log("start")
	
	$("#txtMensagem" ).click(function() {
		$("#txtMensagem").text("");
	});
	
	var user_id = localStorage.getItem("user_id");

	if($('#perfil').length && window.location.search != ""){
		var id = window.location.search.substr(1).split("=")[1];
		if(Math.floor(id) == id && $.isNumeric(id)){
			console.log("perfil do user" + id); 
			user_id = id
			localStorage.setItem("id_usuario_perfil", user_id); 
		}
	}	

	if($('#perfil').length || $('#timeline').length){
		if (user_id != null){
			console.log("carregar usuario" + user_id);
			carregarUsuario(user_id);
		}
	}
})