<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">Screenplay Writer Agent</h1>
<h3 align="center">AI-Powered Professional Screenplay Assistant</h3>

<p align="center">
  <strong>Transform ideas into industry-standard screenplays with AI-powered story development, character creation, and professional formatting</strong><br/>
  Hollywood-quality screenplay writing with proper formatting, character arcs, and scene construction
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/screenplay-writer-agent/actions/workflows/main.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/Paraschamoli/screenplay-writer-agent/main.yml?branch=main" alt="Build Status">
  </a>
  <a href="https://pypi.org/project/screenplay-writer-agent/">
    <img src="https://img.shields.io/pypi/v/screenplay-writer-agent" alt="PyPI Version">
  </a>
  <img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python Version">
  <a href="https://github.com/Paraschamoli/screenplay-writer-agent/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Paraschamoli/screenplay-writer-agent" alt="License">
  </a>
</p>

---

## 🎬 What is Screenplay Writer Agent?

An AI-powered screenplay writing assistant that transforms ideas, conversations, or rough drafts into professionally formatted screenplays. Think of it as having a Hollywood script doctor available 24/7.

### Key Features
*   **📝 Professional Formatting** - Industry-standard screenplay formatting (Final Draft, Hollywood)
*   **🎭 Character Development** - Create compelling characters with detailed backstories and arcs
*   **🎬 Scene Construction** - Build dramatic scenes with proper structure and pacing
*   **💬 Natural Dialogue** - Write authentic character dialogue with distinct voices
*   **📖 Story Development** - Transform ideas into complete 3-act structures
*   **⚡ Lazy Initialization** - Fast boot times, initializes on first request
*   **🎯 Genre Adaptation** - Write in any genre: drama, comedy, thriller, sci-fi, romance, horror

---

## 🛠️ Tools & Capabilities

### Built-in Tools
*   **CrewAI Framework** - Multi-agent system for specialized screenplay tasks
*   **Strict Screenplay Formatter** - Enforces 100% industry-standard formatting
*   **Character Development Agent** - Creates detailed character profiles and arcs
*   **Dialogue Specialist** - Writes natural, character-specific dialogue

### Screenplay Methodology
1.  **Analysis Phase** - Analyze input material, identify story elements
2.  **Development Phase** - Create characters, plot, and scene breakdowns
3.  **Writing Phase** - Write formatted screenplay with proper structure
4.  **Formatting Phase** - Apply strict industry formatting rules
5.  **Quality Phase** - Evaluate screenplay quality and suggest improvements

---

> **🌐 Join the Internet of Agents**
> Register your agent at [bindus.directory](https://bindus.directory) to make it discoverable worldwide and enable agent-to-agent collaboration. It takes 2 minutes and unlocks the full potential of your agent.

---

## 🚀 Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/Paraschamoli/screenplay-writer-agent.git
cd screenplay-writer-agent

# Set up virtual environment with uv
uv venv --python 3.12
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API key (choose one):
OPENAI_API_KEY=sk-...      # For OpenAI GPT-4o
# OR
OPENROUTER_API_KEY=sk-...  # For OpenRouter (cheaper alternative)
```

### 3. Run Locally

```bash
# Start the screenplay writer agent
python screenplay_writer_agent/main.py

# Or using uv
uv run python screenplay_writer_agent/main.py

# Agent will be available at: http://localhost:3773
```

### 4. Test with Docker

```bash
# Build and run with Docker Compose
docker-compose up --build

# Access at: http://localhost:3773
```

---

## 🔧 Configuration

### Environment Variables
Create a `.env` file:

```env
# Choose ONE provider (OpenAI takes priority if both set)
OPENAI_API_KEY=sk-...      # OpenAI API key for GPT-4o
OPENROUTER_API_KEY=sk-...  # OpenRouter API key (alternative)

# Optional
MEM0_API_KEY=your_mem0_key  # For memory features (character consistency)
MODEL_NAME=openai/gpt-4o    # Specify model (default: gpt-4o)
DEBUG=true                  # Enable debug logging
```

### Port Configuration
Default port: `3773` (can be changed in `agent_config.json`)

---

## 💡 Usage Examples

### Via HTTP API

```bash
curl -X POST http://localhost:3773/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Write a tense courtroom drama scene where a defense attorney discovers new evidence that could exonerate their client. Include character descriptions and proper screenplay formatting."
      }
    ]
  }'
```

### Sample Screenplay Queries
*   "Create a meet-cute scene for a romantic comedy set in a bookstore during a rainstorm"
*   "Develop a character profile for a retired detective in a cyberpunk setting who takes one last case"
*   "Transform this conversation into a screenplay scene: Character A: 'I never thought it would come to this.' Character B: 'You left me no choice.' Make it a thriller set in an abandoned warehouse at night"
*   "Write a 3-act structure for a sci-fi thriller about time travel paradoxes"

### Expected Output Format

```text
FADE IN:

