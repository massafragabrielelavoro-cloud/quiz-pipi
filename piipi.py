import streamlit as st

# Titolo della pagina
st.title("❤️🐣Il quiz super importante dei Pipii🐥❤️")

# Domanda
st.subheader("Domanda 1:")
st.write("Qual è stata la prima parola che hai sentito uscire dalla mia voce?")


# Risposta personalizzata
risposta1 = input()
if risposta1 == "Massa":
    st.success("✅ Bravissima Pipi, ma come hai fatto a ricordartelo?")
else:
    st.error(f"❌ Noooooo Pipi, chiu chiu chiu chiu")

