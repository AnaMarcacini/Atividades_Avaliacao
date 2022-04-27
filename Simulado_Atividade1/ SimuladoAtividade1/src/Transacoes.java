

public class Transacoes {
    // public Transacoes(Conta receber, Conta retirar,Conta quantidade){
    //     this.receber.numero = receber.numero;
    // }


       //Métodos da classe
       public String visualizarSaldo(Conta ver){
        return("Nome do usuario " + ver.nome+ " - Saldo: R$" + ver.saldo);
    }

    public String NotaRecebe(Conta ver, double valor){
        return("Nome do usuario " + ver.nome+ " - Saldo: R$" + ver.saldo);
    }
    public String NotaDeQuem(Conta ver){
        return("Do " + ver.nome);
    }




    public boolean depositar(double valor, Conta dep){
        if(valor < 0) 
            return false;
        dep.saldo += valor;
        return true;
    }
    public boolean sacar(double valor, Conta sac){
        if(valor > sac.saldo) return false;
        if(valor < 0) return false;
        sac.saldo -= valor;
        return true;
    }
    public boolean transferirDinheiro(double valor,Conta retirar, Conta destino){
        if(!sacar(valor,retirar)) return false;
        if(depositar(valor,destino))return false;
        return true;
    }


    // public boolean transferirDinheiro(double valor, Conta destino){
    //     if(!sacar(valor)) return false;
    //     if(!destino.depositar(valor)) return false;
    //     return true;
    // }

}
