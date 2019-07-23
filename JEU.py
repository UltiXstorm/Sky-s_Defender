from tkinter import*
from random import*
import time
import sys


##################################    VARIABLES   ######################################################
"coordonnées du joueur à l'apparition"
x = 430
y = 700



p1=-1100
p2=-3098
score = 0
BEST = 0


lancement = 0
BOOMISSILE = 0
launch = 0
BS = 0
INF = 0
IG = 0

DG1 = randint(0,1)
DG2 = randint(0,1)
DG3 = randint(0,1)
DG4 = randint(0,1)
 
ymissile = 80
###########################            REGLAGE  DIFFICULTE         #####################################
vitesse = 10
lancementM = 5
lancementV = 20
vitesseM = 8

lancement1 = 0
lancement2 = 0
lancement3 = 0
lancement4 = 0

vitesseP = 2

ecart1 = 150
ecart2 = 150
ecart3 = 150
ecart4 = 150

rand1 = 900-ecart1
rand2 = 900-ecart2
rand3 = 900-ecart3
rand4 = 900-ecart4
##PLATFORME##
"""variable commune"""
bordG = 0
bordD = 900

#"""Etage 1"""#
Px1 = randrange(0,rand1,5)
Px2 = Px1+150

Py1= -30
#"""Etage 2"""#
Px3 = randrange(0,rand2,5)
Px4 = Px3+150

Py2= -810
#"""Etage 3"""#
Px5 = randrange(0,rand3,5)
Px6 = Px5+150


Py3= -1590
#"""Etage 4"""#
Px7 = randrange(0,rand4,5)
Px8 = Px7+150

Py4= -2370

####################################      OBJET       ##################################################
def platforme():
    global plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8
    global Py1, Py2, Py3, Py4, Px1, Px2, Px3, Px4, Px5, Px6, Px7, Px8

    

    ###CREATION###
    
    plat1 = can.create_rectangle(bordG,Py1+30,Px1,Py1, fill = "blue3")
    plat2 = can.create_rectangle(Px2,Py1+30,bordD,Py1, fill = "blue3")

    plat3 = can.create_rectangle(bordG,Py2+30,Px3,Py2, fill = "blue3")
    plat4 = can.create_rectangle(Px4,Py2+30,bordD,Py2, fill = "blue3")

    plat5 = can.create_rectangle(bordG,Py3+30,Px5,Py3, fill = "blue3")
    plat6 = can.create_rectangle(Px6,Py3+30,bordD,Py3, fill = "blue3")

    plat7 = can.create_rectangle(bordG,Py4+30,Px7,Py4, fill = "blue3")
    plat8 = can.create_rectangle(Px8,Py4+30,bordD,Py4, fill = "blue3")

###################################    DEFINITIONS    ############################################
def START():
    global decor, decor2, Joueur, MS, PC, nombre, TEXTS, nombre2, TEXTB, info, info2, IG
    decor = can.create_image(0, p1,anchor=NW, image=photo)
    decor2 = can.create_image(0, p2,anchor=NW, image=photo2)
    Joueur = can.create_image(x, y, anchor=NW, image=avion)
    MS = can.create_image(0, 0, anchor=NW, image=mothership)
    PC = can.create_image(900, 1, anchor=NW, image=commande)
    nombre = can.create_text(1050,177,anchor=CENTER,text = score ,fill = "white", font = "Arial 50 bold")
    TEXTS = can.create_text(1050,77, anchor=CENTER,text = "SCORE", fill = "RED", font = "Arial 40 bold")
    nombre2 = can.create_text(1050,377,anchor=CENTER,text = BEST ,fill = "white", font = "Arial 50 bold")
    TEXTB = can.create_text(1050,277, anchor=CENTER,text = "BEST", fill = "RED", font = "Arial 40 bold")
    info = can.create_text(1050,777, anchor=CENTER,text = "ATTENTION AUX", fill = "Black", font = "Arial 20 bold")
    info2 = can.create_text(1050,827, anchor=CENTER,text = "ONDES DE CHOCS !", fill = "Black", font = "Arial 20 bold")
    IG = 1
    platforme()


