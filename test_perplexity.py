# test_perplexity.py
from src.api.perplexity import PerplexityAPI

def test_deep_research():
    perplexity = PerplexityAPI()
    results = perplexity.deep_research("Who is Rick Scott and what controversies is he associated with?")
    print(f"Research completed with {len(results.get('sources', []))} sources")
    print("First 500 characters of report:")
    print(results.get('report', '')[:500])
    return results

if __name__ == "__main__":
    test_deep_research()