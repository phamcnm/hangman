"""This is a program that allows you to play the game hangman. Requires that Zelle's graphics.py and textfiles grade3.txt, grade4.txt, grade5.txt and grade6.txt are in the same directory as this file.

hangman.py
Authors: Sasha Mothershead, Minh Pham, and Zoe Pharo, and Titus Klinge
Date: 2019-03-17

"""

from graphics import *
import random
   
def drawComments(comments, win):
    
    """Draws comments in a box to prompt the user 

    Parameters:
        comments: a string 
        win: a window


    Postconditions:
        * every time this function is called, a new box is drawn over the last
        * the function returns a Text object to win located at point 360, 103 and a rectangle based at points (50, 150) and (670, 50)
    """
        
    commentBox = Rectangle(Point(50,150), Point(670,50))
    commentBox.setFill("hot pink")
    commentBox.draw(win)
    com = Text(Point(360,103), comments)
    com.setFace("helvetica")
    com.setSize(32)
    com.setStyle("bold")
    com.setTextColor("white")
    com.draw(win)
    
def DrawHomeScreen(win):
    
    """Draws home screen of Hangman 

    Parameters:
        win: a window
        
    Preconditions:
        * win must be large enough for the anchor points of the objects to be valid. A 1000 x 700 win returns the objects in their desired locations
        
    Postconditions:
        * draws title, a box for each grade level (3, 4, 5, 6), and a box that prompts the user to click for instructions to win
    """
    
    cover_win = Rectangle(Point(0,0), Point(1000,700))
    cover_win.setFill("hot pink")
    cover_win.draw(win)
        
    heading = Text(Point(500, 100), "Play Hangman")
    heading.setFace("helvetica")
    heading.setSize(36)
    heading.setStyle("bold")
    heading.setTextColor("white")
    subheading = Text(Point(500, 137), "Select a Grade Level to Play")
    subheading.setSize(14)
    subheading.setFace("helvetica")
        
    grade3_rect = Rectangle(Point(250,190), Point(480, 250))
    grade3_rect.setFill("PaleVioletRed1")
    grade3_txt = Text(Point(365, 220), "Grade 3")
    grade3_txt.setStyle("bold")
    grade3_txt.setSize(14)
    grade3_txt.setTextColor("white")
        
    grade4_rect = Rectangle(Point(520, 190), Point(750, 250))
    grade4_rect.setFill("PaleVioletRed2")
    grade4_txt = Text(Point(635, 220), "Grade 4")
    grade4_txt.setStyle("bold")
    grade4_txt.setSize(14)
    grade4_txt.setTextColor("white")
              
    grade5_rect = Rectangle(Point(250, 300), Point(480, 360))
    grade5_rect.setFill("PaleVioletRed3")
    grade5_txt = Text(Point(365, 330), "Grade 5")
    grade5_txt.setStyle("bold")
    grade5_txt.setSize(14)
    grade5_txt.setTextColor("white")
        
    grade6_rect = Rectangle(Point(520, 300), Point(750, 360))
    grade6_rect.setFill("PaleVioletRed4")
    grade6_txt = Text(Point(635, 330), "Grade 6")
    grade6_txt.setStyle("bold")
    grade6_txt.setSize(14)
    grade6_txt.setTextColor("white")
        
    instruct_rect = Rectangle(Point(390, 500), Point(610, 570))
    instruct_rect.setFill("pale goldenrod")
    instruct_txt = Text(Point(500, 535), "Click here for instructions")
    instruct_txt.setFace("helvetica")
    instruct_txt.setSize(12)
        
    heading.draw(win)
    subheading.draw(win)
    grade3_rect.draw(win)
    grade3_txt.draw(win)
    grade4_rect.draw(win)
    grade4_txt.draw(win)
    grade5_rect.draw(win)
    grade5_txt.draw(win)
    grade6_rect.draw(win)
    grade6_txt.draw(win)
    instruct_rect.draw(win)
    instruct_txt.draw(win)
        
