import pyttsx3

# Initialize text-to-speech engine
text_speech = pyttsx3.init()

def recommendations(symptoms_list):
    """
    Takes a list of symptoms and returns a list of corresponding prescriptions.

    Args:
        symptoms_list: A list of strings representing symptoms.

    Returns:
        A list of strings representing prescriptions, or None if no match.
    """

    prescriptions_dict = {
        "fever": "Take paracetamol, drink plenty of fluids, and get some rest.",
        "cough": "Try cough syrup, drink warm water, and avoid cold drinks.",
        "headache": "Take ibuprofen or paracetamol and rest in a quiet place.",
        "stomach pain": "Avoid spicy food, drink warm water, and try antacids.",
        "cold": "Stay hydrated, take vitamin C, and get proper rest.",
        "runny nose": "Use saline nasal spray, drink warm liquids, and rest.",
        "sore throat": "Gargle with warm salt water, drink warm tea with honey, and rest.",
        "muscle aches": "Apply a warm compress, take pain relievers, and rest.",
        "fatigue": "Get plenty of sleep, stay hydrated, and eat nutritious foods.",
        "nausea": "Sip on clear liquids, eat bland foods, and rest."
    }

    recommendations_list = []

    for symptom in symptoms_list:
        symptom_lower = symptom.lower()  # Convert to lowercase for case-insensitive matching
        prescription = prescriptions_dict.get(symptom_lower)
        if prescription:
            recommendations_list.append(prescription)
            print(f"Symptom: {symptom.capitalize()}")
            print(f"Prescription: {prescription}")
            text_speech.say(prescription)
            text_speech.runAndWait()
        else:
            recommendations_list.append(f"No recommendation found for: {symptom}")
            print(f"No recommendation found for: {symptom}")
            text_speech.say(f"No recommendation found for: {symptom}")
            text_speech.runAndWait()

    return recommendations_list

# Example Usage:
symptoms = ["Fever", "Cough", "Headache", "runny nose", "unknown symptom"]
prescriptions = recommendations(symptoms)
print("\nFull prescription list:")
for item in prescriptions:
  print(item)