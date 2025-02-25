import streamlit as st

class Wunschmaschine:
    def __init__(self):
        self.ziel = ""
        self.essenz_check = ""
        self.kausal_check = ""
        self.energie_check = ""
        self.physisch_check = ""
        self.hoeheres_selbst = ""
        self.ergebnis = ""

    def ziel_eingeben(self):
        self.ziel = st.text_input("Was möchtest du manifestieren?")
    
    def essenz_pruefung(self):
        antwort = st.radio("Essenz-Ebene: Entspricht dein Wunsch wirklich deinem höchsten Selbst?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.essenz_check = "✅ Dein Wunsch ist in Einklang mit deiner Essenz."
        elif antwort == "Nein":
            self.essenz_check = "⚠️ Dein Wunsch könnte aus Ego oder Mangeldenken stammen."
        else:
            self.essenz_check = "🔍 Reflexionsfragen: Ist dieser Wunsch aus Freude geboren oder aus Angst? Wenn du wüsstest, dass dein höchstes Selbst ihn bereits lebt – würdest du ihn anders formulieren?"
    
    def kausal_pruefung(self):
        antwort = st.radio("Kausale Ebene: Glaubst du zu 100%, dass dein Wunsch möglich ist?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.kausal_check = "✅ Deine innere Überzeugung unterstützt dein Ziel."
        elif antwort == "Nein":
            self.kausal_check = "⚠️ Du hast blockierende Glaubenssätze."
        else:
            self.kausal_check = "🔍 Reflexionsfragen: Woher weiß ich, dass es nicht möglich ist? Habe ich Beweise, dass es für andere funktioniert hat?"
    
    def energie_pruefung(self):
        antwort = st.radio("Energie-Ebene: Fühlst du dich bereits so, als wäre dein Wunsch erfüllt?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.energie_check = "✅ Deine Schwingung ist im Einklang mit deinem Ziel."
        elif antwort == "Nein":
            self.energie_check = "⚠️ Deine Schwingung ist noch nicht auf der Frequenz des Ziels."
        else:
            self.energie_check = "🔍 Reflexionsfragen: Fühle ich Frieden oder Anspannung, wenn ich an meinen Wunsch denke? Was hindert mich daran, jetzt schon in diesem Gefühl zu sein?"
    
    def physisch_pruefung(self):
        antwort = st.radio("Physische Ebene: Hast du bereits konkrete Handlungen unternommen?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.physisch_check = "✅ Du handelst im Einklang mit deiner Manifestation."
        elif antwort == "Nein":
            self.physisch_check = "⚠️ Manifestation erfordert physische Handlungen."
        else:
            self.physisch_check = "🔍 Reflexionsfragen: Habe ich eine kleine Aktion gesetzt – oder warte ich auf das 'perfekte' Zeichen? Gibt es einen nächsten Schritt, den ich sofort tun könnte?"
    
    def hoeheres_selbst_pruefung(self):
        antwort = st.radio("Höheres Selbst: Vertraust du dem Universum und deiner Führung?", ("Ja", "Nein", "Ich weiß es nicht"))
        if antwort == "Ja":
            self.hoeheres_selbst = "✅ Du bist in völliger Harmonie mit deiner höchsten Führung."
        elif antwort == "Nein":
            self.hoeheres_selbst = "⚠️ Du kämpfst gegen den Fluss des Universums."
        else:
            self.hoeheres_selbst = "🔍 Reflexionsfragen: Kann ich loslassen und wissen, dass sich alles fügt? Spüre ich eine innere Gelassenheit oder versuche ich zu kontrollieren?"
    
    def manifestieren(self):
        st.title("✨ Wunschmaschine ✨")
        self.ziel_eingeben()
        if self.ziel:
            self.essenz_pruefung()
            self.kausal_pruefung()
            self.energie_pruefung()
            self.physisch_pruefung()
            self.hoeheres_selbst_pruefung()

            st.subheader("--- WUNSCHMASCHINEN-ANALYSE ---")
            st.write(f"🎯 Ziel: {self.ziel}")
            st.write(self.essenz_check)
            st.write(self.kausal_check)
            st.write(self.energie_check)
            st.write(self.physisch_check)
            st.write(self.hoeheres_selbst)
            
            if "⚠️" not in (self.essenz_check + self.kausal_check + self.energie_check + self.physisch_check + self.hoeheres_selbst):
                self.ergebnis = "🌟 Dein Ziel ist im vollständigen Alignment! Es wird sich schnell materialisieren. 🌟"
            else:
                self.ergebnis = "🔍 Es gibt Blockaden. Arbeite an den Bereichen mit ⚠️ für eine schnellere Manifestation."
                
            st.success(self.ergebnis)

if __name__ == "__main__":
    tool = Wunschmaschine()
    tool.manifestieren()