def CheckHomeScreen(click):
    
    """Checks to see where the user clicks in the home screen 

    Parameters:
        click: click of the user, a point value 
        
    Returns:
        * 3 if the user clicks on the "Grade 3" box
        * 4 if the user clicks on the "Grade 4" box
        * 5 if the user clicks on the "Grade 5" box
        * 6 if the user clicks on the "Grade 6" box
        * "instructions" if the user clicks on the "Click here for instructiions" box
    """
    
    if 250 <= click.getX() <= 480 and 190 <= click.getY() <= 250:
        return 3
    elif 520 <= click.getX() <= 750 and 190 <= click.getY() <= 250:
        return 4
    elif 250 <= click.getX() <= 480 and 300 <= click.getY() <= 360:
        return 5
    elif 520 <= click.getX() <= 750 and 300 <= click.getY() <= 360:
        return 6
    elif 390 <= click.getX() <= 610 and 500 <= click.getY() <= 570:
        return "instructions"
            
def DrawInstructions(win):
    
    """Draws instructions page 

    Parameters:
        win: a window 
        
    Preconditions:
        * win must be large enough for the anchor points of the objects to be valid. A 1000 x 700 win returns the objects in their desired locations

    Postconditions:
        * a win with the title, instruction box, instruction text, and home button objects drawn
        * if the user clicks in the "Ready to play? Click to return to home screen" box, the home screen appears   
    """
    
    background = Rectangle(Point(0,0), Point(1000,700))
    background.setFill("cornflower blue")
    background.draw(win)
        
    heading = Text(Point(500, 100), "How to Play Hangman")
    heading.setFace("helvetica")
    heading.setSize(36)
    heading.setStyle("bold")
    heading.setTextColor("white")
    heading.draw(win)
        
    instruct_box  = Rectangle(Point(50, 150), Point(950, 610))
    instruct_box.setFill("white")
    instruct_box.draw(win)
    
    instruct_txt = Text(Point(500, 365), "1. Select your grade level to begin the game \n\n 2. Try to guess the hidden word by clicking a letter on the keyboard \n\n (you may only guess this letter once) \n\n 3. If your guess is correct (and the letter appears in the hidden word), \n\n the letter will be revealed in its proper place in the hidden word \n OR \n If your guess is incorrect, a body part will be added to the hangman \n\n 4. If you correctly guess all letters in the word, you win! \n OR \n But be careful! If the hangman drawing is completed, you lose")
    instruct_txt.setFace("helvetica")
    instruct_txt.setSize(22)
    instruct_txt.draw(win)
        
    home_button = Rectangle(Point(350, 630), Point(650, 680))
    home_button.setFill("white")
    home_button.draw(win)
        
    home_button_txt = Text(Point(500, 655), "Ready to play? Click to return to home screen")
    home_button_txt.draw(win)
    
def HomeScreen(win, word_list, listgrade3, listgrade4, listgrade5, listgrade6):  
    
    """Creates a list of words that correspond to the grade level (3-6) selected by the user

    Parameters:
        win: a window
        word_list: a list of words 
        listgrade3: a list of words appropriate for third graders
        listgrade4: a list of words appropriate for fourth graders
        listgrade5: a list of words appropriate for fifth graders 
        listgrade6: a list of words appropriate for sixth graders 
    
    Precondition:
        * function CheckHomeScreen must be accessible and working properly
        
    Postconditions: 
        * word_list is set to whichever list corresponds with the user's click (ie. if the user clicks in the grade 3 area, word_list is set to listgrade3) 
        * the length of word_list is equal to the length of whichever list is appended to it
    """
    
    playing_yet = "no"
    while playing_yet == "no":
        DrawHomeScreen(win)
        homeclick = win.getMouse()
        if CheckHomeScreen(homeclick) == 3:
            for i in listgrade3:
                word_list.append(i)
            playing_yet = "yes"
        elif CheckHomeScreen(homeclick) == 4:
            for i in listgrade4:
                word_list.append(i)
            playing_yet = "yes"
        elif CheckHomeScreen(homeclick) == 5:
            for i in listgrade5:
                word_list.append(i)
            playing_yet = "yes"
        elif CheckHomeScreen(homeclick) == 6:
            for i in listgrade6:
                word_list.append(i)
            playing_yet = "yes"
        elif CheckHomeScreen(homeclick) == "instructions":
            DrawInstructions(win)
            instruct_click = win.getMouse()
            if 350 <= instruct_click.getX() <= 650 and 630 <= instruct_click.getY() <= 680:
                playing_yet = "no"
        else:
            playing_yet = "no"
    
