import arxiv
import ollama

client = arxiv.Client()

search = arxiv.Search(
    query="plasma", max_results=5, sort_by=arxiv.SortCriterion.SubmittedDate
)

results = client.results(search)

summary = ""
for r in results:
    summary += f"Title: {r.title}\n\nSummary: {r.summary}\n\n=======\n"


print(summary)

response = ollama.chat(
    model="llama3.1",
    messages=[
        {
            "role": "system",
            "content": f"You are given a list of titles along with abstracts for research papers. Answer user questions about them. \n\n {summary}",
        },
        {"role": "user", "content": "What are some new ideas about plasma turbulence?"},
    ],
)

print(response["message"]["content"])
