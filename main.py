from functions import arxiv_search, elsevier_search


### API KEYS ###
els_key = ""

### Enter your search terms here, list can be as long as you like ###
search_terms = ['computer supported learning',
'computer-supported learning',
'intelligent tutoring system',
'intelligent teaching system',
'artificial tutoring system',
'adaptive teaching',
'educational technology',
'elearning',
'e-learning',
'pedagogical agent',
'educational data mining',
'learning analytics',
'automatic essay evaluation',
'automatic essay scoring',
'adaptive educational hypermedia',
'adaptive learning spaces',
'learning management system',
'educational content management']

# All results are saved to abstracts.csv #
data = arxiv_search(search_terms, max_results=10)
data.to_csv("arxiv_output.tsv", sep="\t")
#elsevier_data = elsevier_search(search_terms, api_key=els_key)
#elsevier_data.to_csv("elsevier_results.csv")








