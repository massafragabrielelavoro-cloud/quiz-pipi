import streamlit as st

# Titolo
st.title("❤️🐣Il quiz super importante dei Pipii🐥❤️")

# Inizializza lo stato
if "step" not in st.session_state:
    st.session_state.step = 1

# Funzione per passare alla domanda successiva
def next_step():
    st.session_state.step += 1

# Domanda 1
if st.session_state.step == 1:
    st.subheader("Domanda 1:")
    st.write("Qual è stata la prima parola che hai sentito uscire dalla mia voce?")
    risposta1 = st.text_input("Scrivi la tua risposta qui sotto 💬", key="domanda1")
    if risposta1:
        if risposta1.strip().lower() == "massa":
            st.success("✅ Bravissima Pipi, ma come hai fatto a ricordartelo?")
        else:
            st.error("❌ Noooooo Pipi, chiu chiu chiu chiu")
        st.button("Avanti ➡️", on_click=next_step)

# Domanda 2
elif st.session_state.step == 2:
    st.subheader("Domanda 2:")
    st.write("Come si chiamava il mio bisnonno materno")
    risposta2 = st.text_input("Scrivi la tua risposta qui sotto 💬", key="domanda2")
    if risposta2:
        if risposta2.strip().lower() == "gennaro":
            st.success("✅ Daleeee Pipiiii wuuuuuuu")
        else:
            st.error("❌ Ma no pipi, era Gennaro, che praticamente è uguale a dire Ciro. Chiuuuuu!!!")
        st.button("Avanti ➡️", on_click=next_step)

# Domanda 3
elif st.session_state.step == 3:
    st.subheader("Domanda 3:")
    st.write("Ma se io sono pipi pulcino, tu sei pipi come?")
    risposta3 = st.text_input("Scrivi la tua risposta qui sotto 💬", key="domanda3")
    if risposta3:
        if risposta3.strip().lower() == "pulcina":
            st.success("✅ Beh si, questa era facile ma a volte ho il dubbio")
        else:
            st.error("❌ Ma Pipi, queste sono le base della pulcinologia")
        st.button("Avanti ➡️", on_click=next_step)

# Domanda 4
elif st.session_state.step == 4:
    st.subheader("Domanda 4:")
    st.write("Chi dovrebbe essere il prossimo Presidente del Consiglio italiano")
    risposta4 = st.text_input("Scrivi la tua risposta qui sotto 💬", key="domanda4")
    if risposta4:
        if risposta4.strip().lower() == "boldrin":
            st.success("✅ Ottimo, ottimo Pipi, ti meriti un bacino dei pipi anche sui piedini e sulla concha di pipi pulcina")
        else:
            st.error("❌ Ma orco Dio Pipi, questa era importante")
        st.button("Avanti ➡️", on_click=next_step)

# Domanda 5
elif st.session_state.step == 5:
    st.subheader("Domanda 5:")
    st.write("Cosa accomuna il nostro gattino e il professore di economia politica di Perón in Italia?")
    risposta5 = st.text_input("Scrivi la tua risposta qui sotto 💬", key="domanda5")
    if risposta5:
        if risposta5.strip().lower() == "einaudi":
            st.success("✅ Wuuuuuuuu, tanto amore per il nostro Eini e le sue sorrelline gattine")
        else:
            st.error("❌ Mamamamamamamama Pipi, il nostro gattino Einaudi")
        st.button("Avanti ➡️", on_click=next_step)

# Domanda 6
elif st.session_state.step == 6:
    st.subheader("Domanda 6:")
    st.write("Come si chiamava la maga che secondo la leggenda diede il nome alla città di Mantova")
    risposta6 = st.text_input("Scrivi la tua risposta qui sotto 💬", key="domanda6")
    if risposta6:
        if risposta6.strip().lower() == "manto":
            st.success("✅ Pipi, mi hai stupito, davvero non credevo che te lo ricordassi. Ti amo")
        else:
            st.error("❌ E vabbè Pipi, questa non è tanto grave non saperla")
        st.button("Avanti ➡️", on_click=next_step)

# Domanda 7
elif st.session_state.step == 7:
    st.subheader("Domanda 7:")
    st.write("Siamo la [...] più bella del mondo")
    risposta7 = st.text_input("Scrivi la tua risposta qui sotto 💬", key="domanda7")
    if risposta7:
        if risposta7.strip().lower() == "coppia":
            st.success("✅ E ci dispiace per gli altri")
        else:
            st.error("❌ Maaaa oh pipi, questa pensavo che non ci dovessi nemmeno riflettere")
        st.button("Avanti ➡️", on_click=next_step)

# Domanda 8
elif st.session_state.step == 8:
    st.subheader("Domanda 8:")
    st.write("Se il prezzo per un abbraccio è di 10 bacini e aumenta del 2% ogni mese per 12 mesi; qual sarà il prezzo di un abbraccio dopo un anno? (fermati al secondo decimale)")
    risposta8 = st.text_input("Scrivi la tua risposta qui sotto 💬", key="domanda8")
    if risposta8:
        if risposta8.strip() == "12,68":
            st.success("✅ Madonna Pipi, ti ricordi anche la matematica che ti ho insegnato, sono troppo orgoglioso di te")
        else:
            st.error("❌ Maaaaa Pipi, dopo te lo spiego")
        st.button("Avanti ➡️", on_click=next_step)

# Domanda 9
elif st.session_state.step == 9:
    st.subheader("Domanda 9:")
    st.write("Quanti esami mi mancano per laurearmi?")
    risposta9 = st.text_input("Scrivi la tua risposta qui sotto 💬", key="domanda9")
    if risposta9:
        if risposta9.strip() == "7":
            st.success("✅ Esatto Pipi, non so se era difficile ma comunque brava")
        else:
            st.error("❌ Ma chiu Pipi, questo te l'avrò detto un milione di volte")
        st.button("Avanti ➡️", on_click=next_step)

# Domanda 10
elif st.session_state.step == 10:
    st.subheader("Domanda 10:")
    st.write("Qual è il nome sui documenti umani della Pipi più bella di tutto l'Universo e che voglio sposare il prima possibile?")
    risposta10 = st.text_input("Scrivi la tua risposta qui sotto 💬", key="domanda10")
    if risposta10:
        if risposta10.strip().lower() == "guadalupe":
            st.success("✅ Ma allora Pipi se lo sai, perché non ci sposiamo????!!!!!!")
        else:
            st.error("❌ Ma sei tu Pipi, sei tuuuuuuuuuu")
        st.button("Finito 💖", on_click=next_step)

# Messaggio finale
elif st.session_state.step > 10:
    st.header("🎉 Fine del quiz 🎉")
    st.markdown("Hai completato il quiz dei Pipii! Sei la **Pulcina più intelligente e adorabile dell’universo** 💘")
    st.balloons()
