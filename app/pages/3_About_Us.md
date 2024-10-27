## Project Scope

The scope of this project is to make use of LLM to let users "talk" to policies from the [Ministry of Sustainability and the Environment](https://www.mse.gov.sg/) (MSE) and find out facts about the policies. This project focuses on the following policies:

- Climate Change
- Energy
- Clean Air
- Water
- Food Security

## Objectives

- Create "Policies AMA" (Ask Me Anything) page that allows users to ask questions based on the policy they chose.
- Create "Sustainability Facts" page that list down 3 random facts derived from content of MSE policies.

## Data Sources

Data for policies are retrieved from the MSE website:

- [Climate Change](https://www.mse.gov.sg/policies/climate-change)
- [Energy](https://www.mse.gov.sg/policies/energy)
- [Clean Air](https://www.mse.gov.sg/policies/clean-air)
- [Water](https://www.mse.gov.sg/policies/water)
- [Food Security](https://www.mse.gov.sg/policies/food/)

## Features

- Logic to retrieve MSE policies from MSE website pages.
- Utilised OpenAI API (via LangChain) for embeddings calculation and content generation based on polices and user queries.
- Utilised Retrieval Augmented Generation (RAG) techniques to improve accuracy of content shown to user.
- Use vector store (Chroma) to store embeddings of downloaded MSE content, and for retrieval of content by similarity search.
- Utilised LangChain RetrievalQA functionalities to simplify process of documents retrieval based on user queries.
- Utilised Streamlit to built frontend features such as chat UI.