# Simple Rule-Based Expert System for Medical Diagnosis

def diagnose(symptoms):
    print("\n--- Medical Diagnosis Expert System ---")
    for rule, disease in rules.items():
        rule_symptoms = rule.split(" and ")
        if all(symptom in symptoms for symptom in rule_symptoms):
            return disease
    return "No exact match found."

# Knowledge Base: Rules mapping symptoms to diseases
rules = {
    "fever and cough": "Flu",
    "fever and headache": "Dengue",
    "cough and sore throat": "Common Cold",
    "chest pain and shortness of breath": "Asthma"
}

# Sample user symptoms
user_symptoms = ["fever", "cough"]

result = diagnose(user_symptoms)
print("Diagnosis:", result)


