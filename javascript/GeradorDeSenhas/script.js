function GerarSenha() {
    tamanho = document.querySelector('#tamanho').value
    resultadoDiv = document.querySelector('#resultado')
    caracteres ='!@#$%&*qwertyuiopasdfghjklzxcvbnm'
    senha = ''
    
    for (var i = 0; i < tamanho; i++) {
        var randomNumber = Math.floor(Math.random() * caracteres.length);
        senha += caracteres.substring(randomNumber, randomNumber + 1);
    }
    console.log(senha)

    resultadoDiv.innerHTML = senha
}