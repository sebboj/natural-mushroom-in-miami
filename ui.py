from app import ask_gpt
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import math

RED = "#F03711"

# Create a Tkinter window
root = tk.Tk()
root.title("EZGRADER.AI")
root.configure(bg = RED)

image = Image.open("C:/Users/sebby/Downloads/ezg_smol.png")
logo = ImageTk.PhotoImage(image)
dalogo = tk.Label(image=logo)
dalogo.image = logo
dalogo.place(relx=0, rely=0)

# Create a label and a text input field for the essay
essay_label = tk.Label(root, text="", bg = RED)
essay_label.pack(pady=33)
essay_text = tk.Text(root, width=200, height=30)
essay_text.pack(pady=5)
essay_text.insert("1.0", "Insert Essay here")  # Set default text

# Remove default text when clicked
def remove_text(event):
    if essay_text.get("1.0", "end-1c") == "Insert Essay here":
        essay_text.delete("1.0", "end")

essay_text.bind("<Button-1>", remove_text)

# Create a set of buttons to select the type of essay
essay_type_label = tk.Label(root, text="Essay Type:", bg = RED)
essay_type_label.pack(pady=5)
essay_type = tk.StringVar()
essay_type.set("Argumentative")  # Set default value
essay_type_label.place(relx=0, rely=0.87, relheight=0.06, relwidth=0.22)
argumentative_button = tk.Radiobutton(root, text="Argumentative", variable=essay_type, value="Argumentative", bg = RED)
informative_button = tk.Radiobutton(root, text="Informative", variable=essay_type, value="Informative", bg = RED)
persuasive_button = tk.Radiobutton(root, text="Persuasive", variable=essay_type, value="Persuasive", bg = RED)
argumentative_button.pack(side=tk.LEFT, padx=10)
informative_button.pack(side=tk.LEFT, padx=10)
persuasive_button.pack(side=tk.LEFT, padx=10)

# Create a word counter label
word_counter_label = tk.Label(root, text="Words: 0", bg = RED)
word_counter_label.pack(pady=10)


# Create a reading level dropdown menu
reading_level_label = tk.Label(root, text="Reading Level:", bg = RED)
reading_level_label.pack(pady=5)
reading_level_label.place(relx=0.22, rely=0.87, relheight=0.06, relwidth=0.22)
reading_level = tk.StringVar()
reading_level.set("K")  # Set default value
reading_level_menu = tk.OptionMenu(root, reading_level, "K", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "College")
reading_level_menu.pack(side=tk.LEFT, padx=10)
reading_level_menu.place(relx=0.22, rely=0.935, relheight=0.06, relwidth=0.22)
reading_level_menu.configure(bg = RED)

def get_letter_grade(total_score):
    letter_grade = ""
    # Determine the final letter grade
    if total_score >= 95:
        letter_grade += "A+"
    elif total_score >= 92:
        letter_grade += "A"
    elif total_score >= 90:
        letter_grade += "A-"
    elif total_score >= 85:
        letter_grade += "B+"
    elif total_score >= 82:
        letter_grade += "B"
    elif total_score >= 80:
        letter_grade += "B-"
    elif total_score >= 75:
        letter_grade += "C+"
    elif total_score >= 72:
        letter_grade += "C"
    elif total_score >= 70:
        letter_grade += "C-"
    elif total_score >= 65:
        letter_grade += "D+"
    elif total_score >= 60:
        letter_grade += "D"
    else:
        letter_grade += "F"
    return letter_grade

