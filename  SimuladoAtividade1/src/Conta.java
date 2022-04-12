public class Conta {
    //Atributos da nossa classe
    // sei que era para fazer get mas n tive tempo
    public int numero;
    public double saldo;
    public String nome;

    public Conta(String nome, double saldo){
        this.saldo = saldo;
        this.nome = nome;
    }

    // //Métodos da classe
    // public void visualizarSaldo(){
    //     System.out.println("Saldo atual na conta " + numero+ ": R$" + saldo);
    // }
    // public boolean depositar(double valor){
    //     if(valor < 0) 
    //         return false;
    //     this.saldo += valor;
    //     return true;
    // }
    // public boolean sacar(double valor){
    //     if(valor > saldo) return false;
    //     if(valor < 0) return false;
    //     this.saldo -= valor;
    //     return true;
    // }
    // public boolean transferirDinheiro(double valor, Conta destino){
    //     if(!sacar(valor)) return false;
    //     if(!destino.depositar(valor)) return false;
    //     return true;
    // }
}