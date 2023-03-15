from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget
import requests


Window.clearcolor = (174/255.0, 174/255.0, 174/255.0,1)




class LastWindow(Widget):
    
    def take(self,):
        url = "http://www.koeri.boun.edu.tr/scripts/lst8.asp"
        response = requests.get(url)
        response = response.text


        liste = list(response.split("</pre>"))

        liste2 = liste[0].split("<pre>")

        liste3 = liste2[1].split("---------- --------  --------  -------   ----------    ------------    --------------                                  --------------")

        liste4 = liste3[1].split("Ýlksel")

        liste_ayrık = []

        for i in liste4:
            liste_hold = []
            hold = i.split(" ")
            for i in hold:
                if len(i) > 2:
                    liste_hold.append(i)
            liste_ayrık.append(liste_hold)
            #print(liste_hold)
        
        #print(liste_ayrık[0])


        self.ids.label1.text = str(liste_ayrık[0][0][2:])
        self.ids.label2.text = liste_ayrık[0][1]
        self.ids.label3.text = str(liste_ayrık[0][5:8])[1:19]
        self.ids.label4.text = str(liste_ayrık[0][8:])

        self.ids.label5.text = str(liste_ayrık[1][0][2:])
        self.ids.label6.text = liste_ayrık[1][1]
        self.ids.label7.text = str(liste_ayrık[1][5:8])[1:19]
        self.ids.label8.text = str(liste_ayrık[1][8:])


        self.ids.label9.text = str(liste_ayrık[2][0][2:])
        self.ids.label10.text = liste_ayrık[2][1]
        self.ids.label11.text = str(liste_ayrık[2][5:8])[1:19]
        self.ids.label12.text = str(liste_ayrık[2][8:])


        self.ids.label13.text = str(liste_ayrık[3][0][2:])
        self.ids.label14.text = liste_ayrık[3][1]
        self.ids.label15.text = str(liste_ayrık[3][5:8])[1:19]
        self.ids.label16.text = str(liste_ayrık[3][8:])


        self.ids.label17.text = str(liste_ayrık[4][0][2:])
        self.ids.label18.text = liste_ayrık[4][1]
        self.ids.label19.text = str(liste_ayrık[4][5:8])[1:19]
        self.ids.label20.text = str(liste_ayrık[4][8:])


        self.ids.label21.text = str(liste_ayrık[5][0][2:])
        self.ids.label22.text = liste_ayrık[5][1]
        self.ids.label23.text = str(liste_ayrık[5][5:8])[1:19]
        self.ids.label24.text = str(liste_ayrık[5][8:])

        self.ids.label25.text = str(liste_ayrık[6][0][2:])
        self.ids.label26.text = liste_ayrık[6][1]
        self.ids.label27.text = str(liste_ayrık[6][5:8])[1:19]
        self.ids.label28.text = str(liste_ayrık[6][8:])


        self.ids.label29.text = str(liste_ayrık[7][0][2:])
        self.ids.label30.text = liste_ayrık[7][1]
        self.ids.label31.text = str(liste_ayrık[7][5:8])[1:19]
        self.ids.label32.text = str(liste_ayrık[7][8:])


        self.ids.label33.text = str(liste_ayrık[8][0][2:])
        self.ids.label34.text = liste_ayrık[8][1]
        self.ids.label35.text = str(liste_ayrık[8][5:8])[1:19]
        self.ids.label36.text = str(liste_ayrık[8][8:])


        self.ids.label37.text = str(liste_ayrık[9][0][2:])
        self.ids.label38.text = liste_ayrık[9][1]
        self.ids.label39.text = str(liste_ayrık[9][5:8])[1:19]
        self.ids.label40.text = str(liste_ayrık[9][8:])


kv = Builder.load_file("deneme.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    
    MyMainApp().run()
