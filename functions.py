import pandas as pd
from tqdm import tqdm
import arxiv
import elsapy
from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json

def arxiv_search(search_terms, max_results=10000):
    results = []
    for term in tqdm(search_terms):
        search = arxiv.Search(query=term,
                max_results=max_results,
                )

        results.append(search)
    results = [item for sublist in results for item in sublist.results()]

    _results = []
    for res in results:
        _results.append({"id": res.entry_id, "title": res.title, "abstract": res.summary, "pubdate": res.published, "pdf_url": res.pdf_url})
    results = pd.DataFrame(_results)

    # Drop all rows not in timeframe
    #results = results[results["published"]# > cutoff_date]
    print("Number of ArXiv Results: " + str(len(results)))

    # Deduplicate
    results = results.drop_duplicates(subset=["id"])
    print("Number of ArXiv Results after removing duplicates: " + str(len(results)))

    return results


## TODO: UNUSED CURRENTLY ##
def elsevier_search(search_terms, api_key, cutoff_date="2010-01-01"):
    client = ElsClient(api_key)

    results = []
    for term in search_terms:
        search = ElsSearch(term, "sciencedirect")
        search.execute(client, get_all=True)
        results.append(search)


    return results

def wiley_search(search_terms, api_key, cutoff_date="2010-01-01"):

    results = []
    return results

