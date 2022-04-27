public class Conta {
    private int idConta;
    private double saldo;
    private static int totalContas = 0;
    public Conta() {
        this.saldo = 0;//  Tanto faz     saldo = 0;//
        this.idConta = totalContas;//tanto faz --  this.idConta = totalContas;  -- recomendado não misturar ambas no codigo

        totalContas++;//atributo da classe -- não pode this.totalcontas
    }
    public boolean depositar(double valor){
        this.saldo += valor;
        return true;
    }

    public boolean sacar(double valor){
        if(valor > this.saldo)
            return false;
        this.saldo -= valor;
        return true;
    }

    public boolean transferir(double valor, Conta destino){
        if(!sacar(valor))
            return false;
        return destino.depositar(valor);
    }
    public int getIdConta() {
        return idConta;
    }
    public double getSaldo() {
        return saldo;
    }
    @Override
    public String toString() {
        return "Conta [idConta=" + idConta + ", saldo=" + saldo + "]";
    }

    
}
