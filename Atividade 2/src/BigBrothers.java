public class BigBrothers extends Hackers{
 
    


    public BigBrothers(String nome, String email) {
        super(nome, email);
        //TODO Auto-generated constructor stub
    }







    public Hackers CadastrarMembro(String nome, String email){
        Hackers a = new Hackers(nome, email);
        return a;

    }







    public void PostarMensagem(boolean hora) {
        if(hora)
        System.out.println("“Sempre ajudando as pessoas membros ou não S2!” ");
        else{

        System.out.println("...");
        }
    }
}