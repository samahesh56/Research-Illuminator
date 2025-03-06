"""
Perplexity API integration for deep research capabilities.
"""
import requests
import json
from typing import List, Dict, Any, Optional
import time
import os
import sys

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now use absolute imports
from config import (
    PERPLEXITY_API_KEY,
    PERPLEXITY_MODEL,
    PERPLEXITY_MAX_TOKENS,
    PERPLEXITY_TEMPERATURE,
    PERPLEXITY_TOP_P,
    PERPLEXITY_FREQUENCY_PENALTY
)

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
    
    def search(self, query: str, max_results: int = 10) -> List[Dict[str, Any]]:
        """Perform a standard search using the Perplexity API.
        
        Args:
            query: The search query
            max_results: Maximum number of results to return
            
        Returns:
            List of search results, each with source information
        """
        endpoint = f"{self.BASE_URL}/chat/completions"
        
        # Create a system prompt that guides the model to provide search results
        system_prompt = "Provide factual search results for the user's query with citations."
        
        payload = {
            "model": "sonar",  # Using standard sonar model for basic searches
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            "max_tokens": 2000,
            "temperature": 0.1,
            "top_p": 0.9,
            "return_images": False,
            "return_related_questions": False
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
            citations = result.get("citations", [])
            
            # Process the response into a list of search results
            processed_results = []
            
            # If we have content and citations, create structured results
            if content and citations:
                # Create a result entry for each citation
                for idx, citation in enumerate(citations):
                    processed_results.append({
                        "title": f"Result {idx+1}",  # We don't have titles directly from the API
                        "content": content,  # The full content from the model
                        "url": citation,
                        "source": citation,
                        "relevance_score": 1.0 - (0.1 * idx)  # Mock relevance score
                    })
            
            # Limit to requested number of results
            return processed_results[:max_results]
            
        except requests.RequestException as e:
            print(f"Error querying Perplexity API: {e}")
            return []
    
    def deep_research(self, query: str, max_tokens: int = PERPLEXITY_MAX_TOKENS, 
                      temperature: float = PERPLEXITY_TEMPERATURE, 
                      search_recency_filter: Optional[str] = None) -> Dict[str, Any]:
        """Perform deep research using Perplexity's sonar-deep-research model.
        
        Utilizes Perplexity's advanced Deep Research capabilities to conduct
        comprehensive research on the query topic, performing dozens of searches,
        reading hundreds of sources, and reasoning through the material to deliver
        a complete report.
        
        Args:
            query: The research question or topic
            max_tokens: Maximum tokens for the response
            temperature: Temperature for generation variability
            search_recency_filter: Optional time filter ("month", "week", "day", "hour")
            
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
            "model": PERPLEXITY_MODEL,
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
            "top_p": PERPLEXITY_TOP_P,
            "frequency_penalty": PERPLEXITY_FREQUENCY_PENALTY,
            "return_images": False,
            "return_related_questions": False
        }
        
        # Add optional search recency filter if provided
        if search_recency_filter:
            payload["search_recency_filter"] = search_recency_filter
        
        try:
            print(f"Starting deep research on: {query}")
            print("This may take several minutes as Perplexity processes multiple searches...")
            
            start_time = time.time()
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            end_time = time.time()
            
            processing_time = end_time - start_time
            
            result = response.json()
            
            # Extract the response content and citations
            research_content = result.get("choices", [{}])[0].get("message", {}).get("content", "No content generated")
            citations = result.get("citations", [])
            
            # Format the sources from citations
            sources = []
            for idx, citation in enumerate(citations):
                sources.append({
                    "id": idx,
                    "title": f"Source {idx+1}",
                    "url": citation,
                    "source_type": "web",
                    "excerpt": f"Citation from {citation}"
                })
            
            # Format into a structured result
            research_result = {
                "query": query,
                "report": research_content,
                "sources": sources,
                "key_findings": [],  # We'd need to extract these from the content or via another API call
                "metadata": {
                    "model": result.get("model", PERPLEXITY_MODEL),
                    "created": result.get("created", int(time.time())),
                    "processing_time": processing_time,
                    "sources_analyzed": len(citations),
                    "searches_performed": "unknown",  # The API doesn't tell us this directly
                    "usage": result.get("usage", {})
                }
            }
            
            print(f"Deep research completed in {processing_time:.2f} seconds with {len(citations)} citations.")
            return research_result
            
        except requests.RequestException as e:
            error_message = f"Error in deep research: {e}"
            if hasattr(e, 'response') and e.response is not None:
                error_message += f" Response: {e.response.text}"
            
            print(error_message)
            return {
                "error": str(e),
                "query": query,
                "report": "Error occurred during research.",
                "sources": [],
                "metadata": {}
            }

# Example usage:
# perplexity = PerplexityAPI()
# results = perplexity.deep_research("Who is Rick Scott and what controversies is he associated with?")