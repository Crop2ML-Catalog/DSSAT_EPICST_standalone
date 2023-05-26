public class STEMP_EPIC_Component
{
    
    public STEMP_EPIC_Component() { }

    STEMP_EPIC _STEMP_EPIC = new STEMP_EPIC();

    public Double [] getBD()
    { return _STEMP_EPIC.getBD(); }
    public void setBD(Double [] _BD){
    _STEMP_EPIC.setBD(_BD);
    }

    public Double [] getDUL()
    { return _STEMP_EPIC.getDUL(); }
    public void setDUL(Double [] _DUL){
    _STEMP_EPIC.setDUL(_DUL);
    }

    public Double [] getDS()
    { return _STEMP_EPIC.getDS(); }
    public void setDS(Double [] _DS){
    _STEMP_EPIC.setDS(_DS);
    }

    public Double [] getDLAYR()
    { return _STEMP_EPIC.getDLAYR(); }
    public void setDLAYR(Double [] _DLAYR){
    _STEMP_EPIC.setDLAYR(_DLAYR);
    }

    public Double [] getLL()
    { return _STEMP_EPIC.getLL(); }
    public void setLL(Double [] _LL){
    _STEMP_EPIC.setLL(_LL);
    }

    public Double [] getSW()
    { return _STEMP_EPIC.getSW(); }
    public void setSW(Double [] _SW){
    _STEMP_EPIC.setSW(_SW);
    }

    public Integer getNLAYR()
    { return _STEMP_EPIC.getNLAYR(); }
    public void setNLAYR(Integer _NLAYR){
    _STEMP_EPIC.setNLAYR(_NLAYR);
    }

    public Integer getNL()
    { return _STEMP_EPIC.getNL(); }
    public void setNL(Integer _NL){
    _STEMP_EPIC.setNL(_NL);
    }

    public String getISWWAT()
    { return _STEMP_EPIC.getISWWAT(); }
    public void setISWWAT(String _ISWWAT){
    _STEMP_EPIC.setISWWAT(_ISWWAT);
    }
    public void  Calculate_Model(STEMP_EPIC_State s, STEMP_EPIC_State s1, STEMP_EPIC_Rate r, STEMP_EPIC_Auxiliary a, STEMP_EPIC_Exogenous ex)
    {
        _STEMP_EPIC.Calculate_Model(s, s1, r, a, ex);
    }
    private Double [] BD;
    private Double [] DUL;
    private Double [] DS;
    private Double [] DLAYR;
    private Double [] LL;
    private Double [] SW;
    private Integer NLAYR;
    private Integer NL;
    private String ISWWAT;
    public STEMP_EPIC_Component(STEMP_EPIC_Component toCopy) // copy constructor 
    {
        
        for (int i = 0; i < toCopy.getBD().length; i++)
        {
            BD[i] = toCopy.getBD()[i];
        }
        
        for (int i = 0; i < toCopy.getDUL().length; i++)
        {
            DUL[i] = toCopy.getDUL()[i];
        }
        
        for (int i = 0; i < toCopy.getDS().length; i++)
        {
            DS[i] = toCopy.getDS()[i];
        }
        
        for (int i = 0; i < toCopy.getDLAYR().length; i++)
        {
            DLAYR[i] = toCopy.getDLAYR()[i];
        }
        
        for (int i = 0; i < toCopy.getLL().length; i++)
        {
            LL[i] = toCopy.getLL()[i];
        }
        
        for (int i = 0; i < toCopy.getSW().length; i++)
        {
            SW[i] = toCopy.getSW()[i];
        }
        this.NLAYR = toCopy.getNLAYR();
        this.NL = toCopy.getNL();
        this.ISWWAT = toCopy.getISWWAT();

    }
}