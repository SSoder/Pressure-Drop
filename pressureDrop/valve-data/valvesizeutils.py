"""
User Defined Functions for the Valve Sizing Spreadsheet.
Functions written by Stefan Soder
Last Updated: 2016-07-29
"""
from iapws import IAPWS97
import pandas as pd
import math as m
import re

#Written by Stefan Soder, 2018-02-02 Last UpdateL 2018-05-01
def seatID(valvecode, valvesize, pressureclass, bonnettype):
    if valvecode == '' or None:
        return('N/A, valvecode')
    elif valvesize == '' or None:
        return('N/A, valvesize')
    elif pressureclass == '' or None:
        return('N/A, pressureclass')
    elif bonnettype == '' or None:
        return('N/A, bonnettype')
    with open('valveData.csv') as datafile:
        df1 = pd.read_csv(datafile)
    df1 = df1.set_index('valveSize')
    ValveCodeCheck = [1,3,5,9,11,17,18,28,29,30]
    BBClassCheck = [125,150,300,400,600,900,1500,2500]
    PSClassCheck = [600,900,1500,2000,2500,4500]
    if pressureclass is not None:
        pressureclass = int(pressureclass)
    if valvecode is not None and valvecode not in ValveCodeCheck:
        return('This Function only returns seatID of gates, globes, & swing checks. Please check your valve code or edit this function.')
    if valvesize not in df1.index.values:
        return('Double check your valve size!')
    bonnettest = '^(b*B?B?b?)(P*p?S?s?)'
    bonnetverify = re.search(bonnettest,bonnettype)
    bonnetverifygroups = bonnetverify.groups()
    if bonnettype not in bonnetverifygroups:
        return('You have not entered a valid bonnet design type. Please enter "BB" for Bolted Bonnet or "PS" for a Pressure Seal bonnet.')
    if bonnettype == bonnetverifygroups[1]:
        if pressureclass not in PSClassCheck:
            return('Powell Pressure Seal valves are only made in Class 600, 900, 1500, 2500, & 4500. Please Validate your presssure class and try again.')
        elif valvecode == 1:
            columnlocate = 'PSGate'+str(pressureclass)
        elif valvecode == 5:
            columnlocate = 'PSYGlobe'+str(pressureclass)
        elif valvecode == 17:
            columnlocate = 'PSYGlobe'+str(pressureclass)
        elif valvecode == 28:
            columnlocate == 'PSNRGlobe' + str(pressureclass)
        else:
            columnlocate = 'PSGlobe'+str(pressureclass)
    elif bonnettype == bonnetverifygroups[0]:
        if pressureclass not in BBClassCheck:
            return('Please double check your pressure class and try again.')
        else:
            columnlocate = 'BBClass'+str(pressureclass)
    rowlocate = valvesize
    seatID = df1.loc[rowlocate,columnlocate]
    return(seatID)


#Written by Stefan Soder,2016-07-25 Last Update: 2018-05-01
def SteamType(pressure, temperature):
    
    #Convert psi to MPa; IAPWS97 object requires SI units    
    pressure = (pressure +14.7) * 0.006895
    #Convert Fahrenheit to Kelvin; IAPWS97 object requires SI units
    temperature = (((temperature-32)/1.8)+273)
    #Round the temperature to the nearest whole number.
    temperature = int(round(temperature))
    #Establishes an empty string to fill with the return value.
    fluid = ""
    #Instantiation of the steam object; assumes saturated steam.
    steam = IAPWS97(P=pressure, x=1)
    #Determines the saturation temperature of the steam.
    satsteamtemp = int(round(steam.T))
    """
    The logic below is to define the type of steam being used in the 
    customer's service. It assumes that the steam is saturated, and determines
    by the first if clause whether or not that is the case.
    It does so by comparing a ratio of the given line temperature to the
    saturation temperature determined above. If that ratio=1, then it is exactly
    the saturation temperature. The logic allows for a ratio right around one
    because customers are rarely going to give the perfect temperature for
    saturated steam at their pressure.
    """
    if 0.995 < temperature / satsteamtemp and temperature / satsteamtemp < 1.01:
            fluid = "Saturated Steam"
    elif 1.01 < temperature / satsteamtemp :
            fluid = "Superheated Steam"
    elif pressure > 22:
            fluid = "Supercritical Steam"
    else:   
        fluid = "Water"
    
    return(fluid)

