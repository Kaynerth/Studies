let vitorias;
let ranking;

function calculadoraDeVitorias (vitorias, derrotas) {
    let resultado = vitorias - derrotas;
    return resultado;
}

vitorias = calculadoraDeVitorias(60, 50);

function calculadoraDeRanking (valor) {
    if (valor <= 10) {
        return 'Ferro';
    }
    else if (valor > 10 && valor <= 20) {
        return 'Bronze';
    }
    else if (valor > 20 && valor <= 50) {
        return 'Prata';
    }
    else if (valor > 50 && valor <= 80) {
        return 'Ouro';
    }
    else if (valor > 80 && valor <= 90) {
        return 'Diamante';
    }
    else if (valor > 90 && valor <= 100) {
        return 'Lendário';
    }
    else {
        return 'Imortal';
    }
}

ranking = calculadoraDeRanking(vitorias);

console.log(`O Herói tem de saldo de ${vitorias} está no nível de ${ranking}`);