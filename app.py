import time
import streamlit as st


LANG_OPTIONS = {
    "Deutsch": "de",
    "Español": "es",
    "English": "en",
}


def get_texts(lang: str) -> dict:
    return {
        "title": {
            "de": "🧘 Anfängerfreundlicher Yoga-Timer",
            "es": "🧘 Temporizador de yoga para principiantes",
            "en": "🧘 Beginner-Friendly Yoga Timer",
        }[lang],
        "intro": {
            "de": "Wähle eine Übung aus, passe die Zeit an und starte den Timer, um sicher zu üben.",
            "es": "Elige una postura, ajusta el tiempo y comienza el temporizador para practicar con seguridad.",
            "en": "Pick a pose, adjust the time, and start the timer to practice safely.",
        }[lang],
        "recommended": {
            "de": "Empfohlene Dauer: {minutes} Minuten",
            "es": "Duración recomendada: {minutes} minutos",
            "en": "Recommended duration: {minutes} minutes",
        }[lang],
        "adjust_label": {
            "de": "Dauer wählen (Minuten)",
            "es": "Elegir duración (minutos)",
            "en": "Choose duration (minutes)",
        }[lang],
        "start_timer": {
            "de": "Timer starten",
            "es": "Iniciar temporizador",
            "en": "Start timer",
        }[lang],
        "time_left": {
            "de": "Verbleibend: {minutes:02d}:{seconds:02d} Minuten",
            "es": "Restante: {minutes:02d}:{seconds:02d} minutos",
            "en": "Remaining: {minutes:02d}:{seconds:02d} minutes",
        }[lang],
        "time_up": {
            "de": "Zeit ist um! Gut gemacht.",
            "es": "¡Tiempo! Bien hecho.",
            "en": "Time is up! Great job.",
        }[lang],
        "duration_helper": {
            "de": "Ziehe den Regler, um zwischen 1 und 10 Minuten zu wählen.",
            "es": "Ajusta el control para elegir entre 1 y 10 minutos.",
            "en": "Use the slider to choose between 1 and 10 minutes.",
        }[lang],
    }


def get_exercises():
    return [
        {
            "id": "mountain_pose",
            "name": {"de": "Berghaltung", "es": "Postura de la montaña", "en": "Mountain Pose"},
            "description": {
                "de": "Stehe aufrecht mit langen Wirbelsäule und ruhiger Atmung, um dich zu zentrieren.",
                "es": "Párate erguido con la columna larga y respiración tranquila para centrarte.",
                "en": "Stand tall with a long spine and calm breath to center yourself.",
            },
            "duration_minutes": 2,
        },
        {
            "id": "child_pose",
            "name": {"de": "Kindhaltung", "es": "Postura del niño", "en": "Child's Pose"},
            "description": {
                "de": "Knie dich hin, setz dich auf die Fersen und lass den Oberkörper nach vorn sinken.",
                "es": "Arrodíllate, siéntate sobre los talones y deja que el torso se relaje hacia adelante.",
                "en": "Kneel, sit back to your heels, and let your torso relax forward.",
            },
            "duration_minutes": 3,
        },
        {
            "id": "cat_cow",
            "name": {"de": "Katze-Kuh", "es": "Gato-Vaca", "en": "Cat-Cow"},
            "description": {
                "de": "Wechsle zwischen rundem und hohlem Rücken, um die Wirbelsäule zu mobilisieren.",
                "es": "Alterna entre espalda redondeada y arqueada para movilizar la columna.",
                "en": "Alternate between rounding and arching the back to mobilize the spine.",
            },
            "duration_minutes": 2,
        },
        {
            "id": "downward_dog",
            "name": {
                "de": "Herabschauender Hund",
                "es": "Perro boca abajo",
                "en": "Downward-Facing Dog",
            },
            "description": {
                "de": "Hebe die Hüften hoch, strecke Arme und Beine und atme gleichmäßig.",
                "es": "Eleva las caderas, estira brazos y piernas y respira de manera uniforme.",
                "en": "Lift hips high, lengthen arms and legs, and breathe steadily.",
            },
            "duration_minutes": 3,
        },
        {
            "id": "cobra_pose",
            "name": {"de": "Kobra", "es": "Cobra", "en": "Cobra Pose"},
            "description": {
                "de": "Rolle die Schultern zurück und hebe die Brust sanft aus der Bauchlage.",
                "es": "Con los hombros atrás, eleva suavemente el pecho desde el suelo.",
                "en": "Roll shoulders back and gently lift the chest from the mat.",
            },
            "duration_minutes": 2,
        },
        {
            "id": "bridge_pose",
            "name": {"de": "Schulterbrücke", "es": "Puente de hombros", "en": "Bridge Pose"},
            "description": {
                "de": "Hebe die Hüften an, drücke die Füße in den Boden und halte den Nacken lang.",
                "es": "Eleva las caderas, presiona los pies y mantén el cuello largo.",
                "en": "Lift the hips, press the feet, and keep the neck long.",
            },
            "duration_minutes": 3,
        },
        {
            "id": "seated_forward_bend",
            "name": {"de": "Sitzende Vorbeuge", "es": "Flexión hacia adelante sentada", "en": "Seated Forward Bend"},
            "description": {
                "de": "Sitze aufrecht und beuge dich aus der Hüfte nach vorn, ohne zu ziehen.",
                "es": "Siéntate erguido y pliégate desde las caderas hacia adelante sin forzar.",
                "en": "Sit tall and hinge forward from the hips without pulling.",
            },
            "duration_minutes": 3,
        },
        {
            "id": "easy_pose",
            "name": {"de": "Einfache Sitzhaltung", "es": "Postura fácil", "en": "Easy Pose"},
            "description": {
                "de": "Setze dich bequem mit gekreuzten Beinen und fokussiere deine Atmung.",
                "es": "Siéntate cómodo con las piernas cruzadas y enfoca la respiración.",
                "en": "Sit comfortably cross-legged and focus on your breath.",
            },
            "duration_minutes": 4,
        },
        {
            "id": "supine_twist",
            "name": {"de": "Liegender Twist", "es": "Torsión supina", "en": "Supine Twist"},
            "description": {
                "de": "Lege dich auf den Rücken und senke beide Knie sanft zur Seite, wechsel dann.",
                "es": "Acuéstate boca arriba y deja caer las rodillas a un lado; luego cambia.",
                "en": "Lie on your back and let both knees fall gently to one side, then switch.",
            },
            "duration_minutes": 3,
        },
        {
            "id": "savasana",
            "name": {"de": "Totenstellung", "es": "Savasana", "en": "Corpse Pose"},
            "description": {
                "de": "Lege dich ruhig hin, entspanne den ganzen Körper und beobachte die Atmung.",
                "es": "Recuéstate en quietud, relaja todo el cuerpo y observa la respiración.",
                "en": "Lie down in stillness, relax the whole body, and watch the breath.",
            },
            "duration_minutes": 5,
        },
    ]


