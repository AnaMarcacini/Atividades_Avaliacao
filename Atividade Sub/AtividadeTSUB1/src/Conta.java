public class Conta {
    //atributos da nossa classe
    private int numero;
    private String titular;
    private double saldo;
    private String cpf;

//metodos da classe

void visualizarSaldo(){

    System.out.println("Saldo atual na conta " + numero +": R$" + saldo);
}


Boolean depositar(double valor){


    if(valor < 0)return false;
    this.saldo+=valor;
    return true;



}



Boolean sacar(double valor){

    if(valor > saldo || valor < 0) return false;
    saldo = saldo - valor;
    return true;



}
Boolean transferirDinheiro(double valor, Conta destino){
    if(!sacar(valor)) return false;
    if(!destino.depositar(valor)) return false;
    return true;

}
    
}
