from .protactive import create_enhanced_yantra





class sinhala:

    def protactive_yantra(filename="yantra_protactive.png"):

        """Create a protactive yantra pattern"""
        create_enhanced_yantra(filename=filename,text= "ඪ") 


class english:

    def protactive_yantra(filename="yantra_protactive.png"):

        """Create a protactive yantra pattern"""
        create_enhanced_yantra(filename=filename, text="dha",sinhala=False)


all = [sinhala,english]



