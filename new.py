import openai

import os

import dotenv 
from dotenv import load_dotenv
load_dotenv()

openai.api_type = "azure"

openai.api_version = "2023-05-15"




openai.api_key = os.getenv("OPENAPI_KEY")

openai.api_base = os.getenv("OPENAI_API_BASE")




class ProductKeyGenerator:

    

    def generate_product_keys(self, product_type):

      
        prompt = f'''Please generate a list of keywords that describe the specifications of the {product_type} based on the provided input.'''
  


        response = openai.Completion.create(

            engine="GPT3-5",  

            prompt=prompt,

            max_tokens=100,

            stop=None,

            temperature=0.0,

            top_p=1.0,

            frequency_penalty=0.0,

            presence_penalty=0.0

        )


        print(response.choices[0].text.strip())
        return response.choices[0].text.strip()
        



    def generate_filled_description(self, product_description, generated_keys):

        # Combine the product description and generated keys in a prompt

        prompt = f'''Please analyze the provided {product_description} and extract specific values for the given specification keywords {generated_keys}. The specification keywords are essential aspects of the {product_type}, and the values should correspond to the information present in the {product_description}. Ensure the extracted values are accurate and relevant to the product's capabilities.
'''




        response = openai.Completion.create(

            engine="GPT3-5",  

            prompt=prompt,

            max_tokens=200,

            stop=None,

            temperature=0.0,

            top_p=1.0,

            frequency_penalty=0.0,

            presence_penalty=0.0

        )




        filled_description = response.choices[0].text.strip()

        return filled_description




product_key_generator = ProductKeyGenerator()




# User enters the product_type

product_type = input("Enter the product type: ")




# Generate the possible keys for the product

possible_keys = product_key_generator.generate_product_keys(product_type)

# print("Generated Keys:")

# print(possible_keys)




# User enters the product description

product_description = input("Enter the product description: ")




# Generate and print the filled description using the generated keys

filled_description = product_key_generator.generate_filled_description(product_description, possible_keys)

print("\nFilled Description:")

print(filled_description)


