
import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage

# Make sure your API key is set in the environment
groq_api_key = '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'

#  Initialize the ChatOpenAI model
chat = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="mixtral-8x7b-32768"  # You can change this to other available models
)

# Get user input from the terminal
user_input = input("Enter your message for the AI: ")

# Create a message with the user's input
message = HumanMessage(content=user_input)

# Generate a response
response = chat.invoke([message])

# Print the response
print("\nAI Response:")
print(response.content)

from langchain.llms import openAI
llm = openAI(temperature = 0.6)
name = llm("I want to open  restaurant for indian food.suggest a fency name for this.")
print(name)
 
from langchain.prompts import PromptTemplate
Prompt_template_name = PromptTemplate(
    input_variables=['cuisine'],
    template= "I want to open  restaurant for {cuisine}food.suggest a fency name for this."
)
Prompt_template_name.format(cuisine="Indian")

from langchain.chains import LLMchain
chain = LLMchain(llm = llm ,prompt = Prompt_template_name)
chain.run("Indian")

llm = openAI(temperature = 0.6)
Prompt_template_name = PromptTemplate(
    input_variables =['cuisine'],
    template= "I want to open  restaurant for {cuisine}food.suggest a fency name for this."
)
name_chain = LLMchain(llm = llm ,prompt = Prompt_template_name)
Prompt_template_name = PromptTemplate(
    input_variables=['restaurant_name'],
    template= """suggest some menu item for {restaurant_name}.Return it as a comma separated list"""
)

food_items_chain = LLMchain(llm = llm ,prompt = Prompt_template_name)
 
from langchain.chains import simpleSequentialChain
chain = simpleSequentialChain(chain = [name_chain,food_items_chain])
response = chain.run("Indian")
print(response)


llm = openAI(temperature = 0.7)
Prompt_template_name = PromptTemplate(
    input_variables =['cuisine'],
    template= "I want to open  restaurant for {cuisine}food.suggest a fency name for this."
)
name_chain = LLMchain(llm = llm ,prompt = Prompt_template_name,output_key = "restaurant_name")

llm = openAI(temperature = 0.7)
Prompt_template_name = PromptTemplate(
    input_variables=['restaurant_name'],
    template= "suggest some menu item for {restaurant_name}."
)
food_items_chain = LLMchain(llm = llm, prompt=Prompt_template_items, output_key ="menu_items")

from langchain.chains import sequentialchain

chain = sequentialchain(
    chain = [name_chain, food_items_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name','menu_items']
)
chain({'cuisine':'Indian'})





#pycham
#import streamlit as st
#import langchain_helper
# pip install streamlit
st.title("Restaurant Name generator")
cuisine = st.sidebar.selectbox("pick a cuisine",("Indian","Italian","Mexcian"))

def generate_restaurant_name_and_items(cuisine):
    return{
        'restaurant_name':'curry delight',
        'menu_item':'samosa,paneer tikka'
    } 
if cuisine:
    response = langchain_helper. generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu_item**")

    for item in menu_item:
        st.write("-",item)





# New File Lang chain helper
def generate_restaurant_name_and_items(cuisine):
    return{
        'restaurant_name':'curry delight',
        'menu_item':'samosa,paneer tikka'
    }



# Agent 
# google search
# langchain agent load tools
# integrations
from langchain.agents import AgentType,initialize_agent,load_tools
from langchain.llms import openai

tools = load_tools(["wikipedia","llm-math"],llm = llm)
agent = initialize_agent(
    tools,
    llm,
    agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION
    verbose = True 
)
agent.run("when was Elon musk born? what is his age right now in 2024?")


# serpApi

from secret_key import serpapi_key
os.environ['SERPAPI_API_KEY'] = serpapi_key

llm = openAI(temperature = 0)
tools = load_tools(["serpapi","llm-math"],llm = llm)
agent = initialize_agent(tools,llm,agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION
    verbose = True )
agent.run("what was the GDP of us in 2022 plus 5?")

# memory attached

from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory()
chain = LLMchain(llm = llm,Prompt_template_name,memory = memory)
name = chain.run("Mexican")
print (name)

name = chain.run("Indian")
print (name)

 



