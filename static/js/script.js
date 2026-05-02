async function gerarSenha() {
    const dados = {
        tamanho: document.getElementById("tamanho").value,
        especiais: document.getElementById("especiais").checked,
        numeros: document.getElementById("numeros").checked,
        minusculas: document.getElementById("minusculas").checked,
        maiusculas: document.getElementById("maiusculas").checked
    };

    const resposta = await fetch("/gerar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
    });

    const resultado = await resposta.json();
    document.getElementById("senhaGerada").value = resultado.senha;
}

function copiarSenha() {
    const campo = document.getElementById("senhaGerada");
    campo.select();
    document.execCommand("copy");
    alert("Senha copiada!");
}
