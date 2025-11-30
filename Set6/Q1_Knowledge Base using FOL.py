# Install kanren if not already installed
# pip install kanren

from kanren import Relation, facts

# Define a relation: doctor_treats(Doctor, Disease)
doctor_treats = Relation()

# Add facts to the knowledge base
facts(doctor_treats,
      ("Dr_Smith", "Flu"),
      ("Dr_Adams", "Covid"),
      ("Dr_Jones", "Flu"),
      ("Dr_Brown", "Diabetes"),
      ("Dr_White", "Covid"))
