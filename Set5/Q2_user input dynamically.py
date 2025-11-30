# Dynamic Propositional Logic System with user input

def implies(p, q):
    return (not p) or q

def iff(p, q):
    return (p and q) or (not p and not q)

# Accept user input for propositions
propositions = {}
for var in ['A', 'B', 'C']:
    val = input(f"Enter truth value for {var} (True/False): ")
    propositions[var] = val.strip().lower() == 'true'

# Evaluate expressions dynamically
def evaluate_expressions(props):
    print("\n--- Propositional Logic Evaluation ---")
    print("A ∧ ¬C =", props['A'] and not props['C'])
    print("(A ∨ B) ∧ C =", (props['A'] or props['B']) and props['C'])
    print("¬B ∨ A =", (not props['B']) or props['A'])
    print("A → C =", implies(props['A'], props['C']))
    print("B ↔ C =", iff(props['B'], props['C']))

# Run evaluation
evaluate_expressions(propositions)
