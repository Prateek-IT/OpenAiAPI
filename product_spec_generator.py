import os
import openai
import json
from dotenv import load_dotenv
load_dotenv()

openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("OPENAPI_KEY")


class Product:
    def __init__(self,product_type,product_description) :
        self.product_description = product_description
        self.product_type =product_type

    def generate_keywords(self, product_type):
        prompt = f"""Generate keywords for the properties of a product:\n{product_type}\n\nSome sample keywords are product type, weight, cost, dimensions, color whereas other keywords may vary depending on what the product is."""
        
        response = openai.Completion.create(

            engine="GPT3-5",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        
        
        return response.choices[0].text.strip()
        



    def generate_specifications_values(self,product_description,specifications_keywords):

        prompt = f"""use the keywords:\n{specifications_keywords}\n generated to create only a single and final dictionary 
        for keywords and values where values can be found in the description:\n{product_description}."""

        response = openai.Completion.create(
            engine="GPT3-5",
            prompt=prompt,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )

        return response.choices[0].text.strip()




if __name__ == "__main__":

    product_type = input("Enter Product Type: ")
    product_description = input("Enter description of Product: ")

    product_specfications = Product(product_type,product_description)

    specifications_keywords = product_specfications.generate_keywords(product_type)
    # print(specifications_keywords)
    
    product_specs = product_specfications.generate_specifications_values(specifications_keywords,product_description)
    
    
    # spec= json.loads(product_specs)
    # print(spec)
    print(product_specs)   