def gen_feedback(focus_score, ideas_score, structure_score, tone_score, grammar_score, vocabulary_score):
# Generate feedback based on the rubric scores
    feedback = "Focus, Purpose, Thesis (Controlling Idea):\n"
    if focus_score == 20:
        feedback += "Masterful - Engaging and full development of a clear thesis as appropriate to assignment purpose.\n"
    elif focus_score >= 15:
        feedback += "Skilled - Competent and well-developed thesis; thesis represents sound and adequate understanding of the assigned topic.\n"
    elif focus_score >= 10:
        feedback += "Able - Mostly intelligible ideas; thesis is weak, unclear, too broad, or only indirectly supported.\n"
    elif focus_score >= 5:
        feedback += "Developing - Mostly simplistic and unfocused ideas; little or no sense of purpose or control of thesis.\n"
    else:
        feedback += "Novice - Ideas are extremely simplistic, showing signs of confusion, misunderstanding of the prompt; thesis is essentially missing or not discernable.\n"

    feedback += "\nIdeas, Support & Development (Evidence):\n"
    if ideas_score == 20:
        feedback += "Masterful - Shows consistent evidence with originality and depth of ideas; ideas work together as a unified whole; main points are sufficiently supported (with evidence); support is valid and specific.\n"
    elif ideas_score >= 15:
        feedback += "Skilled - Shows ideas supported sufficiently; support is sound, valid, and logical.\n"
    elif ideas_score >= 10:
        feedback += "Able - Shows main points and ideas are only indirectly supported; support isn’t sufficient or specific, but is loosely relevant to main points.\n"
    elif ideas_score >= 5:
        feedback += "Developing - Shows insufficient, nonspecific, and/or irrelevant support.\n"
    else:
        feedback += "Novice - Shows lack of support for main points; frequent and illogical generalizations without support.\n"

    feedback += "\nStructure and Organization:\n"
    if structure_score == 15:
        feedback += "Masterful - Shows organization is sequential and appropriate to assignment; paragraphs are well developed and appropriately divided; ideas linked with smooth and effective transitions.\n"
    elif structure_score >= 11:
        feedback += "Skilled - Shows competent organization, without sophistication. Competent paragraph structure; lacking in effective transitions.\n"
    elif structure_score >= 7:
        feedback += "Able - Shows limited attempts to organize around a thesis; paragraphs are mostly stand-alones with weak or nonevident transitions.\n"
    elif structure_score >= 3:
        feedback += "Developing - Shows organization, while attempted, was unsuccessful. Paragraphs were simple.\n"
    else:
        feedback += "Novice - Shows lack of structure and organization.\n"


    feedback += "\nTone and Audience:\n"
    if structure_score == 15:
        feedback += "Masterful - Shows clear discernment of distinctive audience; tone and point-of-view appropriate to the assignment.\n"
    elif structure_score >= 11:
        feedback += "Skilled - Shows effective and accurate awareness of general audience; tone and point-of-view satisfactory.\n"
    elif structure_score >= 7:
        feedback += "Able - Shows little or inconsistent sense of audience related to assignment purpose; tone and point-of-view not refined or consistent.\n"
    elif structure_score >= 3:
        feedback += "Developing - Shows almost no awareness of a particular audience; reveals no grasp of appropriate tone and/or point-of-view for given assignment.\n"
    else:
        feedback += "Novice - Shows a lack of awareness of a particular appropriate audience for assignment; tone and point-of-view are somewhat inappropriate or very inconsistent.\n"


    feedback += "\nGrammar:\n"
    if structure_score == 15:
        feedback += "Masterful - Shows each sentence structured effectively, powerfully; rich, well-chosen variety of sentence styles and length.\n"
    elif structure_score >= 11:
        feedback += "Skilled - Shows effective and varied sentences; errors (if any) due to lack of careful proofreading; syntax errors (if any) reflect uses as colloquialisms.\n"
    elif structure_score >= 7:
        feedback += "Able - Shows formulaic or tedious sentence patterns; shows some errors in sentence construction; some non-standard syntax usage.\n"
    elif structure_score >= 3:
        feedback += "Developing - Sentences show errors of structure; little or no variety; no grasp of sentence flow.\n"
    else:
        feedback += "Novice - Shows simple sentences used excessively, almost exclusively; frequent errors of sentence structure.\n"


    feedback += "\nVocabulary:\n"
    if structure_score == 15:
        feedback += "Masterful - Shows exceptional vocabulary range, accuracy, and correct and effective word usage.\n"
    elif structure_score >= 11:
        feedback += "Skilled - Shows good vocabulary range and accuracy of usage.\n"
    elif structure_score >= 7:
        feedback += "Able - Shows ordinary vocabulary range, mostly accurate; some vernacular terms.\n"
    elif structure_score >= 3:
        feedback += "Developing - Shows errors of diction, and usage, while evident, do not interfere with readability.\n"
    else:
        feedback += "Novice - Shows extremely limited vocabulary; choices lack grasp of diction; usage is inaccurate.\n"

    return feedback


# Create a button to grade the essay
def grade_essay():
    glevel = reading_level.get()
    essay = essay_text.get("1.0", "end-1c")
    essay_type_value = essay_type.get()

    # update word count
    wcount = str(len(essay.split()))
    word_counter_label.config(text="Words: " + wcount)

    # Show message box with "Grading Essay..." while grading
    messagebox.showinfo("Grading Essay", "Grading Essay...")

    # perform grading logic here
    focus_p = int(math.floor(float(ask_gpt("grade the focus and thesis of this essay from 0 to 20, only output the number grade. here is the essay: " + essay))))
    #out of 20

    ideas_p = int(math.floor(float(ask_gpt("grade the strength of the ideas, support, and development of this essay on a scale from 0 to 20, only output the number grade. here is the essay: " + essay))))
    #out of 20

    structure_p = int(math.floor(float(ask_gpt("grade the structure and organization of this essay on a scale from 0 to 15, only output the number grade. here is the essay: " + essay))))
    #out of 15

    tone_p = int(math.floor(float(ask_gpt("grade the tone and point of view of this essay on a scale from 0 to 15, only output the number grade. here is the essay: " + essay))))
    #out of 15

    grammar_p = int(math.floor(float(ask_gpt("grade the quality of grammar of this essay based off a reading level of " + glevel + "on a scale from 0 to 15, only output the number grade. here is the essay: " + essay))))
    #out of 15

    vocabulary_p = int(math.floor(float(ask_gpt("grade the level of vocabulary of this essay based off a reading level of " + glevel + "and give the grade on a scale from 0 to 15, only output the number grade. here is the essay: " + essay))))
    #out of 15

    # Calculate the total score
    tot = focus_p + ideas_p + structure_p + tone_p + grammar_p + vocabulary_p
    letter_g = get_letter_grade(tot)

    if(int(wcount) < 33):
        focus_p = 0
        ideas_p = 0
        structure_p = 0
        tone_p = 0
        grammar_p = 0
        vocabulary_p = 0
        letter_g = "F"

    # Show message box with result
    result = "Essay type: {}\nGrade: {}\n".format(essay_type_value, letter_g)
    fb = gen_feedback(focus_p, ideas_p, structure_p, tone_p, grammar_p, vocabulary_p)
    messagebox.showinfo("Essay Graded", result+fb)

grade_button = tk.Button(root, bg = "#FFFB8E", text="Grade", command=grade_essay)
grade_button.pack(pady=10)
grade_button.place(relx=0.78, rely=0.935, relheight=0.06, relwidth=0.22)


# Run the Tkinter event loop
root.mainloop()

