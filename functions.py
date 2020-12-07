import pandas as pd
from tqdm import tqdm
import arxiv

def arxiv_search(search_terms, cutoff_date="2010-01-01"):
    results = []
    for term in tqdm(search_terms):
        search = arxiv.query(query=term,
                max_results=10000,
                start=0,
                sort_by="relevance",
                sort_order="descending",
                prune=True,
                iterative=False,
                max_chunk_results=1000)

        results.append(search)
    results = [item for sublist in results for item in sublist]
    results = pd.DataFrame(results)

    # Drop all rows not in timeframe
    #results = results[results["published"]# > cutoff_date]
    print("Number of ArXiv Results: " + str(len(results)))

    # Deduplicate
    results = results.drop_duplicates(subset=["id"])
    print("Number of ArXiv Results after removing duplicates: " + str(len(results)))

    return results