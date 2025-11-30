# Extended system to return multiple possible diseases


def diagnose_multiple(symptoms):
    print("\n--- Advanced Medical Diagnosis Expert System ---")
    possible_diseases = []

    for rule, disease in rules.items():
        rule_symptoms = rule.split(" and ")
        if all(symptom in symptoms for symptom in rule_symptoms):
            possible_diseases.append(disease)

    return possible_diseases if possible_diseases else ["No matching disease found."]

# Knowledge Base
rules = {
    "fever and cough": "Flu",
    "fever and headache": "Dengue",
    "cough and sore throat": "Common Cold",
    "fever and body pain": "Viral Infection",
    "cough and shortness of breath": "Asthma"
}

# User enters symptoms manually
user_input = input("\nEnter symptoms separated by comma: ").lower().strip()
user_symptoms = [s.strip() for s in user_input.split(",")]

result = diagnose_multiple(user_symptoms)

print("\nPossible Diagnoses:")
for disease in result:
    print("-", disease)
