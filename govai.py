import openai
import os

# Set up your API key: Make sure to set it as an environment variable OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_legislation(document_text):
    """
    Takes a legislative document text as input and returns a summary.
    :param document_text: Full text of a legislative document
    :return: Summary of the document
    """
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Assuming GPT-4 is what we're using
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes legislative documents."},
                {"role": "user", "content": f"Summarize this legislative document:\n\n{document_text}"}
            ]
        )
        
        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    document_example = """
    This is a placeholder for a legislative document text. 
    It should include multiple points, references, and specific legal language that requires summarization.
    """
    
    summary = summarize_legislation(document_example)
    if summary:
        print("Summary of the legislative text:")
        print(summary)