EXT. CITY STREET - NIGHT

Rain pours down heavily. Detective MARLOWE stands under a flickering streetlight, trench coat soaked.

                         MARLOWE
                Just another rainy night in the city.

He pulls a crumpled letter from his pocket. The paper is worn, the ink smudged.

                         MARLOWE
                (to himself)
                Ten years. Ten long years.

A shadow moves in the alley across the street. Marlowe tenses.

INT. DARK ALLEY - NIGHT

Marlowe follows the shadow. His footsteps echo on wet pavement.

                         UNKNOWN VOICE
                (from darkness)
                Should have stayed retired, Marlowe.

FADE OUT.
```

---

## 🎭 Features in Detail

### Professional Formatting
*   **Scene Headers:** INT./EXT. LOCATION - TIME
*   **Character Names:** Centered, ALL CAPS
*   **Dialogue:** Properly indented under character names
*   **Action Lines:** Present tense, visual descriptions
*   **Transitions:** FADE IN:/FADE OUT., CUT TO:, DISSOLVE TO:
*   **Parentheticals:** Character actions within dialogue

### Character Development
*   **Backstory Creation:** Detailed character histories
*   **Motivation Analysis:** Character goals and conflicts
*   **Arc Planning:** Character transformation throughout story
*   **Relationship Dynamics:** Character interactions and conflicts

### Genre Support
*   **Drama:** Character-driven stories
*   **Comedy:** Humorous situations and dialogue
*   **Thriller:** Suspense and tension building
*   **Sci-Fi:** World-building and futuristic elements
*   **Romance:** Emotional connections and relationships
*   **Horror:** Atmosphere and suspense
*   **Action:** Fast-paced sequences and conflict

---

## 🐳 Docker Deployment

### Quick Docker Setup

```bash
# Build the image
docker build -t screenplay-writer-agent .

# Run container
docker run -d \
  -p 3773:3773 \
  -e OPENROUTER_API_KEY=your_key_here \
  --name screenplay-writer-agent \
  screenplay-writer-agent

# Check logs
docker logs -f screenplay-writer-agent
```

### Docker Compose (Recommended)
`docker-compose.yml`

```yaml
version: '3.8'
services:
  screenplay-writer-agent:
    build: .
    ports:
      - "3773:3773"
    environment:
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - MEM0_API_KEY=${MEM0_API_KEY}
    restart: unless-stopped
```

Run with Compose:

```bash
# Start with compose
docker-compose up -d

# View logs
docker-compose logs -f
```

---

## 📁 Project Structure

```text
screenplay-writer-agent/
├── screenplay_writer_agent/
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Main agent implementation
│   └── skills/
│       └── screenplay-writer/
│           ├── skill.yaml       # Skill configuration
│           └── __init__.py
├── agent_config.json            # Bindu agent configuration
├── pyproject.toml               # Python dependencies
├── Dockerfile                   # Multi-stage Docker build
├── docker-compose.yml           # Docker Compose setup
├── README.md                    # This documentation
├── .env.example                 # Environment template
├── uv.lock                      # Dependency lock file
└── tests/                       # Test suite
```

---

## 🔌 API Reference

### Health Check

```bash
GET http://localhost:3773/health
```

Response:
```json
{"status": "healthy", "agent": "Screenplay Writer Agent"}
```

### Chat Endpoint

```bash
POST http://localhost:3773/chat
Content-Type: application/json

{
  "messages": [
    {"role": "user", "content": "Your screenplay request here"}
  ]
}
```

Response Format:
```json
{
  "success": true,
  "screenplay": {
    "formatted_script": "FADE IN:\n\nINT. LOCATION - TIME\n\n...",
    "story_analysis": "Analysis of story elements...",
    "character_profiles": "Character descriptions...",
    "quality_score": {
      "story_structure": 8,
      "character_development": 9,
      "dialogue_quality": 8,
      "formatting": 10,
      "emotional_impact": 7,
      "overall": 8.4
    }
  }
}
```

---

## 🧪 Testing

### Local Testing

```bash
# Install test dependencies
uv sync --group dev

# Run tests
pytest tests/

# Test with specific API key
OPENROUTER_API_KEY=test_key python -m pytest
```

### Integration Test

```bash
# Start agent
python screenplay_writer_agent/main.py &

