from . import STEMP_EPIC_Component
import pandas as pd
import os

def simulation(datafile, vardata, params, init):
    rep = os.path.dirname(datafile)
    out = os.path.join(rep, 'output.csv')
    df = pd.read_csv(datafile, sep = ";")

    # inputs values
    t_RAIN = df[vardata.loc[vardata["Variables"]=="RAIN","Data columns"].iloc[0]].to_list()
    t_NDays = df[vardata.loc[vardata["Variables"]=="NDays","Data columns"].iloc[0]].to_list()
    t_DEPIR = df[vardata.loc[vardata["Variables"]=="DEPIR","Data columns"].iloc[0]].to_list()
    t_TMIN = df[vardata.loc[vardata["Variables"]=="TMIN","Data columns"].iloc[0]].to_list()
    t_WetDay = df[vardata.loc[vardata["Variables"]=="WetDay","Data columns"].iloc[0]].to_list()
    t_BIOMAS = df[vardata.loc[vardata["Variables"]=="BIOMAS","Data columns"].iloc[0]].to_list()
    t_TAMP = df[vardata.loc[vardata["Variables"]=="TAMP","Data columns"].iloc[0]].to_list()
    t_MULCHMASS = df[vardata.loc[vardata["Variables"]=="MULCHMASS","Data columns"].iloc[0]].to_list()
    t_TDL = df[vardata.loc[vardata["Variables"]=="TDL","Data columns"].iloc[0]].to_list()
    t_X2_PREV = df[vardata.loc[vardata["Variables"]=="X2_PREV","Data columns"].iloc[0]].to_list()
    t_DSMID = df[vardata.loc[vardata["Variables"]=="DSMID","Data columns"].iloc[0]].to_list()
    t_TMAX = df[vardata.loc[vardata["Variables"]=="TMAX","Data columns"].iloc[0]].to_list()
    t_TAV = df[vardata.loc[vardata["Variables"]=="TAV","Data columns"].iloc[0]].to_list()
    t_SNOW = df[vardata.loc[vardata["Variables"]=="SNOW","Data columns"].iloc[0]].to_list()
    t_TMA = df[vardata.loc[vardata["Variables"]=="TMA","Data columns"].iloc[0]].to_list()
    t_TAVG = df[vardata.loc[vardata["Variables"]=="TAVG","Data columns"].iloc[0]].to_list()
    t_SRFTEMP = df[vardata.loc[vardata["Variables"]=="SRFTEMP","Data columns"].iloc[0]].to_list()
    t_ST = df[vardata.loc[vardata["Variables"]=="ST","Data columns"].iloc[0]].to_list()
    t_CUMDPT = df[vardata.loc[vardata["Variables"]=="CUMDPT","Data columns"].iloc[0]].to_list()

    #parameters
    BD = params.loc[params["name"]=="BD", "value"].iloc[0]
    DUL = params.loc[params["name"]=="DUL", "value"].iloc[0]
    DS = params.loc[params["name"]=="DS", "value"].iloc[0]
    DLAYR = params.loc[params["name"]=="DLAYR", "value"].iloc[0]
    LL = params.loc[params["name"]=="LL", "value"].iloc[0]
    SW = params.loc[params["name"]=="SW", "value"].iloc[0]
    NLAYR = params.loc[params["name"]=="NLAYR", "value"].iloc[0]
    NL = params.loc[params["name"]=="NL", "value"].iloc[0]
    ISWWAT = params.loc[params["name"]=="ISWWAT", "value"].iloc[0]

    #initialization

    #outputs
    output_names = ["CUMDPT","DSMID","TDL","TMA","NDays","WetDay","X2_PREV","SRFTEMP","ST"]

    df_out = pd.DataFrame(columns = output_names)
    for i in range(0,len(df.index)-1):
        RAIN = t_RAIN[i]
        NDays = t_NDays[i]
        DEPIR = t_DEPIR[i]
        TMIN = t_TMIN[i]
        WetDay = t_WetDay[i]
        BIOMAS = t_BIOMAS[i]
        TAMP = t_TAMP[i]
        MULCHMASS = t_MULCHMASS[i]
        TDL = t_TDL[i]
        X2_PREV = t_X2_PREV[i]
        DSMID = t_DSMID[i]
        TMAX = t_TMAX[i]
        TAV = t_TAV[i]
        SNOW = t_SNOW[i]
        TMA = t_TMA[i]
        TAVG = t_TAVG[i]
        SRFTEMP = t_SRFTEMP[i]
        ST = t_ST[i]
        CUMDPT = t_CUMDPT[i]
        CUMDPT,DSMID,TDL,TMA,NDays,WetDay,X2_PREV,SRFTEMP,ST= STEMP_EPIC_Component.model_stemp_epic_(BD,RAIN,NDays,DEPIR,TMIN,WetDay,DUL,BIOMAS,DS,TAMP,DLAYR,MULCHMASS,LL,TDL,X2_PREV,SW,DSMID,NLAYR,TMAX,TAV,SNOW,TMA,TAVG,SRFTEMP,ST,NL,ISWWAT,CUMDPT)

        df_out.loc[i] = [CUMDPT,DSMID,TDL,TMA,NDays,WetDay,X2_PREV,SRFTEMP,ST]
    df_out.insert(0, 'date', pd.to_datetime(df.year*10000 + df.month*100 + df.day, format='%Y%m%d'), True)
    df_out.set_index("date", inplace=True)
    df_out.to_csv(out, sep=";")
    return df_out