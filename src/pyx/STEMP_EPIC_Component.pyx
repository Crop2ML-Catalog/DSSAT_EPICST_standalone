from datetime import datetime
from math import *
from DSSAT_EPICST_standalone.stemp_epic import model_stemp_epic
def model_stemp_epic_(float BD[NL],
      float RAIN,
      int NDays,
      float DEPIR,
      float TMIN,
      int WetDay[30],
      float DUL[NL],
      float BIOMAS,
      float DS[NL],
      float TAMP,
      float DLAYR[NL],
      float MULCHMASS,
      float LL[NL],
      float TDL,
      float X2_PREV,
      float SW[NL],
      float DSMID[NL],
      int NLAYR,
      float TMAX,
      float TAV,
      float SNOW,
      float TMA[5],
      float TAVG,
      float SRFTEMP,
      float ST[NL],
      int NL,
      str ISWWAT,
      float CUMDPT):
    CUMDPT, DSMID, TDL, TMA, NDays, WetDay, X2_PREV, SRFTEMP, ST = model_stemp_epic( NL,ISWWAT,BD,DLAYR,DS,DUL,LL,NLAYR,TAMP,RAIN,SW,TAVG,TMAX,TMIN,TAV,CUMDPT,DSMID,TDL,TMA,NDays,WetDay,X2_PREV,SRFTEMP,ST,DEPIR,BIOMAS,MULCHMASS,SNOW)
    return CUMDPT, DSMID, TDL, TMA, NDays, WetDay, X2_PREV, SRFTEMP, ST