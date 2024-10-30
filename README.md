# natural-mushroom-in-miami
**EZGrader.AI**  
Our project for the Kaseya Miami AI Hackathon that won 2nd place.  

With this new tool, teachers no longer have to spend hours grading papers manulally. Instead, this interactive essay grader can grade essays quickly and accurately. Teachers can set their own grading criteria and preferences such as the reading level (K through College) and essay type (argumentative, informative, or persuasive). We chose the davinci LLM model which allows for multilingual processing so that teachers all around the world are able to use this tool.  

Once the essay is inputed into the text box and the grade button is pressed, the word count is calculated and the model goes to work in a matter of seconds. The essay is given a letter grade and feedback is provided based on the given rubric. Detailed feedback is provided on the thesis, idea development, essay structure, tone, grammar, and even vocabulary.   

It is difficult to fool the model. Essays that are too short or contain many errors will receive a low grade. A one word essay, for example: "Howdy", is quickly given an F.

The call to the LLM model can be found in the ```app.py``` file and the grading logic is found in the ```ui.py``` file.