def DrawEndScreen(win):
    
    """Draws the end screen 

    Parameters:
        win: a window 
    
    Preconditions:
        * win must be large enough for the anchor points of the objects to be valid. A 1000 x 700 win returns the objects in their desired locations
     
    Postcondition:
        * draws a new screen to win that includes a heading and two boxes 
    """
    
    cover_win = Rectangle(Point(0,0), Point(1000,700))
    cover_win.setFill("Hot Pink")
    cover_win.draw(win)
        
    heading = Text(Point(500, 250), "Do you want to play again?")
    heading.setFace("helvetica")
    heading.setSize(36)
    heading.setStyle("bold")
    heading.setTextColor("white")
              
    yes_rect = Rectangle(Point(250, 300), Point(480, 360))
    yes_rect.setFill("PaleVioletRed3")
    yes_txt = Text(Point(365, 330), "Yes, again!")
    yes_txt.setStyle("bold")
    yes_txt.setSize(14)
    yes_txt.setTextColor("white")
        
    no_rect = Rectangle(Point(520, 300), Point(750, 360))
    no_rect.setFill("PaleVioletRed4")
    no_txt = Text(Point(635, 330), "No, I'm calling it quits")
    no_txt.setStyle("bold")
    no_txt.setSize(14)
    no_txt.setTextColor("white")     
    
    heading.draw(win)
    yes_rect.draw(win)
    yes_txt.draw(win)
    no_rect.draw(win)
    no_txt.draw(win)
        
def CheckEndScreen(click):
    """Checks to see where the user clicked on the end screen  

    Parameters:
        click: click of the user 
        
    Postcondition:
        * if the user clicks within the "Yes, again!" box, the function returns "yes play again" 
        * if the user clicks within the "No, I'm calling it quits" box, the function returns "no, quit" 
    """
    
    if 250 <= click.getX() <= 480 and 300 <= click.getY() <= 360:
        return "yes, play again"
    elif 520 <= click.getX() <= 750 and 300 <= click.getY() <= 360:
        return "no, quit"

