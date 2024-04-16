# Large Language Models (LLMs)

## 1. How to utilize a model via API
Application Programming Interface (API) is a way to interact with a remote application programmatically. Instead of going to any website and typing the prompt we can do this via API. so in python we type the prompt and with this API we can send requests and receive a response from the model.<br>
Using API we can customize the system messages, we can adjust the input parameters like max response length, no of responses and temperature, process images and other files, extract helpful word embeddings for downstream tasks, input audio for transcription and translation, model fine-tuning functionality.<br>
**Code :-** **`1. Using_Gemini_API.ipynb`**

## 2. How to use Open Source Models from Hugging Face
There are thousands of open source pre-trained ML models available for free. The datasets repository which are also available for free to train our own models or for fine-tuning. Hugging Face Spaces is a platform to build and deploy ML models.<br>
Transformers is a python library which makes downloading and training ML models super easy. Initially it was only for NLP; now it can be used for any domain. We can use its pipeline function to perform many tasks.<br>
On Hugging Face there are several models we can specify which task we want to accomplish, which dataset we need, and for commercial use cases we can also select the license. We can use Gradio library to build a UI for our application and instead of hosting it locally we can host it on HF Spaces which is a git repos hosted by Hugging Face that allows us to make ML applications.<br>

### 2.1. Natural Language Processing
NLP is a field of linguistics and ML, and it is focused on everything related to human language. The significant improvement in this field is due to the transformer architecture, from a well known paper "Attention Is All You Need" paper in 2017.<br>
And since then this architecture is the core of many state-of-art ML models nowadays. 
We will try to create our own chatbot and for this we will use Facebook's blenderbot model as it is very small and only needs 1.6GB to load it. We can’t use LLAMA2 or any other model since we won’t be able to load it as it exceeds 4GB. HF also provides a leaderboard where we can compare models.<br>
**Code :-** **`2.1. Intro_to_NLP.ipynb`**

### 2.2. Embeddings
Here we will try to measure sentence similarity, it measures how close two pieces of text are. For example ‘I like kittens’ and ‘We love cats’ have similar meanings. Sentence similarity is particularly used for information retrieval and clustering or grouping. The sentence similarity models convert input text into vectors or so-called embeddings. These embeddings capture semantic information.<br>
**Code :-** **`2.2. Embeddings.ipynb`**

### 2.3. Zero-Shot Audio Classification
Zero-Shot is an alternate method to avoid fine-tuning. Here we will use the Hugging Face model to solve Audio Classification problem.<br>
**Code :-** **`2.3. Zero_Shot_Audio_Classification.ipynb`**

