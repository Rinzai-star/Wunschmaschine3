import streamlit as st

class Wunschmaschine:
    def __init__(self):
        self.ziel = ""
        self.essenz_check = ""
        self.kausal_check = ""
        self.energie_check = ""
        self.physisch_check = ""
        self.hoeheres_selbst = ""
        self.blockaden = ""
        self.ergebnis = ""

    def ziel_eingeben(self):
        self.ziel = st.text_input("🎯 Was möchtest du manifestieren?")
    
    def essenz_pruefung(self):
        antwort = st.radio("🌟 Essenz-Ebene: Entspricht dein Wunsch wirklich deinem höchsten Selbst?", ["Ja", "Nein"])
        if antwort == "Ja":
            self.essenz_check = "✅ Dein Ziel entspricht deiner tiefsten Wahrheit."
        else:
            self.essenz_check = "⚠️ Dein Wunsch könnte aus Ego oder Mangeldenken stammen. Überdenke ihn."
            self.blockaden += "\n- Überlege, ob dein Wunsch aus deiner höchsten Frequenz oder aus Angst stammt."
    
    def kausal_pruefung(self):
        antwort = st.radio("🧠 Kausale Ebene: Glaubst du zu 100%, dass dein Wunsch möglich ist?", ["Ja", "Nein"])
        if antwort == "Ja":
            self.kausal_check = "✅ Deine innere Überzeugung unterstützt dein Ziel."
        else:
            self.kausal_check = "⚠️ Deine Glaubenssätze blockieren dich noch. Ändere sie bewusst."
            self.blockaden += "\n- Ersetze negative Überzeugungen durch klare Dekrete: ‚Es ist so.‘"
    
    def energie_pruefung(self):
        antwort = st.radio("💫 Energie-Ebene: Fühlst du dich bereits so, als wäre dein Wunsch erfüllt?", ["Ja", "Nein"])
        if antwort == "Ja":
            self.energie_check = "✅ Deine Schwingung ist in Alignment mit deinem Wunsch."
        else:
            self.energie_check = "⚠️ Deine Schwingung ist noch nicht auf der Frequenz des Ziels."
            self.blockaden += "\n- Lebe in der Frequenz der erfüllten Realität. Dein Zustand erschafft Materie."
    
    def physisch_pruefung(self):
        antwort = st.radio("🔨 Physische Ebene: Hast du bereits konkrete Handlungen unternommen?", ["Ja", "Nein"])
        if antwort == "Ja":
            self.physisch_check = "✅ Du handelst im Einklang mit deiner Manifestation."
        else:
            self.physisch_check = "⚠️ Manifestation erfordert physische Schritte. Setze sofort eine Handlung um!"
            self.blockaden += "\n- Handle aus Vertrauen, nicht aus Angst. Dein Wunsch existiert bereits."

    def hoeheres_selbst_pruefung(self):
        antwort = st.radio("👁️ Höheres Selbst: Vertraust du dem Universum und deiner Führung?", ["Ja", "Nein"])
        if antwort == "Ja":
            self.hoeheres_selbst = "✅ Du bist in völliger Harmonie mit deiner höchsten Führung."
        else:
            self.hoeheres_selbst = "⚠️ Du kämpfst noch gegen deine eigene Führung an."
            self.blockaden += "\n- Vertraue. Lass Kontrolle los. Sei in Alignment mit deinem höchsten Selbst."

    def manifestieren(self):
        st.title("✨ **Dekret-Maschine** ✨")
        self.ziel_eingeben()
        if self.ziel:
            self.essenz_pruefung()
            self.kausal_pruefung()
            self.energie_pruefung()
            self.physisch_pruefung()
            self.hoeheres_selbst_pruefung()

            st.subheader("--- **MANIFESTATIONS-ANALYSE** ---")
            st.write(f"🎯 **Ziel:** {self.ziel}")
            st.write(self.essenz_check)
            st.write(self.kausal_check)
            st.write(self.energie_check)
            st.write(self.physisch_check)
            st.write(self.hoeheres_selbst)
            
            if "⚠️" not in (self.essenz_check + self.kausal_check + self.energie_check + self.physisch_check + self.hoeheres_selbst):
                self.ergebnis = "🌟 Dein Ziel ist vollkommen ausgerichtet. Es manifestiert sich jetzt! 🌟"
            else:
                self.ergebnis = "🔍 Es gibt Blockaden. Arbeite an den Bereichen mit ⚠️ für eine schnellere Manifestation."
                st.warning(self.blockaden)
            
            st.success(self.ergebnis)

if __name__ == "__main__":
    tool = Wunschmaschine()
    tool.manifestieren()
