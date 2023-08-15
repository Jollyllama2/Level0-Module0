from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    question = simpledialog.askstring(title="sup",prompt='can turtles draw?')
    #      // 3.  Use an if statement to check if their answer is correct
    if question == "yes":
        score=score+1
        messagebox.showinfo(title='sup',message="well duh")
    else:
        score=0
        messagebox.showinfo(title="i",message="COME ON, OF COURSE THEY CAN")
    #      // 4.  if the user's answer was correct, add one to their score 
    question = simpledialog.askstring(title='sup',prompt='can pigs fly?')
    if question == "no":
        score=score+1
        messagebox.showinfo(title="hi",message='THANK YOU FOR GETTING THIS ONE RIGHT, THANK YOU!')
    else:
        score=score
        messagebox.showinfo(title="hi",message="HOW ON EARTH DID YOU GET THAT ANSWER LIKE IT'S A METAPHOR FOR SOME THING THAT WILL NEVER HAPPEN ")

        question = simpledialog.askstring(title='yo',prompt='can dogs talk?')
    if question == "no":
        score=score+1
        messagebox.showinfo(title='yo',prompt="good job")
    else:
        score=score
        messagebox.showinfo(title='hi',prompt='COME ON')
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