class Hangman: 
    """A class that creates an object representing the "hanged" person"""
    def __init__(self):
        """A constructor of the Hangman object. Needs no instance variables to be passed in by the user"""
        self.body_parameters = ["head", "torso", "leftarm", "rightarm", "leftleg", "rightleg"]    
    def drawHangman(self, wrong_count, win):
        """A method that draws the body parts of Hangman to win
        Parameters:
            wrong_count: an integer consisting of the number of wrong guesses the person has made
            
            win: the window 
        Preconditions:
            *the wrong_count is a parameter passed in from the main that is an integer in range(0, 6)
            
        Postconditions:
            *if wrong_count > -1, a body part (from self.body_parameters) is drawn on the window
            *as wrong_count increases, the number of body parts drawn to the screen also increases to correspond
            
        """ 
        circ = Circle(Point(700, 200), 40)
        circ.setWidth(5)
        circ.setOutline("hot pink")
        circ.setFill("yellow")
        circ.draw(win)
        reye = Circle(Point(680, 195), 4)
        reye.setWidth(5)
        reye.setOutline("hot pink")
        reye.draw(win)
        leye = Circle(Point(720, 195), 4)
        leye.setWidth(5)
        leye.setOutline("hot pink")
        leye.draw(win)
        if self.body_parameters[wrong_count] == "head":
            mouth = Line(Point(680,220), Point(720,220))
            mouth.setWidth(7)
            mouth.setFill("hot pink")
            mouth.draw(win)
        if self.body_parameters[wrong_count] == "torso":
            ln1 = Line(Point(700, 240), Point(700, 370))
            ln1.setWidth(5)
            ln1.setFill("hot pink")
            ln1.draw(win)
            mouth = Line(Point(682,222), Point(701,220))
            mouth.setWidth(7)
            mouth.setFill("hot pink")
            mouth.draw(win)
            mouth = Line(Point(718,222), Point(699,220))
            mouth.setWidth(7)
            mouth.setFill("hot pink")
            mouth.draw(win)
        if self.body_parameters[wrong_count] == "leftarm":
            ln2 = Line(Point(700, 270), Point(650, 320))
            ln2.setWidth(5)
            ln2.setFill("hot pink")
            ln2.draw(win)
            mouth = Line(Point(683,223), Point(701,220))
            mouth.setWidth(7)
            mouth.setFill("hot pink")
            mouth.draw(win)
            mouth = Line(Point(717,223), Point(699,220))
            mouth.setWidth(7)
            mouth.setFill("hot pink")
            mouth.draw(win)
        if self.body_parameters[wrong_count] == "rightarm":
            ln3 = Line(Point(700, 270), Point(750, 320))
            ln3.setWidth(5)
            ln3.setFill("hot pink")
            ln3.draw(win)
            mouth = Line(Point(685,224), Point(702,220))
            mouth.setWidth(7)
            mouth.setFill("hot pink")
            mouth.draw(win)
            mouth = Line(Point(715,224), Point(698,220))
            mouth.setWidth(7)
            mouth.setFill("hot pink")
            mouth.draw(win)
        if self.body_parameters[wrong_count] == "leftleg":
            ln4 = Line(Point(700, 370), Point(650, 440))
            ln4.setWidth(5)
            ln4.setFill("hot pink")
            ln4.draw(win)
            mouth = Line(Point(686,226), Point(702,220))
            mouth.setWidth(7)
            mouth.setFill("hot pink")
            mouth.draw(win)
            mouth = Line(Point(714,226), Point(698,220))
            mouth.setWidth(7)
            mouth.setFill("hot pink")
            mouth.draw(win)
            d = 0
            while d<20:
                d = d + 6
                tear = Line(Point(678, 195 + d), Point(682, 195 + d))
                tear.setWidth(4)
                tear.setOutline("white")
                tear.draw(win)             
        if self.body_parameters[wrong_count] == "rightleg":
            ln5 = Line(Point(700, 370), Point(750, 440))
            ln5.setWidth(5)
            ln5.setFill("hot pink")
            ln5.draw(win)
            reye.undraw()
            leye.undraw()
            reye = Line(Point(678, 195), Point(682, 195))
            reye.setWidth(7)
            reye.setOutline("hot pink")
            reye.draw(win)
            leye = Line(Point(718, 195), Point(722, 195))
            leye.setWidth(7)
            leye.setOutline("hot pink")
            leye.draw(win)
            mouth = Line(Point(693,220), Point(707,220))
            mouth.setWidth(7)
            mouth.setFill("hot pink")
            mouth.draw(win)

                    
    def drawHang(self, win):
        """A method that draws the hanging structure on the window
        Parameters:
            win: the window that the hanging structure will be drawn on
        
        Preconditions:
            * win must be large enough for the anchor points of the objects to be valid. A 1000 x 700 win returns the objects in their desired locations
            
        Posconditions:
            *A hanging structure is drawn on the window    
            
        """  
        ln1 = Line(Point(700, 160), Point(700, 100))
        ln2 = Line(Point(700, 100), Point(900, 100))
        ln3 = Line(Point(900, 100), Point(900, 450))
        ln4 = Line(Point(870, 450), Point(930, 450))
    
        ln1.setWidth(5)
        ln2.setWidth(5)
        ln3.setWidth(5)
        ln4.setWidth(5)
        
        ln1.setFill("pink")
        ln2.setFill("pink")
        ln3.setFill("pink")
        ln4.setFill("pink")
        
        ln1.draw(win)
        ln2.draw(win)
        ln3.draw(win)
        ln4.draw(win)
                
                    
