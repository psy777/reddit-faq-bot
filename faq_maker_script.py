import praw
import re
import pandas as pd
from transformers import pipeline
import json

def load_credentials(file_path="credentials.json"):
    with open(file_path, "r") as file:
        return json.load(file)

def setup_reddit_client():
    credentials = load_credentials()
    return praw.Reddit(
        client_id=credentials["client_id"],
        client_secret=credentials["client_secret"],
        user_agent=credentials["user_agent"]
    )

def fetch_reddit_data(topic, subreddit='all', limit=100):
    reddit = setup_reddit_client()
    subreddit = reddit.subreddit(subreddit)
    data = []
    for post in subreddit.search(topic, limit=limit):
        if not post.stickied:  # Ignore pinned posts
            data.append({
                'title': post.title,
                'selftext': post.selftext,
                'comments': post.num_comments,
                'url': post.url,
                'score': post.score,
            })
    return data

def fetch_comments(post_url, max_comments=10):
    reddit = setup_reddit_client()
    submission = reddit.submission(url=post_url)
    submission.comments.replace_more(limit=0)  # Flatten nested comments
    comments = []
    for comment in submission.comments[:max_comments]:
        comments.append({
            'body': comment.body,
            'score': comment.score
        })
    return comments

def extract_questions(text):
    question_pattern = r".+\?$"  # Ends with a question mark
    questions = [line.strip() for line in text.split('\n') if re.match(question_pattern, line)]
    return questions

def get_best_answer(comments):
    if not comments:
        return None
    best_comment = max(comments, key=lambda x: x['score'])
    return best_comment['body']

def summarize_text(text):
    summarizer = pipeline('summarization')
    if len(text.split()) < 50:  # Skip short comments
        return text
    return summarizer(text, max_length=50, min_length=25, do_sample=False)[0]['summary_text']

def generate_faq(topic, subreddit='all', limit=100):
    posts = fetch_reddit_data(topic, subreddit, limit)
    faq = []

    for post in posts:
        questions = extract_questions(post['title'] + "\n" + post['selftext'])
        if not questions:
            continue

        comments = fetch_comments(post['url'])
        best_answer = get_best_answer(comments)

        if best_answer:
            faq.append({
                'question': questions[0],  # Take the first detected question
                'answer': summarize_text(best_answer),
                'source': post['url']
            })
    return faq

def display_faq(faq):
    for i, qa in enumerate(faq, 1):
        print(f"Q{i}: {qa['question']}")
        print(f"A{i}: {qa['answer']}")
        print(f"Source: {qa['source']}\n")

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    faq = generate_faq(topic, subreddit="learnpython", limit=50)
    display_faq(faq)
