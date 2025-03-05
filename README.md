# Research Illuminator

## Illuminating Complex Topics Through Multi-Source Research and AI Analysis

Research Illuminator is a tool that combines deep search capabilities with AI analysis to generate comprehensive, nuanced reports on complex topics that are often misrepresented or poorly documented in mainstream coverage.

![Status: Early Development](https://img.shields.io/badge/Status-Early%20Development-yellow)

## Project Vision

In today's information ecosystem, finding basic facts is easy, but developing deep understanding is hard. Research Illuminator addresses this gap by:

1. **Connecting disparate information sources** across time and platforms
2. **Revealing patterns and relationships** that aren't visible in isolated sources
3. **Highlighting inconsistencies and gaps** in mainstream coverage
4. **Generating comprehensive reports** with full source attribution

The project aims to democratize in-depth research capabilities that typically require extensive time and expertise.

## How It Works

Research Illuminator follows a systematic pipeline:

1. **Query Processing**: Transforms initial questions into comprehensive search strategies
2. **Deep Information Retrieval**: Utilizes Perplexity API to gather information across diverse sources
3. **Source Analysis**: Classifies and evaluates source credibility and perspective
4. **Content Extraction**: Identifies key facts, claims, and contextual information
5. **Pattern Recognition**: Discovers connections, contradictions, and corroborations across sources
6. **Report Generation**: Creates structured narratives with full source attribution
7. **Insight Highlighting**: Emphasizes significant patterns, gaps, or inconsistencies

## Project Status

This project is in early prototype development. The current focus is on building core functionality for:

- Integration with Perplexity API for information retrieval
- Structured storage of research findings
- Basic analysis using Claude/OpenAI APIs
- Simple report generation

## Case Study: Rick Scott and Columbia/HCA

The project concept was validated through a manual case study examining Rick Scott's journey from healthcare executive to U.S. Senator.

This research connected:
- His role as CEO during the largest Medicare fraud case in U.S. history
- The $1.7 billion settlement paid by Columbia/HCA
- Scott's $300 million severance package despite the company's guilty pleas
- His subsequent political career and positions on healthcare policy

This case demonstrated the value of connecting information across multiple sources and time periods to reveal significant patterns typically not presented together in mainstream coverage.

## Future Case Studies

Future development will include additional case studies in areas such as:

- Corporate accountability and malfeasance
- Political figures with complex histories
- Underreported global events
- Historical controversies with modern implications

## Technical Architecture

Research Illuminator is built on:

- **Backend**: Python for core processing
- **Data Storage**: MongoDB for flexible document storage
- **APIs**: Perplexity API (information retrieval), Claude/OpenAI API (analysis)
- **Frontend**: Streamlit for simple user interface (future development)

## Getting Started

### Prerequisites

- Python 3.8+
- API keys for Perplexity and Claude/OpenAI
- MongoDB (local or Atlas)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/research-illuminator.git
cd research-illuminator

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up configuration
cp config.example.py config.py
# Edit config.py with your API keys
```

### Basic Usage

```bash
# Run basic prototype
python research.py "Research topic query"
```

## Project Roadmap

### Phase 1: Core Functionality (Current)
- Information retrieval integration
- Basic data processing
- Simple report generation

### Phase 2: Expanded Analysis
- Enhanced pattern recognition
- More sophisticated source evaluation
- Improved report formatting

### Phase 3: User Experience
- Web interface development
- Visualization capabilities
- Collaboration features

## Contributing

This project is currently a personal research tool in early development. However, feedback, suggestions, and discussions are welcome through issues.

## Acknowledgments

- This project is inspired by the challenges of navigating complex information in the modern media environment
- Special thanks to my academic research mentor for guidance
- Built using the capabilities of Perplexity and Claude/OpenAI

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*Note: This is an undergraduate research project in early development. The tool aims to support human research rather than replace critical thinking or domain expertise.*
