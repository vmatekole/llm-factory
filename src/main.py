from injector import Injector, singleton
from llm_maker.base_llm import Configuration, LLMService
from llm_maker.llms import LLMFactory

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


MODEL_PATH: str = '/Users/PI/Library/Application Support/nomic.ai/GPT4All/llama-2-7b-chat.ggmlv3.q4_0.bin'


def configure_llm(binder):
    config = Configuration(
        provider='GPT4All', temperature=0, model_filepath=MODEL_PATH, verbose=True
    )
    binder.bind(Configuration, to=config, scope=singleton)


if __name__ == '__main__':
    injector: Injector = Injector([configure_llm, LLMFactory()])
    service: LLMService = injector.get(LLMService)
    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate(template=template, input_variables=['question'])

    llm_chain: LLMChain = LLMChain(prompt=prompt, llm=service.model.provider)

    question = 'What happens when it rains somewhere?'
    response = llm_chain.run(question)
