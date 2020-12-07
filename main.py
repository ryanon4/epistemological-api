from functions import arxiv_search

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
data = arxiv_search(search_terms)
data.to_csv("abstracts.csv")






