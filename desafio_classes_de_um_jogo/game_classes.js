class characterClasses {
    constructor(nome, idade, tipo) {
        this.nome = nome;
        
        if (typeof idade === "number") {
            this.idade = idade;
        }
        else {
            console.log("Insira um valor de idade válido! Apenas números inteiros.");
            console.log(typeof idade);
        }
        
        if (tipo === "guerreiro" || tipo === "mago" || tipo === "monge" || tipo === "ninja") {
            this.tipo = tipo.toLowerCase();
        }
    }

    atacar() {
        let ataqueTipo;

        if (this.tipo === "guerreiro") {
            ataqueTipo = "espada";
        }

        if (this.tipo === "mago") {
            ataqueTipo = "magia";
        }

        if (this.tipo === "monge") {
            ataqueTipo = "artes marciais";
        }

        if (this.tipo === "ninja") {
            ataqueTipo = "shuriken";
        }

        console.log(`O ${this.tipo} atacou usando ${ataqueTipo}`);
    }
}

let character1 = new characterClasses("Elliot", 24, "guerreiro");
let character2 = new characterClasses("Morgana", 21, "mago");
let character3 = new characterClasses("Gray", 30, "monge");
let character4 = new characterClasses("Rikimaru", 22, "ninja");

console.log(character1);
character1.atacar();

console.log(character2);
character2.atacar();

console.log(character3);
character3.atacar();

console.log(character4);
character4.atacar();