def INFOS():
        global info, info2, info3, INF, IG
        if score == 1:
            can.delete(info)
            can.delete(info2)
            IG = 0

        if score == lancementM and INF == 0:
            can.delete(info)
            can.delete(info2)
            info = can.create_text(1050,777, anchor=CENTER,text = "L'ENNEMI OUVRE", fill = "Black", font = "Arial 20 bold")
            info2 = can.create_text(1050,827, anchor=CENTER,text = "LE FEU !", fill = "Black", font = "Arial 20 bold")
            INF = 1
            IG = 1
            
        if score == lancementM+1 and INF == 1:
            can.delete(info)
            can.delete(info2)
            INF = 2
            IG = 0
      
        if score == lancementV and INF == 2:
            can.delete(info)
            can.delete(info2)
            info = can.create_text(1050,777, anchor=CENTER,text = "L'ENNEMI A", fill = "Black", font = "Arial 20 bold")
            info2 = can.create_text(1050,827, anchor=CENTER,text = "REPARE SON", fill = "Black", font = "Arial 20 bold")
            info3 = can.create_text(1050,877, anchor=CENTER,text = "SYSTEME DE VISER !", fill = "Black", font = "Arial 20 bold")
            INF = 3
            IG = 2

        
        if score == lancementV+1 and INF == 3:
            can.delete(info)
            can.delete(info2)
            can.delete(info3)
            IG = 0

    

def MAJ_score():
    global nombre, nombre2, TEXTS, TEXTB, score
    score = score+1
    can.delete(nombre)
    nombre = can.create_text(1050,177,anchor=CENTER,text = score ,fill = "white", font = "Arial 50 bold")
    can.delete(nombre2)
    nombre2 = can.create_text(1050,377,anchor=CENTER,text = BEST ,fill = "white", font = "Arial 50 bold")
def compte_score():
    global score, fond, nombre, TEXTS, nombre2, TEXTB, BEST

    if Py1+14 == y+16:
        MAJ_score()
        
    if Py2+14 == y+16:
        MAJ_score()
    
    if Py3+14 == y+16:
        MAJ_score()
        
    if Py4+14 == y+16:
        MAJ_score()

    if BEST < score:
        BEST = score
        can.delete(nombre2)
        nombre2 = can.create_text(1050,377,anchor=CENTER,text = BEST ,fill = "white", font = "Arial 50 bold")
        
def droite():
    for i in range(1):
        deplacement(10,1)
        fen.update()
        
def gauche():
    for i in range(1):
        deplacement(10,-1)
        fen.update() 
   
def game_over():
    global TEXT1, TEXT2, TEXT3, EXPLOSION, EXPLOM, BS, TEXT4, IG, info, info2
  
    can.delete(Joueur)
    EXPLOSION = can.create_image(x, y-2, anchor=NW, image=explosion)
    TEXT1 = can.create_text(450,350,anchor=CENTER,text = "MISSION TERMINEE", fill = "Blue", font = "Arial 50 bold")
    TEXT2 = can.create_text(450,450,anchor=CENTER,text = "Votre score est de:", fill = "Blue", font = "Arial 50 bold") 
    TEXT3 = can.create_text(450,550,anchor=CENTER,text = score ,fill = "Red", font = "Arial 50 bold")
    if BEST == score:
        BS = 1
        TEXT4 = can.create_text(450,650,anchor=CENTER,text = "C'EST VOTRE MEILLEUR SCORE !" ,fill = "purple", font = "Arial 40 bold")
    if BOOMISSILE == 1:
        can.delete(MISSILE)
        EXPLOM = can.create_image(xmissile-11, ymissile-6, anchor=NW, image=explosion)
    if IG == 1:
        can.delete(info)
        can.delete(info2)
    if IG == 2:
        can.delete(info)
        can.delete(info2)
        can.delete(info3)
    info = can.create_text(1050,777, anchor=CENTER,text = "APPUIE SUR ENTREE", fill = "Black", font = "Arial 20 bold")
    info2 = can.create_text(1050,827, anchor=CENTER,text = "POUR REJOUER", fill = "Black", font = "Arial 20 bold")
        

def M_S():
    global MS
    can.delete(MS)
    MS = can.create_image(0, 0, anchor=NW, image=mothership)

