import streamlit as st

# Titre de l'application
st.title("📝 Mon Bloc-Notes")

# Initialisation de la session state pour stocker les notes
if "notes" not in st.session_state:
    st.session_state.notes = []

# Zone de saisie de texte
note = st.text_area("✍️ Écris ta note ici")

# Bouton pour sauvegarder la note
if st.button("📌 Ajouter la note"):
    if note != "":
        st.session_state.notes.append(note)
        st.success("✅ Note ajoutée avec succès !")
    else:
        st.warning("⚠️ Le champ est vide.")

# Affichage des notes
st.subheader("📖 Mes Notes")
for i, n in enumerate(st.session_state.notes):
    st.write(f"{i+1}. {n}")

# Bouton pour effacer toutes les notes
if st.button("🗑️ Effacer toutes les notes"):
    st.session_state.notes = []
    st.success("🗑️ Toutes les notes ont été supprimées.")
