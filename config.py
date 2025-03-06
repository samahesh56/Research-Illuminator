"""
Configuration module for Research Illuminator.
Loads environment variables and provides configuration settings.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DB = os.getenv("MONGO_DB", "research_illuminator")

# Research Configuration
DEFAULT_SOURCES_PER_QUERY = 10
MAX_DEPTH = 3  # Maximum levels of recursive querying (for reference only now)

# AI Configuration
# OpenAI Configuration
OPENAI_MODEL = "gpt-4"

# Anthropic Configuration
ANTHROPIC_MODEL = "claude-3-opus-20240229"  # Or your preferred Claude model

# Perplexity Configuration
PERPLEXITY_MODEL = "sonar-deep-research"  # Deep research model
PERPLEXITY_MAX_TOKENS = 4000              # Default max tokens for responses
PERPLEXITY_TEMPERATURE = 0.2              # Default temperature
PERPLEXITY_TOP_P = 0.9                    # Default top_p setting
PERPLEXITY_FREQUENCY_PENALTY = 1.0        # Default frequency penalty

# Check for required configuration
def validate_config():
    """Validate that all required configuration is present."""
    required_vars = [
        "PERPLEXITY_API_KEY",
        "OPENAI_API_KEY" if not ANTHROPIC_API_KEY else None,
        "ANTHROPIC_API_KEY" if not OPENAI_API_KEY else None,
    ]
    
    missing = [var for var in required_vars if var and not globals().get(var)]
    
    if missing:
        raise EnvironmentError(
            f"Missing required configuration: {', '.join(missing)}"
        )

# Run validation when module is imported
validate_config()