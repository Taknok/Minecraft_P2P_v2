# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:21:27 2015

@author: Paul
"""
def Update():
    try:
        import urllib.request
        
        PageUpdate = "https://drive.google.com/folderview?id=0B2C3bbpA-keER0lDTi1MdjYzYmc&usp=sharing"      #navigue jusqu'a la page dans le drive
        Page_Web = str(urllib.request.urlopen(PageUpdate).read())                                           #récupère le code source
        a = 0   
        Liste_Version = []
        while a != -1:                                              #on recherche le nom du script(a jour) dans le drive
            a = Page_Web.find("""cercledraw""")
            if a == -1:
                break
            b = Page_Web.find(""".py""",a ,a + 40)
            Old_Version = Page_Web[a:b + 3:]
            Liste_Version.append(Old_Version)
            Page_Web = Page_Web.replace("""cercledraw""","""""",1)      #on supprime celui trouvé pour ne plus le trouver
        
        n = len(Liste_Version)
        Liste_Version = Liste_Version[0:int(n/2):]                  #le nom se trouve 2 fois dans le code source, donc on divise par 2 la liste
        
        
        A_Jour = False
        for i in range(int(n/2)):
            if Liste_Version[i] == Version:
                A_Jour = True        
        
        if A_Jour == True:
            print("\nLe script est à jour\n\n")
        else:
            print("\nNouvelle version du script disponible !\n\n")
    except:
        print("""\nImpossible de se connecter pour vérifier la dernière version du script\n""")