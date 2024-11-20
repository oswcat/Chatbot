from flask import Flask, request, jsonify
import spacy
import json

app = Flask(__name__)

# Cargar modelo SpaCy
nlp = spacy.load("es_core_news_sm")

# Cargar intenciones
with open("Json/intenciones.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

# Función para encontrar la intención más cercana
def encontrar_intencion(mensaje):
    doc = nlp(mensaje.lower())
    mayor_similitud = 0
    intencion_encontrada = None

    for intencion in intents:
        for patron in intencion["patterns"]:
            doc_patron = nlp(patron.lower())
            similitud = doc.similarity(doc_patron)
            if similitud > mayor_similitud:
                mayor_similitud = similitud
                intencion_encontrada = intencion

    return intencion_encontrada if mayor_similitud > 0.7 else None

# Contador de fallos para escalar a asesor
fallos_continuos = 0

@app.route("/chat", methods=["POST"])
def chat():
    global fallos_continuos

    mensaje_usuario = request.json.get("mensaje", "").strip()
    if not mensaje_usuario:
        return jsonify({"respuesta": "Por favor, escribe algo."})

    # Encontrar intención
    intencion = encontrar_intencion(mensaje_usuario)

    if intencion:
        fallos_continuos = 0  # Reiniciar contador de fallos
        respuesta = intencion["responses"][0]
    else:
        fallos_continuos += 1
        if fallos_continuos >= 2:
            return jsonify({"respuesta": "No entiendo tu pregunta. Te conecto con un asesor humano."})
        else:
            respuesta = (
                "No estoy seguro de lo que necesitas. Aquí tienes un menú de opciones:\n"
                "1. Información sobre licenciaturas\n"
                "2. Información sobre maestrías\n"
                "3. Hablar con un asesor\n"
                "4. Ver nuestra ubicación"
            )

    return jsonify({"respuesta": respuesta})


if __name__ == "__main__":
    app.run(debug=True)