# Test API endpoint
curl -X POST http://localhost:3773/chat \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Write a short scene about two friends meeting in a café"}]}'
```

### Test Examples

```python
# Example test for screenplay formatting
def test_screenplay_formatting():
    input_text = "Two detectives discuss a case in a rainy alley"
    result = agent.generate_screenplay(input_text)
    assert "FADE IN" in result
    assert "INT." in result or "EXT." in result
    assert any(char.isupper() and len(char) < 30 for char in result.split('\n'))
```

---

## 🚨 Troubleshooting

### Common Issues & Solutions

**"No API key available"**
```bash
# Check if .env file exists and has correct variable names
cat .env

# Set API key directly
export OPENROUTER_API_KEY=your_key_here
```

**"Port 3773 already in use"**
```bash
# Find and kill process using port 3773
lsof -ti:3773 | xargs kill -9

# Or change port in agent_config.json
```

**"ModuleNotFoundError: No module named 'crewai'"**
```bash
# Reinstall dependencies
uv sync --force

# Check uv.lock is present
ls -la uv.lock
```

**"Crew not initialized"**
*   Ensure API key is valid
*   Check network connectivity
*   Try with `DEBUG=true` for more details

**Docker build fails**
```bash
# Clean Docker cache
docker system prune -a

# Rebuild without cache
docker-compose build --no-cache
```

**"Input too long" error**
*   Maximum input length: 5000 characters
*   Break complex requests into multiple queries
*   Use the character development feature separately

---

## 📊 Dependencies

### Core Packages
*   `bindu==2026.1.12` - Agent deployment framework
*   `crewai>=0.80.0` - Multi-agent framework for screenplay tasks
*   `langchain>=0.1.0` - LLM orchestration
*   `openai>=2.11.0` - OpenAI client
*   `mem0ai>=1.0.1` - Memory for character consistency
*   `python-dotenv>=1.0.1` - Environment management
*   `pyyaml>=6.0` - Configuration parsing

### Development Packages
*   `pytest>=7.2.0` - Testing framework
*   `ruff>=0.11.5` - Code formatting/linting
*   `pre-commit>=2.20.0` - Git hooks

### Utility Packages
*   `requests>=2.31.0` - HTTP requests
*   `rich>=13.0.0` - Console output formatting
*   `pyperclip>=1.8.0` - Clipboard operations for screenplay copying

---

## 🤝 Contributing

We welcome contributions from screenwriters, developers, and AI enthusiasts! Please follow these steps:

1.  Fork the repository
2.  Create a feature branch: `git checkout -b feature/screenplay-improvement`
3.  Make your changes following screenplay formatting standards
4.  Add tests for new screenplay features
5.  Commit with descriptive messages
6.  Push to your fork
7.  Open a Pull Request

**Code Style Guidelines:**
*   Follow PEP 8 conventions
*   Use type hints for all function signatures
*   Add docstrings for public functions
*   Maintain strict screenplay formatting in test cases
*   Keep functions focused on single screenplay elements

**Areas for Contribution:**
*   Additional screenplay genres (musical, documentary, etc.)
*   Enhanced character relationship mapping
*   Dialogue improvement algorithms
*   Export to Final Draft/Fountain format
*   Integration with screenplay databases

---

## 📄 License
MIT License - see LICENSE file for details.

---

## 🙏 Credits & Acknowledgments

*   **Developer:** Paras Chamoli
*   **Framework:** Bindu - Agent deployment platform
*   **Agent Framework:** CrewAI - Multi-agent orchestration
*   **Screenplay Formatting:** Industry-standard Hollywood formatting rules
*   **Memory Management:** Mem0 for character consistency

**Special Thanks**
*   Hollywood screenplay formatting standards
*   Final Draft and Celtx for industry benchmarks
*   Screenwriting community for best practices

### 🔗 Useful Links
*   🌐 **Bindu Directory:** bindus.directory
*   📚 **Bindu Docs:** docs.getbindu.com
*   🐙 **GitHub:** github.com/Paraschamoli/screenplay-writer-agent
*   🎬 **Screenplay Resources:** WriterDuet, Final Draft
*   💬 **Discord:** Bindu Community

<p align="center">
  <strong>Built with ❤️ by Paras Chamoli</strong><br/>
  <em>Bringing Hollywood screenplay quality to every writer</em>
</p>

<p align="center">
  <a href="https://github.com/Paraschamoli/screenplay-writer-agent/stargazers">⭐ Star on GitHub</a> •
  <a href="https://bindus.directory">🌐 Register on Bindu</a> •
  <a href="https://github.com/Paraschamoli/screenplay-writer-agent/issues">🐛 Report Issues</a>
</p>

> **Note:** This agent follows strict Hollywood screenplay formatting standards with 100% precision. It uses lazy initialization for fast startup and maintains character consistency through memory features when Mem0 API key is provided.