def syst_visé():
    global xmissile

    if lancementM <= score:
        CHOIX = randint(0,1)
        if CHOIX == 0:
            xmissile = randrange(20,370,50)
        if CHOIX == 1:
            xmissile = randrange(570,920,50)

    if lancementV <= score:
        if 0 <= x+16 <= 50:
            xmissile = 20
        if 51 <= x+16 <= 100:
            xmissile = 70
        if 101 <= x+16 <= 150:
            xmissile = 120
        if 151 <= x+16 <= 200:
            xmissile = 170
        if 201 <= x+16<= 250:
            xmissile = 220
        if 251 <= x+16 <= 300:
            xmissile = 270
        if 301 <= x+16 <= 450:
            xmissile = 320            
        if 451 <= x+16 <= 600:
            xmissile = 570
        if 601 <= x+16 <= 650:
            xmissile = 620
        if 651 <= x+16 <= 700:
            xmissile = 670
        if 701 <= x+16 <= 750:
            xmissile = 720
        if 751 <= x+16 <= 800:
            xmissile = 770
        if 801 <= x+16 <= 850:
            xmissile = 820
        if 851 <= x+16 <= 900:
            xmissile = 870

def armement_ennemi():
    global MISSILE, launch
    
    if score >= lancementM and launch == 0:
        syst_visé()
        MISSILE = can.create_image(xmissile, ymissile, anchor=NW, image= missile )
        launch = 1
        
def rearmement():
    global ymissile, MISSILE
    if score >= lancementM:
        can.move(MISSILE, 0, vitesseM)
        ymissile = ymissile +vitesseM
        if ymissile >= 900 :
            can.delete(MISSILE)
            syst_visé()
            ymissile = 80
            MISSILE = can.create_image(xmissile, ymissile, anchor=NW, image= missile )
            
def deplacement(dplX,X):
    global x, BOOM
    for i in range(dplX):
        if BOOM == 1:
            break
        can.move(Joueur,X,0)
        x=x+X

def déplacement_étage(platG,platD):
    can.move(platD,0,+2)
    can.move(platG,0,+2)

def delete_plat():
    can.delete(plat1)
    can.delete(plat2)
    can.delete(plat3)
    can.delete(plat4)
    can.delete(plat5)
    can.delete(plat6)
    can.delete(plat7)
    can.delete(plat8)
    
def renouvellement_de_plat():
    global plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8
    global Py1, Py2, Py3, Py4, Px1, Px2, Px3, Px4, Px5, Px6, Px7, Px8, DG1, DG2, DG3, DG4

    if Py1==2310:
        can.delete(plat1)
        can.delete(plat2)
        Py1 = -810
        Px1 = randrange(0,rand1,5)
        Px2 = Px1+ecart1
        DG1 = randint(0,1)
        plat1 = can.create_rectangle(bordG,Py1+30,Px1,Py1, fill = "blue3")
        plat2 = can.create_rectangle(Px2,Py1+30,bordD,Py1, fill = "blue3")
    déplacement_étage(plat1,plat2)
    Py1 = Py1+2

    if Py2==2310:
        can.delete(plat3)
        can.delete(plat4)
        Py2 = -810
        Px3 = randrange(0,rand2,5)
        Px4 = Px3+ecart2
        DG2 = randint(0,1)
        plat3 = can.create_rectangle(bordG,Py2+30,Px3,Py2, fill = "blue3")
        plat4 = can.create_rectangle(Px4,Py2+30,bordD,Py2, fill = "blue3")
    déplacement_étage(plat3,plat4)
    Py2 = Py2+2
        
    if Py3==2310:
        can.delete(plat5)
        can.delete(plat6)
        Py3 = -810
        Px5 = randrange(0,rand3,5)
        Px6 = Px5+ecart3
        DG3 = randint(0,1)
        plat5 = can.create_rectangle(bordG,Py3+30,Px5,Py3, fill = "blue3")
        plat6 = can.create_rectangle(Px6,Py3+30,bordD,Py3, fill = "blue3")
    déplacement_étage(plat5,plat6)
    Py3 = Py3+2

    if Py4==2310:
        can.delete(plat7)
        can.delete(plat8)
        Py4 = -810
        Px7 = randrange(0,rand4,5)
        Px8 = Px7+ecart4
        DG4 = randint(0,1)
        plat7 = can.create_rectangle(bordG,Py4+30,Px7,Py4, fill = "blue3")
        plat8 = can.create_rectangle(Px8,Py4+30,bordD,Py4, fill = "blue3")
    déplacement_étage(plat7,plat8)
    Py4 = Py4+2



