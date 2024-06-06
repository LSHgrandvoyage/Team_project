from abc import ABCMeta, abstractmethod

from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain_core.language_models.llms import LLM
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from pydantic_core import Url


class BaseLLMModel(BaseModel, metaclass=ABCMeta):
    name: str = Field(description='LLM name')
    api_key: str = "sk-proj-uj3I1vE7ZrLXzEALrqNWT3BlbkFJUmM9fvC3VhtON4Y3ySRB"
    @abstractmethod
    def build(self) -> LLM:
        return ChatOpenAI(openai_api_key=self.api_key)

    def __hash__(self) -> int:
        return hash(self.name)


class ChatGPTModel(BaseLLMModel):
    model: str = 'gpt-4o'
    temperature: float = 0.7

    def build(self) -> LLM:
        return ChatOpenAI(
            model_name=self.model,  # type: ignore
            temperature=self.temperature,
            openai_api_key=self.api_key
        )  # type: ignore


class HuggingFaceEndpointModel(BaseLLMModel):
    endpoint_url: Url = Url('http://huggingface-tgi/')
    temperature: float = 0.8

    def build(self) -> LLM:
        return HuggingFaceEndpoint(
            endpoint_url=str(self.endpoint_url),
            temperature=0.01,
            # max_new_tokens=512,
            # top_k=10,
            # top_p=0.95,
            # typical_p=0.95,
            # repetition_penalty=1.03,
        )  # type: ignore
