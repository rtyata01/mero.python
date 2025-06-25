from datetime import datetime, timedelta
import math

# Sample post and user data structure
class Post:
    def __init__(self, id, author_id, created_at, likes, comments, shares):
        self.id = id
        self.author_id = author_id
        self.created_at = created_at
        self.likes = likes
        self.comments = comments
        self.shares = shares

class User:
    def __init__(self, id, friends, interactions):
        self.id = id
        self.friends = friends  # list of friend user_ids
        self.interactions = interactions  # dict: {author_id: interaction_score}

def recency_score(post, current_time):
    # Exponential decay: newer posts get higher scores
    delta = current_time - post.created_at
    hours_passed = delta.total_seconds() / 3600
    return math.exp(-0.1 * hours_passed)

def interaction_score(user, post):
    # How much the user has interacted with this author
    return user.interactions.get(post.author_id, 0)

def relationship_score(user, post):
    # Basic: 1 if friend, else 0. Can be more complex
    return 1 if post.author_id in user.friends else 0

def popularity_score(post):
    # Weighted sum of engagement metrics
    return post.likes * 1 + post.comments * 2 + post.shares * 3

def rank_posts(posts, user, current_time):
    scored_posts = []
    for post in posts:
        score = (
            0.4 * recency_score(post, current_time) +
            0.3 * interaction_score(user, post) +
            0.2 * relationship_score(user, post) +
            0.1 * popularity_score(post)
        )
        scored_posts.append((post, score))
    scored_posts.sort(key=lambda x: x[1], reverse=True)
    return [p[0] for p in scored_posts]

# Example usage:
now = datetime.now()

posts = [
    Post(1, 101, now - timedelta(hours=1), likes=10, comments=5, shares=1),
    Post(2, 102, now - timedelta(hours=5), likes=50, comments=10, shares=0),
    Post(3, 103, now - timedelta(minutes=30), likes=5, comments=1, shares=0),
]

user = User(201, friends=[101, 103], interactions={101: 5, 103: 2})

ranked = rank_posts(posts, user, now)
for post in ranked:
    print(f"Post {post.id} by Author {post.author_id}")
