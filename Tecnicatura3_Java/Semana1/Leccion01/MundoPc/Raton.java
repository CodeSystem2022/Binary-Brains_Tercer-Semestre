// Clase hija Raton

package ar.com.system2023.mundopc;
public class Raton extends DispositivosEntrada {
    
    private static int contadorRatones;
    private final int idRaton;

    public Raton(String marca, String tipoEntrada) {
        super(marca, tipoEntrada);
        this.idRaton = ++Raton.contadorRatones;
    }
    
    // Metodo Set y Get ID
    public void setContadorRatones (int contadorRatones){
        this.contadorRatones = contadorRatones;
    }
    
    public int getContadorRatones(){
        return this.contadorRatones;
    }
    
    public int getIdRaton(){
        return idRaton;
    }
    
    @Override
    public String toString(){
        return "Raton{" + " Id# " + idRaton  + ". "+ super.toString() + " }";
    } 
}
