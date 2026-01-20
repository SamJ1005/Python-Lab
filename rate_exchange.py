def usd_to_inr(usd):
    return usd * 89.84

def usd_to_eur(usd):
    return usd * 0.86

def inr_to_usd(inr):
    return inr / 89.84

def inr_to_eur(inr):
    return inr * 0.0095

def eur_to_usd(eur):
    return eur * 1.17

def eur_to_inr(eur):
    return eur * 105.01


usd = float(input("Enter amount in USD ($): "))
print(f"{usd} USD($) = {usd_to_inr(usd):.4f} INR(₹)")
print(f"{usd} USD($) = {usd_to_eur(usd):.4f} EUR(€)")

inr = float(input("\nEnter amount in INR (₹): "))
print(f"{inr} INR(₹) = {inr_to_usd(inr):.4f} USD($)")
print(f"{inr} INR(₹) = {inr_to_eur(inr):.4f} EUR(€)")

eur = float(input("\nEnter amount in EUR (€): "))
print(f"{eur} EUR(€) = {eur_to_usd(eur):.4f} USD($)")
print(f"{eur} EUR(€) = {eur_to_inr(eur):.4f} INR(₹)")