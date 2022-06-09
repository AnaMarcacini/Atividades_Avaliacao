
public class Hackers implements InterfaceHackers{

    protected String nome;
    protected String email;
    //protected EnumFuncionarios tipo;
    //protected boolean horarioDeTrabalho;

    //protected String[] funções;


    public Hackers(String nome, String email) {
        this.nome = nome;
        this.email = email;
    }

    public void PostarMensagem(boolean hora) {

    }

    @Override
    public String toString() {
        return "Hackers [email=" + email + ", nome=" + nome + "]";
    }

    // @Override
    // public void PostarMensagem() {
    //     //System.out.println("Bom dia "+ this.nome +"\n Segue a baixo os dados do seu usuário");
    //     //System.out.println(toString()+ \n "Happy Coding");
        
    // }




}
