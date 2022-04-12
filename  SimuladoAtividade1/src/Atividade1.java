public class Atividade1 {
    public void run(){
        //codigo principal
        Conta conta1 = new Conta("Ana",1000);
        Conta conta2 = new Conta("Helena", 250);
        Conta conta3 = new Conta("Marcacini", 3000);
        Transacoes t = new Transacoes();

        System.out.println("Estado Inicial");
        System.out.println(""+ t.visualizarSaldo(conta1));

        System.out.println(t.visualizarSaldo(conta2));

        System.out.println(t.visualizarSaldo(conta3));



        System.out.println("Notas Fiscais");
        //        t.transferirDinheiro(valor, retirar, destino)
        
        t.transferirDinheiro(250, conta2, conta1);
        System.out.println(""+t.NotaRecebe(conta1, 250)+ t.NotaDeQuem(conta2));

        t.transferirDinheiro(250, conta3, conta1);
        System.out.println(""+t.NotaRecebe(conta1, 250)+ t.NotaDeQuem(conta3));

        t.transferirDinheiro(250, conta2, conta1);
        System.out.println(""+t.NotaRecebe(conta1, 250)+ t.NotaDeQuem(conta2));


        t.transferirDinheiro(1000, conta3, conta2);
        System.out.println(""+t.NotaRecebe(conta2, 250)+ t.NotaDeQuem(conta3));

        System.out.println("Estado Final");
        System.out.println(""+t.visualizarSaldo(conta1));

        System.out.println(""+t.visualizarSaldo(conta2));

        System.out.println(""+t.visualizarSaldo(conta3));


    }
    //funções


}