class wordbank:
    """An object that represents the word bank"""
    def __init__(self):
        """The wordbank constructor. Does not need any instance variables to be passed in"""
        self.wb = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.incorrects = []
        
    def getKeyCheck(self, win):
        """A method that pauses the program to allow the user to press a key and checks if that key is stored within the wordbank object
        
        Parameters:
            win: a window 
            
        Preconditions:
            *graphics.py must be in the same folder and getKey() must work properly   
            *user must type a key
            *drawComments function must be accessible and work properly
            
        Returns:
            A letter (string)
            
        Postconditions:
            *if the guessed key is in the wordbank, then this letter will be returned
            *if the gussed key is not in the wordbank, the function will draw a comment to let the user know that the letter has already been guessed and will loop until a guess is acceptable   
        """
        move = False
        while move == False:
            guess = win.getKey()
            if guess in self.wb:
                move = True
                return guess
            else:
                drawComments("Letter has already been guessed", win)
                
    def updateWB(self, letter):
        """A method that updates the wordbank list by checking to see if the list contains letter and--if it does--by turning this index into an empty string
        
        Parameters:
            letter: a letter, type: string
            
        Returns:
            an updated self.wb
            
        Postconditions:
            *the self.wb list will be changed so that if letter had previously existed within it, that index is now an empty string
        """
        for i in range(len(self.wb)):
            if self.wb[i] == letter:
                self.wb[i] = ""
        return self.wb
    
    def drawWB(self, win):
        """A method that draws the wordbank list to the win
        
        Parameters:
            win: a window
            
        Preconditions:
            * win must be large enough for the anchor points of the wordbank text to be valid. A 1000 x 700 win returns the objects in their desired locations
            
        Postconditions:
            *a box is drawn to the win containing the elements of self.wb
            *if self.wb[i] == "", nothing is drawn to the screen
        """
        boxWB = Rectangle(Point(50, 650), Point(750, 500))
        boxWB.setFill("PaleVioletRed1")
        boxWB.draw(win)
        x = 50
        for i in self.wb[:13]:
            let = Text(Point(50 + x, 550), i)
            let.draw(win)
            x = x + 50
        x = 50
        for i in self.wb[13:]:
            let = Text(Point(50 + x, 600), i)
            let.draw(win)
            x = x + 50

    def updateIncorrects(self, letter):
        """A method that updates the list of incorrect guesses by appending a letter to it
        
        Parameters:
            letter: a letter, type: string
            
        Returns:
            the updated list of incorrect guesses (self.incorrects)
            
        Postconditions:
            *letter will be appended to the self.incorrects list        
        """
        self.incorrects.append(letter)
        return self.incorrects
    
    def drawIncorrects(self, win):
        """A method that draws the incorrect list (self.incorrects) to the window
        
        Parameters:
            win: the window 
            
        Preconditions:
            * win must be large enough for the anchor points of the incorrect wordbank to be valid. A 1000 x 700 win returns the objects in their desired locations
            
        Postconditions:
            *box for "wrong guesses" will be drawn to win containing the elements of self.incorrects
        """
        boxIC = Rectangle(Point(800, 650), Point(950, 500))
        boxIC.setFill("PaleVioletRed1")
        boxIC.draw(win)
        x = 0
        for i in self.incorrects[:3]:
            x = x + 150/4
            let = Text(Point(800 + x, 550), i)
            let.setTextColor("red")
            let.draw(win)
        x = 0
        for i in self.incorrects[3:]:
            x = x + 150/4
            let = Text(Point(800 + x, 600), i)
            let.setTextColor("red")
            let.draw(win)
            
    def DrawTitles(self, win):
        """A method that draws the titles "letters remaining" and "wrong letters" to win 

        Parameters:
            win: a window
            
        Preconditions:
            * win must be large enough for the anchor points of the title texts to be valid. A 1000 x 700 win returns the objects in their desired locations
            
        Postconditions:
            *a win with the titles drawn to it
        """
        txt1 = Text(Point(100, 480), "Letters Remaining")
        txt1.setSize(14)
        txt1.setFace("helvetica")
        txt1.draw(win)
        txt2 = Text(Point(840, 480), "Wrong Letters")
        txt2.setSize(14)
        txt2.setFace("helvetica")
        txt2.draw(win)
            
class word:
    """A class that creates an object of the word that the user interacts with to guess (the word that is seen as dashes in the beginning by the user, not the answer key)"""
    
    def __init__(self, key):
        """A constructor that takes the answer key in as a parameter"""
        self.word = ["__"] *len(key)
        
    def updateWord(self, letter, pos):
        """A method that updates the word when a letter is guessed correctly
        Parameters:
            letter: a string; in this case, the correctly guessed letter
            pos: an integer that indicates which index needs to be updated
            
        Postconditions:
            *self.word is updated to the index of pos == letter
            """
        self.word[pos] = letter
        
    def drawWord(self, win, key):
        """A method that draws the current state of the word being guessed on the screen
        Parameters:
            win: the window to be drawn on
            key: the answer key (a string) for the word to be compared to
            
        Postconditions:
            *elements of self.word is drawn to win
            *each element is 80 pixels apart unless the word is longer than six letters. If the word is longer than six letters, each element is drawn 50 piexels apart
        """
        x = 0
        if len(key) <= 6:
            for i in self.word:
                let = Text(Point(200 + x, 400), i)
                let.setSize(15)
                let.draw(win)
                x = x + 80
        else:
            for i in self.word:
                let = Text(Point(50 + x, 400), i)
                let.setSize(15)
                let.draw(win)
                x = x + 50
        
