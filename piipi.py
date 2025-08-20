import streamlit as st

# Titolo della pagina
st.title("❤️🐣Il quiz super importante dei Pipii🐥❤️")


# Titolo e domanda
st.subheader("Domanda 1:")
st.write("Qual è stata la prima parola che hai sentito uscire dalla mia voce?")

# Campo di input Streamlit
risposta1 = st.text_input("Scrivi la tua risposta qui sotto 💬")

# Controllo della risposta
if risposta1:
    if risposta1 == "Massa":
        st.success("✅ Bravissima Pipi, ma come hai fatto a ricordartelo?")
    else:
        st.error("❌ Noooooo Pipi, chiu chiu chiu chiu")


