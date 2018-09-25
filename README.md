# twitterlight

Engenharia de Software II - UFMG - 2018/2 - Trabalho Prático

Parte 3: Módulos principais de uma rede social simples - Twitter Light

Semelhante às primeiras versões do Twitter; com mensagens apenas textuais, limitadas
a 140 caracteres.
Módulos/microserviços a serem implementados:

(1) Users:
- login, internal_id, full name, followers, following, short bio
- cadastrar
- remover (sair da rede social)
- seguir um dado usuário (dado o seu ID)
- parar de seguir um dado usuário (dado o seu ID)

(2) Mensagens:
- internal_id (da mensagem), ID do usuário que postou, texto
- postar mensagem
- recuperar msg dado seu ID

(3) Timelines: 
- Posts: dado um ID de um usuário, retorna uma lista com suas msg
- Home: dado um ID de um usuário, retorna uma lista com suas msgs e de todos os usuários que ele segue

Documente um conjunto de URLs que podem ser chamadas em um browser para teste do sistema (será feita uma demonstração em sala de aula).

O código deverá estar no GitHub (um diretório para cada microserviço).