def plat_mouvante(lancement1, lancement2, lancement3, lancement4):
    global Px1, Px2, Px3, Px4, Px5, Px6, Px7, Px8, plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8, DG1, DG2, DG3, DG4

    for i in range(1):
        if lancement1 <= score and 0 < Py1 < 900:
            if DG1 == 0:
                Px1 = Px1-vitesseP
                Px2 = Px1+ecart1
                can.delete(plat1)
                can.delete(plat2)
                plat1 = can.create_rectangle(bordG,Py1+30,Px1,Py1, fill = "blue3")
                plat2 = can.create_rectangle(Px2,Py1+30,bordD,Py1, fill = "blue3")
                if Px1 <= bordG+5:
                    DG1 = 1                           
            if DG1 == 1:
                Px1 = Px1+vitesseP
                Px2 = Px1+ecart1
                can.delete(plat1)
                can.delete(plat2)
                plat1 = can.create_rectangle(bordG,Py1+30,Px1,Py1, fill = "blue3")
                plat2 = can.create_rectangle(Px2,Py1+30,bordD,Py1, fill = "blue3")
                if Px2 >= bordD-5:
                    DG1 = 0




        if lancement2 <= score and 0 < Py2 < 900:
            if DG2 == 0:
                Px3 = Px3-vitesseP
                Px4 = Px3+ecart2
                can.delete(plat3)
                can.delete(plat4)
                plat3 = can.create_rectangle(bordG,Py2+30,Px3,Py2, fill = "blue3")
                plat4 = can.create_rectangle(Px4,Py2+30,bordD,Py2, fill = "blue3")
                if Px3 <= bordG+5:
                    DG2 = 1                          
            if DG2 == 1:
                Px3 = Px3+vitesseP
                Px4 = Px3+ecart2
                can.delete(plat3)
                can.delete(plat4)
                plat3 = can.create_rectangle(bordG,Py2+30,Px3,Py2, fill = "blue3")
                plat4 = can.create_rectangle(Px4,Py2+30,bordD,Py2, fill = "blue3")
                if Px4 >= bordD-5:
                    DG2 = 0




        if lancement3 <= score and 0 < Py3 < 900:
            if DG3 == 0:
                Px5 = Px5-vitesseP
                Px6 = Px5+ecart3
                can.delete(plat5)
                can.delete(plat6)
                plat5 = can.create_rectangle(bordG,Py3+30,Px5,Py3, fill = "blue3")
                plat6 = can.create_rectangle(Px6,Py3+30,bordD,Py3, fill = "blue3")
                if Px5 <= bordG+5:
                    DG3 = 1                
            if DG3 == 1:
                Px5 = Px5+vitesseP
                Px6 = Px5+ecart3
                can.delete(plat5)
                can.delete(plat6)
                plat5 = can.create_rectangle(bordG,Py3+30,Px5,Py3, fill = "blue3")
                plat6 = can.create_rectangle(Px6,Py3+30,bordD,Py3, fill = "blue3")
                if Px6 >= bordD-5:
                    DG3 = 0




        if lancement4 <= score and 0 < Py4 < 900:
            if DG4 == 0:
                Px7 = Px7-vitesseP
                Px8 = Px7+ecart4
                can.delete(plat7)
                can.delete(plat8)
                plat7 = can.create_rectangle(bordG,Py4+30,Px7,Py4, fill = "blue3")
                plat8 = can.create_rectangle(Px8,Py4+30,bordD,Py4, fill = "blue3")     
                if Px7 <= bordG+5:
                    DG4 = 1                
            if DG4 == 1:
                Px7 = Px7+vitesseP
                Px8 = Px7+ecart4
                can.delete(plat7)
                can.delete(plat8)
                plat7 = can.create_rectangle(bordG,Py4+30,Px7,Py4, fill = "blue3")
                plat8 = can.create_rectangle(Px8,Py4+30,bordD,Py4, fill = "blue3")
                if Px8 >= bordD-5:
                    DG4 = 0


                
