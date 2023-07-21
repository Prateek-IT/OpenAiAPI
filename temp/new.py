import openai
import os


openai.api_type = "azure"
openai.api_version = "2023-05-15" 
openai.api_base = "https://ai-training0.openai.azure.com/" # Your Azure OpenAI resource's endpoint value.
openai.api_key = "ad32fb199aab424f8ccc264b8ac08bec"
class specifications:

   def get_product_specs(category):
    prompt = f"List 10 specs of a product in the {category} category:"
    response = openai.Completion.create(
            engine="GPT3-5",
            prompt=prompt,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
    )

    return response.choices[0].text.strip()

   def get_product_values(specs , description):
    prompt = f'''use the keywords generated in {specs} to create a dictionary keywords and values where values can be found in the description:\n{description}\n\nIf there are no values for the specification of the product show null against the specification.'''
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


def main():
    category = input("Enter the product category: ")
    specs = specifications()
    specs = specifications.get_product_specs(category)
    print("keywords :" , specs)
    description = input("Enter product details : ")
    output = specifications.get_product_values(specs , description)
    print(output)
if __name__ == "__main__":
    main()

