# 📠 Simulador de la Màquina ENIGMA

Aquest projecte és una implementació en Python de la històrica màquina de xifratge **ENIGMA** (model de 3 rotors), utilitzada per la Wehrmacht durant la Segona Guerra Mundial. El simulador reprodueix el comportament mecànic dels rotors, el "stepping" (moviment de l'odòmetre) i el xifratge reversible.

## 👥 Autors
* **Marc Malo** - (marma990)
* **Martí Querol** - (martiquerol22)

## 🚀 Funcionalitats
El programa compleix amb els requisits de la pràctica:
1.  **Xifratge de missatges:** Converteix text net en text xifrat (agrupat de 5 en 5).
2.  **Desxifratge:** Recupera el missatge original utilitzant la configuració inversa.
3.  **Gestió de Rotors:**
    * Càrrega des de fitxers `.txt`.
    * Validació automàtica (26 lletres úniques).
    * Edició i guardat de noves configuracions de rotors.
4.  **Simulació Mecànica:** Implementació del moviment dels rotors i el sistema de "Notch" (muesca).

## 🛠️ Requisits Tècnics
* **Llenguatge:** Python 3.x
* No es requereixen llibreries externes (només estàndard: `os`, `unicodedata`, `re`).

## 📂 Estructura del Projecte
```text
ENIGMA/
├── data/                  # Fitxers de configuració (Rotor1.txt, etc.) i missatges
├── src/                   # Codi font
│   ├── main.py            # Punt d'entrada (Menú principal)
│   ├── enigma.py          # Lògica de xifratge i moviment de rotors
│   ├── gestor_archivos.py # Lectura i escriptura de fitxers
│   └── utilidades.py      # Neteja i format de text
└── README.md              # Documentació del projecte