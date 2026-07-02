IN this task i have use two GROQ APIs stored in .env
two models used : openai/gpt-oss-20b
First model machanism
ask the user to enter the prompt:
the first model generate a perfect prompt for model 2,
so this model work as prompt generator/engineer
second model write cpp code for the given prompt so it work as coder
inside the pipeline function i have pass the output of first model or api request to the second model through openai()

and finaly print the output of the second model in main function.
further it store the history of both models.
