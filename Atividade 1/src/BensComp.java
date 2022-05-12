import javax.print.DocFlavor.STRING;
import javax.swing.tree.VariableHeightLayoutCache;

public class BensComp {
    private int id;
    protected float custoH;
    protected String tipo;
    

    public BensComp(int id) {
        this.id = id;
    }

    //@Override
    public String TestarVeiculo() {
        return "BensComp [custoH=" + custoH + ", id=" + id + ", tipo=" + tipo + "]";
    }

    public float getCustoH() {
        return custoH;
    }

    public void setCustoH(float custoH) {
        this.custoH = custoH;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getId() {
        return id;
    }



    
}
