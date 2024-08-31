import joblib
import os

# Încărcarea modelului salvat din directorul specificat
model_path = os.path.join('results', 'model_optimization_results', 'Optimized_RandomForest_Model.joblib')
best_rf = joblib.load(model_path)

# Definirea unei noi compoziții ca dicționar
tested_composition = {
    "BaO": 0,
    "CaO": 0,
    "MgO": 0,
    "PbO": 0,
    "SrO": 0,
    "ZnO": 67.7,
    "GeO2": 0,
    "SiO2": 20.15,
    "TeO2": 0,
    "TiO2": 0,
    "ZrO2": 0,
    "WO3": 0,
    "K2O": 0,
    "Li2O": 0,
    "Na2O": 0,
    "Al2O3": 0,
    "B2O3": 12.4,
    "Bi2O3": 0,
    "P2O5": 0
}

# Verificarea dacă suma compozițiilor este egală cu 100%
total_composition = sum(tested_composition.values())

if total_composition != 100:
    raise ValueError(f"Suma compozițiilor trebuie să fie egală cu 100%. Suma actuală este {total_composition:.2f}%")
    
# Pregătirea compoziției pentru predicție - doar valorile
composition_values = list(tested_composition.values())

# Predicția Tg pentru noua compoziție
predicted_tg = best_rf.predict([composition_values])

# Filtrarea și formatarea componentelor care nu sunt 0
composition_str = ", ".join([
    f"{component}: {amount}%" 
    for component, amount in tested_composition.items() 
    if amount != 0
])

# Afișarea compoziției care nu conține 0 și a Tg prezis
print(f"Compoziție: {composition_str}")
print(f"Predicted Tg: {predicted_tg[0]:.2f}")
