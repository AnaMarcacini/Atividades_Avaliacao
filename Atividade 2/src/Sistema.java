import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Sistema {
    public static void run(){


        System.out.println("Boas Vindas");

        boolean horarioDeTrabalho = true;

        LinkedList<Hackers> funcinarios = new LinkedList<Hackers>();
        funcinarios.add(new ScriptGuys("Ana", "email"));
        funcinarios.add(new BigBrothers("Ana1", "email"));
        funcinarios.add(new HeavyLifters("Ana2", "email"));
        funcinarios.add(new MobileMembers("Ana3", "email"));
        funcinarios.remove(4);

        for (Hackers funcionario : funcinarios){
            funcionario.PostarMensagem(horarioDeTrabalho);
        }


        horarioDeTrabalho = mudarTurno(horarioDeTrabalho);

        for (Hackers funcionario : funcinarios){
            funcionario.PostarMensagem(horarioDeTrabalho);
        }


        horarioDeTrabalho = mudarTurno(horarioDeTrabalho);
        for (Hackers funcionario : funcinarios){
            funcionario.PostarMensagem(horarioDeTrabalho);
        }



    }




    public static Boolean mudarTurno(boolean horario){

        if(horario==true)
            return false;
        return true;
        

    }

}
