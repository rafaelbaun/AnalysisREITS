import numpy as np



#import aus csv Datei
adj_closings_sbra = np.loadtxt("SBRA.csv", skiprows=1, usecols=5, delimiter=',')
print(adj_closings_sbra)

adj_closings_eqr = np.loadtxt("EQR.csv",skiprows=1,usecols=5,delimiter=',')
print(adj_closings_eqr)

#Berechnung einfache Rendite
def simple_rate_of_return(adj_closings):
    daily_simple_ror = np.diff(adj_closings)/adj_closings[:-1]
    return daily_simple_ror
#Differenz/Startpreis - letztes Element, da durch Differenz kürzer

daily_simple_returns_sbra = simple_rate_of_return(adj_closings_sbra)
print(daily_simple_returns_sbra)

daily_simple_returns_eqr = simple_rate_of_return(adj_closings_eqr)
print(daily_simple_returns_eqr )

#Durchschnitt der täglichen Rendite
average_daily_simple_return_sbra = np.mean(daily_simple_returns_sbra)
print(average_daily_simple_return_sbra)

average_daily_simple_return_eqr = np.mean(daily_simple_returns_eqr)
print(average_daily_simple_return_eqr)

#Berechnung Loragithmische Rendite
def log_returns(adj_closings):
    log_adj_closings = np.log(adj_closings)
    daily_log_returns = np.diff(log_adj_closings)
    return daily_log_returns

daily_log_returns_sbra = log_returns(adj_closings_sbra)
print(daily_log_returns_sbra)

daily_log_returns_eqr = log_returns(adj_closings_eqr)
print(daily_log_returns_eqr)

#Tägliche Durchschnittsrendite auf jährliche aufrechnen
def annualize_log_return(daily_log_returns):
    average_daily_log_returns = np.mean(daily_log_returns)
    annualized_log_return = average_daily_log_returns * 250
    return annualized_log_return

annualized_log_return_sbra = annualize_log_return(daily_log_returns_sbra)
print(annualized_log_return_sbra)

annualized_log_return_eqr = annualize_log_return(daily_log_returns_eqr)
print(annualized_log_return_eqr)

#Varianz berechnen
daily_varaince_sbra = np.var(daily_log_returns_sbra)
print(daily_varaince_sbra)

daily_variance_eqr = daily_log_returns_eqr.var()
print(daily_variance_eqr)

#Standardabweichung berechnen
daily_sd_sbra = np.std(daily_log_returns_sbra)
print(daily_sd_sbra)

daily_sd_eqr = np.std(daily_log_returns_eqr)
print(daily_sd_eqr)

#Korrelation berechnen
corr_sbra_eqr = np.corrcoef(daily_log_returns_sbra,daily_log_returns_eqr)
print(corr_sbra_eqr)