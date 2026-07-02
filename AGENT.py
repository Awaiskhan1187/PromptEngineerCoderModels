from openai import OpenAI
import dotenv
import os


dotenv.load_dotenv("/home/dev/c++/data science lab/data science lab/planning_trip_to_paris/.env")
Input_history_Bot1 = [
    {"role": "system", "content": "you are a programmer working on coding tasks, you should only write the perfect prompt for the task, you should not write any code"},
    {"role": "user", "content": "write a fabonachi function in c++"},
    {"role": "assistant", "content": "write a perfect fabonachi function in C++, the function should take an integer n as input and return the nth number in the fibonachi series, use the most optimal aproach"}
]

Input_history_Bot2 = [
    {"role": "system", "content": """you are a programmer working on coding tasks, Write clean, simple, and optimal code. 
     you should stricktly follow the instructions. Avoid unnecessary complexity unless asked.
      also donot explain the code, keep the code simply and easy to understand"""},
    {"role": "user", "content": "write a fibonacci function in c++.avoid sign and unsign if user did not specif"},
    {"role": "assistant", "content": """
    int fibonacci(int n) {
     if(n <= 1)
      return n;
     int a = 0, b = 1 , c;
     for (int i = 2; i <= n; i++){
     c = a + b;
     a = b;
     b = c;
     }
     return c;
     }
"""}
]
API_KEY = os.getenv("GROQ_API") #get the API key 
client = OpenAI(api_key = API_KEY, base_url = "https://api.groq.com/openai/v1")


API_KEY2 = os.getenv("GROQ_API2") #get the API key for model 2
client2 = OpenAI(api_key = API_KEY2, base_url = "https://api.groq.com/openai/v1")


def model1(prompt): #first model that work as a prompt generator
    model1_prompt = {"role": "user", "content":prompt}
    Input_history_Bot1.append(model1_prompt)
    
    response = client.chat.completions.create(
        model = "openai/gpt-oss-20b",
        messages = Input_history_Bot1)
    response = response.choices[0].message.content
    Input_history_Bot1.append({"role": "assistant", "content": response})
    return response

def model2(prompt): #second model that work as a c++ programmer

    model2_prompt = {"role": "user", "content": prompt}
    Input_history_Bot2.append(model2_prompt)
    response = client2.chat.completions.create(
        model =  "openai/gpt-oss-20b",
        messages = Input_history_Bot2
    )
    response = response.choices[0].message.content
    Input_history_Bot2.append({"role": "assistant","content": response}) 
    return response

def pipeline(prompt): 
    response1 = model1(prompt)
    print("Prompt pass to model: ", response1)
    response2 = model2(response1)
    return response2

def main():
    while True:
        prompt= input("enter Prompt here: ")
        if prompt.lower() == "exit" or prompt.lower() == "quit":
            break
        finaloutput = pipeline(prompt)
        print("Code : \n",finaloutput)

if __name__ == "__main__":
    main()


    