//Ana Helena Marcacini 20.01305-0

public class Atividade1 {
    public static void run(){
    Moto m1 = new Moto(1234);
        Bicicleta b1 = new Bicicleta(1234);
        //Carro c1 = new Carro(1234);
        //Patinete p1 = new Patinete(1234);
        
        Usuario a1 = new Usuario("Ana",m1);
        Usuario a2 = new Usuario("AnaH",b1);
        System.out.println("Antes da troca ________________________________________________________________________________________________________________________________________________________________________________");

        System.out.println(a1.Testar());
        System.out.println(a2.Testar());



        System.out.println("Depois da troca ________________________________________________________________________________________________________________________________________________________________________________");

        if(a1.Trocar("Carro")){
            System.out.println("Troca realizada com sucesso \n estado atual do usuario");
            System.out.println(a1.Testar());
        }
        else{
            System.out.println("erro na troca");
        }


        if(a2.Trocar("Moto")){
            System.out.println("Troca realizada com sucesso \n estado atual do usuario");
            System.out.println(a2.Testar());


        }
        else{
            System.out.println("erro na troca");
        }


        System.out.println("Depois da troca 2º troca________________________________________________________________________________________________________________________________________________________________________________");



        if(a1.Trocar("Patinete")){
            System.out.println("Troca realizada com sucesso \n estado atual do usuario");
            System.out.println(a1.Testar());
        }
        else{
            System.out.println("erro na troca");
        }

        if(a2.Trocar("Moto")){
            System.out.println("Troca realizada com sucesso \n estado atual do usuario");
            System.out.println(a2.Testar());


        }
        else{
            System.out.println("erro na troca");
        }




    }
}
