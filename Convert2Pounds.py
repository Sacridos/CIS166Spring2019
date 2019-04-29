# Guancho Suriel
# Project Weight Converter
#  To convert from pounds to grams kilos and onces
#  CSI-166

from graphics import *
from button import *
import math

#def makeTable():
  
def cKilos(pounds): # Convert to Kilos    
    kilos = pounds * .4535
    return(round(kilos, ndigits=2)) 

def cOnces(pounds): # Convert to Onces   
    onces = pounds * 16
    return(round(onces, ndigits=2))

def cGrams(pounds): # Convert to Grams    
    grams = pounds * 453.592
    return(round(grams, ndigits=2))
   
def errorCheck(output1,output2,output3): #Error Print out
    output1.setText("please enter a number under the entry")
    output2.setText("please enter a number under the entry")
    output3.setText("please enter a number under the entry")
    

def main():

    win = GraphWin("empty",350,350)
    win.setCoords(0.0,0.0,3.5,3.5)
    win.setBackground("lightgray")

    wMessage = Text(Point(1.8,3), "Weight Converter" )
    wMessage.setSize(30)
    wMessage.setStyle("bold")
    wMessage.draw(win)
#  Create the Input for pounds     
    Text(Point(2.9,2.45),"lb").draw(win)
    input = Entry(Point(1.5,2.5),22)
    input.setSize(15)
    input.setText("")
    input.setFill("white")
    input.draw(win)
#  Create the Lable & Text box for Grams 
    Text(Point(.6,2.15),"Grams").draw(win)
    output1 = Entry(Point(1.7,1.9),30)
    output1.setText("0.0")
    output1.setFill("white")
    output1.draw(win)
#  Create the Lable & Text box for Kilograms     
    Text(Point(.73,1.6), "Kilograms").draw(win)
    output2 = Entry(Point(1.7,1.35),30)
    output2.setFill("white")
    output2.setText("0.0")
    output2.draw(win)
#  Create the Lable & Text boxbox for Onces     
    Text(Point(.6,1.05), "Onces").draw(win)
    output3 = Entry(Point(1.7,.8),30)
    output3.setFill("white")
    output3.setText("0.0")
    output3.draw(win)
#  Create the button of death or the one that does the work 
    convertButton = Button(win,Point(2,.3),1.2,.3,"Convert")
    convertButton.activate()
    ifClicked = win.getMouse()
#  Check to make sure Numbers where input if not error try agian
    while convertButton.clicked(ifClicked):
        try:
            pounds = eval(input.getText())
            output1.setText(cGrams(pounds))
            output2.setText(cKilos(pounds))
            output3.setText(cOnces(pounds))      
        except NameError:                      # Error incase letters where input to the
            errorCheck(output1,output2,output3)
        except TypeError:                      # Error incase both numbers and letters where input
            errorCheck(output1,output2,output3)
        except SyntaxError:                    # Error inase a Special character was input
            errorCheck(output1,output2,output3)
        except:                                # Error incase anything else is missed
            errorCheck(output1,output2,output3)      

        ifClicked = win.getMouse()    
    win.getMouse()

main()


'''
  


'''





    
