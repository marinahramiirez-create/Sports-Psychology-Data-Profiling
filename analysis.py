# Script para identificar áreas de prioridad basadas en los resultados del IPED

scores = {
    "Motivation": 27,
    "Self-Confidence": 24,
    "Attitudinal Control": 24,
    "Visuomotor Control": 24,
    "Attentional Control": 20,
    "Positive Coping": 20,
    "Negative Coping": 16
}

def analyze_performance(data):
    print("--- PSYCHOLOGICAL DATA ANALYSIS ---")
    for variable, score in data.items():
        # Los baremos del IPED sugieren que menos de 20 requiere atención inmediata
        status = "OPTIMAL" if score >= 24 else "STABLE"
        if score < 20: status = "PRIORITY INTERVENTION"
        
        print(f"{variable}: {score} -> Status: {status}")

if __name__ == "__main__":
    analyze_performance(scores)
