public class BigBrothers extends Hackers{
 
    


    public BigBrothers(String nome, String email) {
        super(nome, email);
        //TODO Auto-generated constructor stub
    }







    public Hackers CadastrarMembro(String nome, String email, EnumFuncionarios tipo){
        if(tipo == EnumFuncionarios.BigBrothers){
            Hackers a = new BigBrothers(nome, email);
            return a;
        }
        if(tipo == EnumFuncionarios.HeavyLifters){
            Hackers a = new HeavyLifters(nome, email);
            return a;
        }
        if(tipo == EnumFuncionarios.MobileMembers){
            Hackers a = new MobileMembers(nome, email);
            return a;
        }
    }







    public void PostarMensagem(boolean hora) {
        if(hora)
        System.out.println("“Sempre ajudando as pessoas membros ou não S2!” ");
        else{

        System.out.println("...");
        }
    }
}