#Written by Stefan Soder,2016-07-25 Last Update: 22018-05-01
def SteamVolume(steamtype,pressure,temperature):
    #Initialize the volume variable.
    volume = 0
    #Convert pressure as in the SteamType function.
    pressure = (pressure + 14.7) * 0.006895
    #Convert Temperature as in the SteamType function
    temperature = (((temperature-32)/1.8)+273)
    temperature = int(round(temperature))
    """
    The logic below returns the specific volume attribute of the steam objects
    instatiated, while simultaneously converting them from MPa to psi.
    This is so that the returned value can be utilized correctly in the Valve
    Sizing Excel file.
    """
    if steamtype == "Saturated Steam":
        volsatsteam = IAPWS97(P=pressure, x=1)
        volume = volsatsteam.v * 16.0185
    elif steamtype == "Superheated Steam":
        volshsteam = IAPWS97(P=pressure, T=temperature)
        volume = volshsteam.v * 16.0185
    elif steamtype == "Supercritical Steam":
        volscsteam = IAPWS97(P=pressure, T=temperature)
        volume = volscsteam.v * 16.0185
    elif steamtype == "Water":
        volwater = IAPWS97(T=temperature,x=0)
        volume = volwater.v * 16.0185
    return(volume)
    
#Written by Stefan Soder,2018-03-09 Last Update: 2018-05-01
def SteamRe(steamtype,pressure,temperature,SeatID,massflow):
    """This function calculates the Reynolds number of the flow through the valve
    at the Seat ID. ***NOTE*** THIS IS FOR STEAM ONLY. It calculates via converting
    mass flow to velocity, and water applications use volumetric flow.
    """
    if massflow == '' or None:
        return('N/A, Require massflow')
    while True:
        try:
            SeatID = float(SeatID)
            break
        except ValueError:
            return("Seat ID needs calculated!")
    #Convert pressure as in the SteamType function.
    pressure = (pressure + 14.7) * 0.006895
    #Convert Temperature as in the SteamType function
    temperature = (temperature + 459.67)*(5.0/9.0)
    temperature = int(round(temperature))
    density = 0
    massflow = massflow*(0.454/3600)
    SeatID = SeatID * 0.0254
    """
    The logic below returns the viscosity and density attributes of the steam objects
    instantiated.
    """
    if steamtype == "Saturated Steam":
        satsteam = IAPWS97(P=pressure, x=1)
        steamtest = IAPWS97(P=pressure,T=temperature)
        viscosity = satsteam.mu
        density = satsteam.rho
    elif steamtype == "Superheated Steam" or "Supercritical Steam":
        shsteam = IAPWS97(P=pressure, T=temperature)
        viscosity = shsteam.mu
        density = shsteam.rho
    velocity = (massflow * (1/density))/((m.pi/4)*(SeatID**2))
    Re = (SeatID*density*velocity)/viscosity   
    return Re

#Written by Stefan Soder, 2018-05-01
def GasVolume(molecularweight, pressure, temperature):
    #Calculates the specific volume of a gas of given molecular weight. Uses
    #the ideal gas law to do so
    absoluteRI = 1545.349 # (ft-lbs)/(lbmol*DegR)
    absoluteT = 459.67  # Conversion for Fahrenheit to Rankine
    absoluteP = 14.7    # Conversion to Absolute Pressure from Gage
    #Convert Temperature to Rankin
    temperature = absoluteT + temperature
    pressure = absoluteP + pressure #Determine Absolute Pressure from Gage
    #Calculating the Gas Constant for the given weight
    relativeR = absoluteRI / molecularweight
    #And finally, calculate the specific volume of the gas in question.
    specificvolume = ((temperature*relativeR)/(144*pressure))
    return(specificvolume)
    
#Written by Stefan Soder, 2018-05-01
def scfdConversion (scfd, pressure, temperature):
    #converts SCFD to gpm
    standardtemp = 519.67
    standardpres = 14.73
    absolutetemp = temperature + 459.67
    absolutepres = pressure + 14.73
    scfm = (scfd/24)/60
    pressure = absolutepres/standardpres
    temperature = standardtemp/absolutetemp
    acfm = scfm /(pressure*temperature)
    gpm = acfm * 7.481
    return(gpm)
