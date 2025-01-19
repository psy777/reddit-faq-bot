# Reddit FAQ Maker

Generate niche, helpful FAQs from Reddit posts and comments. This tool allows users to input a topic, search Reddit for relevant discussions, identify frequently asked questions, and summarize the best answers into a structured FAQ format.

---

## Features

- **Topic-Based Search**: Input a topic and retrieve relevant questions from Reddit.
- **Summarized Answers**: Uses a Hugging Face transformer model to generate concise answers.
- **Subreddit Customization**: Search across all subreddits or a specific subreddit.
- **Flexible Output**: Returns FAQs in a clear, structured format.

---

## Prerequisites

- Python 3.8 or higher
- Reddit API credentials (create an app at [Reddit's Developer Portal](https://www.reddit.com/prefs/apps))
- Virtual environment (recommended)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/reddit-faq-maker.git
   cd reddit-faq-maker
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv faqbotenv
   source faqbotenv/bin/activate  # Windows: faqbotenv\\Scripts\\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Reddit API credentials:
   - Create a `credentials.json` file in the project root:
     ```json
     {
         "client_id": "your_client_id",
         "client_secret": "your_client_secret",
         "user_agent": "your_user_agent"
     }
     ```

---

## Usage

1. Run the script:
   ```bash
   python faq_maker_script.py
   ```

2. Enter a topic when prompted (e.g., `iPhone screen dimming`).

3. View the generated FAQs in the terminal.

---

## Example

**Input Topic**: `iPhone screen dimming`

**Generated FAQ**:
```
Q1: Why does my iPhone screen dim automatically?
A1: Your iPhone screen dims due to Auto-Brightness. Go to Settings > Accessibility > Display & Text Size and disable Auto-Brightness to stop this behavior.
Source: https://reddit.com/r/example-thread

Q2: How can I adjust the screen brightness manually?
A2: You can swipe down from the top-right corner to access Control Center and adjust the brightness slider.
Source: https://reddit.com/r/example-thread
```

---

## Tech Stack

- **Python**: Core language
- **praw**: Reddit API integration
- **Hugging Face Transformers**: Summarization of long answers
- **PyTorch**: Backend for the summarization model
- **pandas**: Data organization

---

## Contributing

1. Fork the repository:
   ```bash
   git fork https://github.com/your-username/reddit-faq-maker.git
   ```
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request via GitHub.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Reddit API Documentation](https://www.reddit.com/dev/api)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [PyTorch](https://pytorch.org/)
