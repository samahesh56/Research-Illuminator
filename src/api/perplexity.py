"""
Perplexity API integration for deep research capabilities.
"""
import requests
import json
from typing import List, Dict, Any, Optional
import time

from ...config import PERPLEXITY_API_KEY

class PerplexityAPI:
    """Client for interacting with the Perplexity API for deep research."""
    
    BASE_URL = "https://api.perplexity.ai"
    
    def __init__(self, api_key: str = PERPLEXITY_API_KEY):
        """Initialize the Perplexity API client.
        
        Args:
            api_key: Perplexity API key
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def deep_research(self, query: str, max_tokens: int = 4000, temperature: float = 0.2, 
                      search_recency_filter: Optional[str] = None) -> Dict[str, Any]:
        """Perform deep research using Perplexity's sonar-deep-research model.
        
        Args:
            query: The research question or topic
            max_tokens: Maximum tokens in the response (default: 4000)
            temperature: Temperature for generation (default: 0.2)
            search_recency_filter: Time filter ("month", "week", "day", "hour") or None
            
        Returns:
            A dictionary containing the research report and metadata
        """
        endpoint = f"{self.BASE_URL}/chat/completions"
        
        # Create a detailed system prompt that guides the model to perform deep research
        system_prompt = """You are a research assistant conducting in-depth research on complex topics. 
Your task is to:
1. Gather comprehensive information from multiple sources
2. Analyze patterns, connections, and contradictions across sources
3. Pay special attention to connections across different time periods
4. Identify important but non-obvious insights
5. Create a well-structured, detailed report with full citations
6. Include a timeline of key events where relevant

Your report should be thorough, balanced, and properly cited with sources."""
        
        payload = {
            "model": "sonar-deep-research",
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": f"Conduct a comprehensive investigation on: {query}. Include all relevant details, connections across time periods, and proper citations."
                }
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": 0.9,
            "frequency_penalty": 1,
            "return_images": False,
            "return_related_questions": False
        }
        
        # Add optional search recency filter if provided
        if search_recency_filter:
            payload["search_recency_filter"] = search_recency_filter
        
        try:
            print(f"Starting deep research on: {query}")
            print("This may take several minutes as Perplexity processes multiple searches...")
            
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            
            # Extract the response content and citations
            research_content = result.get("choices", [{}])[0].get("message", {}).get("content", "No content generated")
            citations = result.get("citations", [])
            
            # Format into a structured result
            research_result = {
                "query": query,
                "report": research_content,
                "sources": [{"url": citation} for citation in citations],
                "metadata": {
                    "model": result.get("model", "unknown"),
                    "created": result.get("created", 0),
                    "usage": result.get("usage", {})
                }
            }
            
            print(f"Deep research completed with {len(citations)} citations.")
            return research_result
            
        except requests.RequestException as e:
            print(f"Error in deep research: {e}")
            return {
                "error": str(e),
                "query": query
            }   
        
def search(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
    """Perform a standard search using the Perplexity API.
    
    Args:
        query: The search query
        max_results: Maximum number of results to return
        
    Returns:
        List of search results, each with source information
    """
    endpoint = f"{self.BASE_URL}/chat/completions"
    
    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": "Provide search results for the user's query."
            },
            {
                "role": "user",
                "content": query
            }
        ],
        "max_tokens": 2000,
        "temperature": 0.1
    }
    
    try:
        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
        citations = result.get("citations", [])
        
        # Processing to extract structured results from content would go here
        # For now, return a simplified format
        return [{"title": query, "content": content, "url": citation} for citation in citations]
        
    except requests.RequestException as e:
        print(f"Error querying Perplexity API: {e}")
        return []