#########################################         HITBOX             #######################################

def hit_etage1(Ax1,Ay1,Ax2,Ay2):
    global BOOM
    if bordG <= Ax1 <= Px1 and Py1 <= Ay1 <= Py1+30:
        BOOM = 1
    if Px2 <= Ax2 <= bordD and Py1 <= Ay2 <= Py1+30:
        BOOM = 1

def hit_etage2(Ax1,Ay1,Ax2,Ay2):
    global BOOM
    if bordG <= Ax1 <= Px3 and Py2 <= Ay1 <= Py2+30:
        BOOM = 1
    if Px4 <= Ax2 <= bordD and Py2 <= Ay2 <= Py2+30:
        BOOM = 1

def hit_etage3(Ax1,Ay1,Ax2,Ay2):
    global BOOM
    if bordG <= Ax1 <= Px5 and Py3 <= Ay1 <= Py3+30:
        BOOM = 1
    if Px6 <= Ax2 <= bordD and Py3 <= Ay2 <= Py3+30:
        BOOM = 1

def hit_etage4(Ax1,Ay1,Ax2,Ay2):
    global BOOM
    if bordG <= Ax1 <= Px7 and Py4 <= Ay1 <= Py4+30:
        BOOM = 1
    if Px8 <= Ax2 <= bordD and Py4 <= Ay2 <= Py4+30:
        BOOM = 1

def hit_missile(Ax1,Ay1,Ax2,Ay2):
    global BOOM, BOOMISSILE
    if xmissile <= Ax1 <= xmissile +9 and ymissile <= Ay1 <= ymissile+20:
        BOOM = 1
        BOOMISSILE = 1
    if xmissile <= Ax2 <= xmissile +9 and ymissile <= Ay2 <= ymissile+20:
        BOOM = 1
        BOOMISSILE = 1

   
def rac_HIT(name):
    name(x+15,y,x+17,y)
    name(x+14,y+1,x+18,y+1)
    name(x+13,y+3,x+19,y+3)
    name(x+12,y+5,x+20,y+5)
    name(x+11,y+7,x+21,y+7)
    name(x+10,y+9,x+22,y+9)
    name(x+9,y+11,x+23,y+11)
    name(x+8,y+13,x+24,y+13)
    name(x+7,y+15,x+25,y+15)
    name(x+6,y+16,x+26,y+16)
    name(x+5,y+17,x+27,y+17)        
    name(x+4,y+18,x+28,y+18)
    name(x+3,y+19,x+29,y+19)
    name(x+2,y+20,x+30,y+20)
    name(x+1,y+21,x+31,y+21)
    name(x+1,y+24,x+31,y+24)
    name(x+2,y+25,x+30,y+25)
    name(x+8,y+28,x+24,y+28)
    name(x+8,y+30,x+24,y+30)
    name(x+9,y+31,x+23,y+31)

   
def HITBOX():
    global BOOM, BOOMISSILE
    BOOM = 0
    BOOMISSILE = 0

    if x+30 >= bordD:
        BOOM = 2
    if x <= bordG:
        BOOM = 3

    rac_HIT(hit_etage1)

    rac_HIT(hit_etage2)

    rac_HIT(hit_etage3)

    rac_HIT(hit_etage4)

    if score >= lancementM:   
        rac_HIT(hit_missile)




###################################    MOTEUR DE JEU    ############################################   
def MOTEUR2():
    global p1, p2, Joueur, decor, decor2
    for i in range(1):
        if BOOM == 1:
            break
        can.move(decor,0,0.5)
        p1=p1+0.5
        can.move(decor2,0,0.5)
        p2=p2+0.5
        if p1==900:
            can.delete(decor)
            p1=-3097
            can.delete(Joueur)
            delete_plat()
            decor = can.create_image(0, p1,anchor=NW, image=photo)
            Joueur = can.create_image(x, y, anchor=NW, image=avion)
            platforme()
        if p2==900:
            can.delete(decor2)
            p2=-3097
            can.delete(Joueur)
            delete_plat()
            decor2 = can.create_image(0, p2,anchor=NW, image=photo2)
            Joueur = can.create_image(x, y, anchor=NW, image=avion)
            platforme()
        can.after(vitesse, MOTEUR2)

    
