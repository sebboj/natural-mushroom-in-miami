from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI
import os

#api key for huggingface
os.environ["OPENAI_API_KEY"] = "<insert your openai api key here>"

template = """Question: {question}
Answer: """

prompt = PromptTemplate(template=template, input_variables=["question"])

davinci = OpenAI(model_name="text-davinci-003")

#davinci openai
llm_chain = LLMChain(prompt=prompt, llm=davinci)

def ask_gpt(q):
    return llm_chain.run(q)
