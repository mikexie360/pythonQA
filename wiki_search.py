import wikipedia
import re

def search_topic(topic):
    try:
        # Search for the topic on Wikipedia
        search_results = wikipedia.search(topic)

        if not search_results:
            print("No results found for the given topic.")
            return

        # Get the summary of the first search result
        page = wikipedia.page(search_results[0])
        summary = page.summary

        print("Topic: ", page.title)
        print("Summary: ", summary)
        print("Source: ", page.url)

        # Ask and answer questions related to the topic
        while True:
            question = input("Ask a question (or type 'exit' to quit): ")
            if question.lower() == "exit":
                break

            # Remove question marks and extra spaces
            question = re.sub(r'\?$', '', question.strip())

            try:
                answer = wikipedia.summary(question, sentences=2)
                print("Answer: ", answer)
            except wikipedia.exceptions.PageError:
                print("Question not found in the given topic.")
            except wikipedia.exceptions.DisambiguationError as e:
                print("Question is ambiguous. Did you mean one of the following?")
                options = e.options[:5]  # Display up to 5 options
                print(options)

    except wikipedia.exceptions.HTTPTimeoutError:
        print("Error: Connection to Wikipedia API timed out. Please try again later.")
    except wikipedia.exceptions.WikipediaException:
        print("An error occurred while fetching data from Wikipedia.")

if __name__ == "__main__":
    topic = input("Enter a topic to search: ")
    search_topic(topic)
