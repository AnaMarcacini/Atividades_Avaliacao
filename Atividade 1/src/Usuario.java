public class Usuario {
    private String nome;
    private BensComp veiculo;
    private int contador =0;



    public Usuario(String nome, BensComp veiculo) {
        this.nome = nome;
        this.veiculo = veiculo;
    }
    


    public Boolean Trocar(String b1){
        contador = contador+1;

        if (b1 == "Bicicleta"){
            Bicicleta b2 = new Bicicleta(1234);

            this.veiculo = b2;
            return true;
        }
        if (b1 == "Carro"){
            Carro b2 = new Carro(1234);

            this.veiculo = b2;
            return true;
        }
        if (b1 == "Patinete"){
            Patinete b2 = new Patinete(1234);

            this.veiculo = b2;
            return true;
        }
        if (b1 == "Moto"){
            Moto b2 = new Moto(1234);

            this.veiculo = b2;
            return true;
        }
        contador = contador-1;

        return false;
    }

        // BensComp aux = new BensComp(a2.veiculo.getId());


        // aux.setID(id); = this.a1.veiculo;
        // a1.veiculo = a2.veiculo;
        // a2.veiculo = aux;



        public String Testar() {
            return " O usuario "+ nome +" Possui um(a) " + veiculo.getTipo() + " com um custo de " + veiculo.getCustoH() + " de id igual à " + veiculo.getId() + "\n\n Contador de trocas = "+contador;

    }
}
