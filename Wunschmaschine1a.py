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
        self.reflexionsfrage = ""
        self.schwingungsanpassung = ""

    def ziel_eingeben(self):
        self.ziel = st.text_input("Was möchtest du manifestieren?")
    
    def essenz_pruefung(self):
        antwort = st.radio("Essenz-Ebene: Ist das Ziel wirklich dein tiefstes Seelenziel?", ("Ja", "Nein"))
        if antwort == "Ja":
            self.essenz_check = "✅ Dein Ziel entspricht deinem wahren Seelenwunsch."
        else:
            self.essenz_check = "⚠️ Dein Wunsch könnte aus Ego oder Mangeldenken stammen. Überdenke ihn."
            self.blockaden += "\n- Überlege, ob dein Wunsch aus deiner höchsten Frequenz oder aus Angst stammt."
    
    def kausal_pruefung(self):
        antwort = st.radio("Kausale Ebene: Glaubst du, dass du es leicht erreichen kannst?", ("Ja", "Nein"))
        if antwort == "Ja":
            self.kausal_check = "✅ Deine innere Überzeugung unterstützt dein Ziel."
        else:
            self.kausal_check = "⚠️ Du hast blockierende Glaubenssätze. Arbeite an deiner inneren Einstellung."
            self.blockaden += "\n- Erkenne, welche alten Überzeugungen dich limitieren."
    
    def energie_pruefung(self):
        antwort = st.radio("Energie-Ebene: Fühlst du dich bereits so, als hättest du dein Ziel erreicht?", ("Ja", "Nein"))
        if antwort == "Ja":
            self.energie_check = "✅ Deine energetische Ausstrahlung stimmt mit deinem Ziel überein."
        else:
            self.energie_check = "⚠️ Deine Schwingung ist noch nicht auf der Frequenz des Ziels."
            self.blockaden += "\n- Lebe in der Frequenz der erfüllten Realität. Dein Zustand erschafft Materie."
    
    def physisch_pruefung(self):
        antwort = st.radio("Physische Ebene: Hast du bereits eine Handlung ausgeführt?", ("Ja", "Nein"))
        if antwort == "Ja":
            self.physisch_check = "✅ Du handelst im Einklang mit deiner Manifestation."
        else:
            self.physisch_check = "⚠️ Manifestation benötigt physische Handlungen. Setze einen ersten konkreten Schritt!"
            self.blockaden += "\n- Entwickle eine klare Strategie, um erste Schritte zu gehen."
    
    def hoeheres_selbst_pruefung(self):
        antwort = st.radio("Bist du bereit, deinem höheren Selbst zu vertrauen?", ("Ja", "Nein"))
        if antwort == "Ja":
            self.hoeheres_selbst = "✅ Du bist in völliger Harmonie mit deiner höchsten Führung."
        else:
            self.hoeheres_selbst = "⚠️ Lasse Kontrolle los und vertraue dem Fluss des Universums."
            self.blockaden += "\n- Übe Vertrauen und Hingabe in den natürlichen Manifestationsprozess."
    
    def schwingungsanpassung_modul(self):
        if "⚠️" in (self.essenz_check + self.kausal_check + self.energie_check + self.physisch_check + self.hoeheres_selbst):
            antwort = st.radio("Möchtest du eine Frequenzanpassung für diesen Wunsch?", ("Ja", "Nein"))
            if antwort == "Ja":
                self.schwingungsanpassung = "✨ Schließe die Augen und visualisiere, dass dein Wunsch bereits Realität ist. Welche Emotionen kommen hoch? ✨"
                st.info(self.schwingungsanpassung)
    
    def selbstreflexion(self):
        self.reflexionsfrage = st.text_area("Gibt es eine innere Überzeugung, die diesem Wunsch widerspricht? Falls ja, welche?")
    
    def manifestieren(self):
        st.title("✨ Wunschmaschine ✨")
        self.ziel_eingeben()
        if self.ziel:
            self.essenz_pruefung()
            self.kausal_pruefung()
            self.energie_pruefung()
            self.physisch_pruefung()
            self.hoeheres_selbst_pruefung()
            self.schwingungsanpassung_modul()
            self.selbstreflexion()

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
                st.warning(self.blockaden)
            
            st.success(self.ergebnis)

if __name__ == "__main__":
    tool = Wunschmaschine()
    tool.manifestieren()