def MOTEUR():
    global Joueur, BOOM, MS
    for i in range(1):
        renouvellement_de_plat()
        plat_mouvante(lancement1, lancement2, lancement3, lancement4)
        M_S()
        compte_score()
        INFOS()
        armement_ennemi()
        rearmement()
        HITBOX()
        if BOOM == 1:
            game_over()
            break
        fen.update()
        
        can.after(vitesse, MOTEUR)
###################################         JEU          ##########################       
def Jeu():
    for i in range(1):
        global BOOM
        
        MOTEUR()
        MOTEUR2()
        if BOOM == 1:
            break
        
#######################################      JOUABILTE      ###############################################
def clavier(event):
    global vitesse, lancement, x, y, score, vitesse, bordG, bordD, Px1, Px2, Px3, Px4, Px5, Px6, Px7, Px8, Py1, Py2, Py3, Py4, TEXT1 ,TEXT2, TEXT3
    global launch, ymissile, BS, DG1, DG2, DG3, DG4, INF
    touche = event.keysym

    if touche == "Right":
        for i in range(1):
            if BOOM == 2:
                break
            droite()
    if touche == "Left":
        for i in range(1):
            if BOOM == 3:
                break
            gauche()
    if touche == "Return":

        if lancement ==0 :
            lancement = 1
            can.delete(ECRANTITRE)
            can.delete(ECRANTITRE2)
            START()
            Jeu()
            
        if BOOM == 1:
            ymissile = 80
            x = 430
            y = 700
            launch = 0
            score = 0
            INF = 0
            DG1 = randint(0,1)
            DG2 = randint(0,1)
            DG3 = randint(0,1)
            DG4 = randint(0,1)       
            bordG = 0
            bordD = 900
            Px1 = randrange(0,rand1,5)
            Px2 = Px1+ecart1
            Py1= -30
            Px3 = randrange(0,rand2,5)
            Px4 = Px3+ecart2
            Py2= -810
            Px5 = randrange(0,rand3,5)
            Px6 = Px5+ecart3
            Py3= -1590
            Px7 = randrange(0,rand4,5)
            Px8 = Px7+ecart4
            Py4= -2370

            can.delete(decor)
            can.delete(decor2)
            can.delete(EXPLOSION)
            can.delete(plat1)
            can.delete(plat2)
            can.delete(plat3)
            can.delete(plat4)
            can.delete(plat5)
            can.delete(plat6)
            can.delete(plat7)
            can.delete(plat8)
            can.delete(TEXT1)
            can.delete(TEXT2)
            can.delete(TEXT3)
            can.delete(info)
            can.delete(info2)
            
            if BOOMISSILE == 1:
                can.delete(EXPLOM)
            if BS == 1:
                can.delete(TEXT4)
                BS = 0
            START()
            Jeu()
            
##########################   FENETRE DE JEU + ECRAN TITRE   ###############################################
fen=Tk()
fen.title('PROJET') #titre de la fenetre

can=Canvas(fen,height=900,width=1198, bg = "blue3") #Dimension de l'écran de jeu"
can.pack(side=TOP)

photo = PhotoImage(file="map.gif")
photo2 = PhotoImage(file="map.gif")
avion = PhotoImage(file="mirage2002.gif")
titre = PhotoImage(file="titremodif.gif")
mothership = PhotoImage(file="SHIP.gif")
missile = PhotoImage(file="MISSILE.gif")
explosion = PhotoImage(file="explosion.gif")
commande = PhotoImage(file="PC.gif")

bou1=Button(fen,text="QUITTER",command=fen.destroy)
bou1.pack(side=BOTTOM)

can.focus_set()
can.bind("<Key>", clavier)

ECRANTITRE = can.create_image(0, 0, anchor=NW, image= titre)
ECRANTITRE2= can.create_text(600,650, anchor=CENTER,text = "APPUYEZ SUR ENTREE POUR JOUER", fill = "Black", font = "Arial 20 bold")

fen.mainloop()