def init_session_state():
    if "timers" not in st.session_state:
        st.session_state["timers"] = {}


def run_timer(exercise_id: str, total_seconds: int, texts: dict, placeholder: st.delta_generator.DeltaGenerator):
    for sec in range(total_seconds, -1, -1):
        minutes, seconds = divmod(sec, 60)
        message = texts["time_left"].format(minutes=minutes, seconds=seconds)
        placeholder.info(message)
        st.session_state["timers"][exercise_id]["last_status"] = message
        time.sleep(1)
    placeholder.success(texts["time_up"])
    st.session_state["timers"][exercise_id]["last_status"] = texts["time_up"]


def render_exercise_card(exercise: dict, lang: str, texts: dict):
    with st.container():
        st.markdown("---")
        st.subheader(exercise["name"][lang])
        st.markdown(exercise["description"][lang])
        st.caption(texts["recommended"].format(minutes=exercise["duration_minutes"]))
        st.caption(texts["duration_helper"])

        duration = st.slider(
            texts["adjust_label"],
            min_value=1,
            max_value=10,
            value=exercise["duration_minutes"],
            key=f"duration_{exercise['id']}",
        )

        start = st.button(texts["start_timer"], key=f"start_{exercise['id']}")
        placeholder = st.empty()

        timer_state = st.session_state["timers"].get(exercise["id"], {})

        if start:
            total_seconds = int(duration * 60)
            st.session_state["timers"][exercise["id"]] = {
                "start_time": time.time(),
                "duration": total_seconds,
                "last_status": texts["time_left"].format(minutes=total_seconds // 60, seconds=total_seconds % 60),
            }
            run_timer(exercise["id"], total_seconds, texts, placeholder)
        elif timer_state.get("last_status"):
            if timer_state["last_status"] == texts["time_up"]:
                placeholder.success(timer_state["last_status"])
            else:
                placeholder.info(timer_state["last_status"])


def main():
    st.set_page_config(page_title="Yoga Timer", page_icon="🧘", layout="wide")
    init_session_state()

    language_label = st.sidebar.selectbox("Language / Sprache / Idioma", list(LANG_OPTIONS.keys()))
    lang = LANG_OPTIONS[language_label]
    texts = get_texts(lang)

    st.title(texts["title"])
    st.markdown(texts["intro"])

    exercises = get_exercises()
    for exercise in exercises:
        render_exercise_card(exercise, lang, texts)


if __name__ == "__main__":
    main()

# Installation: pip install streamlit
# Run locally: streamlit run app.py
# Deploy: Push this file to GitHub and create a new app on Streamlit Cloud linking to the repository.