def main():
    """The main function that is called when the program is run."""
    
    # creates window for game 
    win = GraphWin("Hangman", 1000,700)
    ending_yet = "no"
    
    # while player wants to play
    while ending_yet == "no":
        
        word_list = []
    
    #defines word lists from files
    
        grade3 = open("grade3.txt", "r")
        listgrade3 = [line.rstrip("\n") for line in grade3]
        grade3.close()
        
        grade4 = open("grade4.txt", "r")
        listgrade4 = [line.rstrip("\n") for line in grade4]
        grade4.close()
        
        grade5 = open("grade5.txt", "r")
        listgrade5 = [line.rstrip("\n") for line in grade5]
        grade5.close()
        
        grade6 = open("grade6.txt", "r")
        listgrade6 = [line.rstrip("\n") for line in grade6]
        grade6.close()
        
    #draws the Homescreen and checks the user's click to determine where the screen should advance (playing screen vs. instructions) and which list the word should be drawn from
    
        HomeScreen(win, word_list, listgrade3, listgrade4, listgrade5, listgrade6)
        background = Rectangle(Point(0,700), Point(1000,0))
        background.setFill("yellow")
        background.draw(win)
        
    #chooses word and creates and draws necessary objects to win
    
        key = random.choice(word_list)
        wordguess = word(key)
        letters_remain = wordbank()
        letters_remain.drawIncorrects(win)
        letters_remain.drawWB(win)
        letters_remain.DrawTitles(win)
        wordguess.drawWord(win, key)
        man = Hangman()
        man.drawHang(win)
        wrong_count = -1
        i = 0
        game = "in progress"

        while game == "in progress":
            
    #checks a user's click to see if it is in the wordbank, then uses this guess to update and draw the wordbank 
    
            drawComments("Press a key to make a guess", win)
            guessed_letter = letters_remain.getKeyCheck(win)
            letters_remain.updateWB(guessed_letter)
            letters_remain.drawWB(win)
            state = "wrong"
            
    #indexes through the letters of the key word to see if the guessed letter is present. if it is, the word that is being displayed is updated to include this letter
    
            for pos in range(len(key)):
                letter = key[pos]
                if guessed_letter == letter:
                    state = "not wrong"
                    cover_rect = Rectangle(Point(0, 350), Point(800, 500))
                    cover_rect.setOutline("yellow")
                    cover_rect.draw(win)
                    wordguess.updateWord(letter, pos)
                    wordguess.drawWord(win, key)
                    i = i +1
                    
    #if the user has gussed all the letters correctly, the game is won
    
                if i == len(key):
                    game = "won"
                
    #if letter is not present, the wrong_count increases by one and the gussed letter is added to the incorrects box
    
            if state == "wrong":
                wrong_count = wrong_count + 1
                man.drawHangman(wrong_count, win)
                letters_remain.updateIncorrects(guessed_letter)
                letters_remain.drawIncorrects(win)
                
    #if the user guesses incorrectly five times, the game is lost
    
                if wrong_count == 5:
                    game = "lost"
                
    #draws end screen         
        if game == "won":
            drawComments("Congrats! You've won. Press any key", win)
            z = win.getKey()
            DrawEndScreen(win)
            homeclick = win.getMouse()
            if CheckEndScreen(homeclick) == "yes, play again":
                ending_yet = "no"
            elif CheckEndScreen(homeclick) == "no, quit":
                ending_yet = "yes"
                win.close()
        
        if game == "lost":
            drawComments("Sorry! You've lost. Press any key", win)
            x = win.getKey()
            com = "Answer: " + key + ". Press any key"
            drawComments(com, win)
            z = win.getKey()
            DrawEndScreen(win)
            homeclick = win.getMouse()
            if CheckEndScreen(homeclick) == "yes, play again":
                ending_yet = "no"
            elif CheckEndScreen(homeclick) == "no, quit":
                ending_yet = "yes"
                win.close()
                
if __name__ == "__main__":
    main() 