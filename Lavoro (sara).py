class CampioneDna:
    def __init__(self,codice_campione,sequenza,laboratorio, geni_mappati=None,mutazioni_rilevate=None):
        self.__codice_campione = codice_campione
        self.__sequenza = sequenza.upper()
        self.laboratorio=laboratorio
    
        if geni_mappati is None:
            self.__geni_mappati=[]
        else:
            self.__geni_mappati = geni_mappati
        
        if mutazioni_rilevate is None:
            self.__mutazioni_rilevate = {}
        else:
            self:__mutazioni_rilevate = mutazioni_rilevate
        
#attributi pubblici
    def aggiungi_gene(self, gene):
        if (gene in self.__geni_mappati) == False:
            self.__geni_mappati.append(gene)
    
    def registra_mutazione(self, posizione, tipo_mutazione):
        self.__mutazioni_rilevate[posizione] = tipo_mutazione
    
    
    def calcola_percentuale_gc(self):
        g = self.__sequenza.count("G")
        c = self.__sequenza.count("C")
        totale = len(self.__sequenza)
        if totale == 0:
            return 0.0
        return ((g + c) / totale)* 100


    def stampa_report(self):
        seq_breve =""
        contatore=0
        for lettera in self.__sequenza:
            if contatore < 20:
                seq_breve =seq_breve + lettera
                contatore = contatore + 1
        if len(self.__sequenza) > 20:
           seq_breve = seq_breve + "la sequenza si è abbreviata"
                
            
        
        print("Codice:" , self.__codice_campione)
        print("Laboratorio:", self.laboratorio)
        print("sequenza:" ,seq_breve)
        print("Geni_mappati:", self.__geni_mappati)
        print("Percentuale Guanina e Citoplasma:", self.calcola_percentuale_gc(),"%")
        print("Mutazioni:", self.__mutazioni_rilevate)
        
        
campione=CampioneDna("DNA-4029","atcggctagctagc","Labgen-BioApp",["geneA"])
campione.aggiungi_gene("ampR")
campione.registra_mutazione(5,"sostituzione")
campione.stampa_report()
        
        
    
                
            
    
    
    
    
        
        
            
                
                
                
            
                
        
        