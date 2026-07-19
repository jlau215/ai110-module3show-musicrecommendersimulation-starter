# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
    - My system will use similar features as given but they will have a different weighting system.
- What information does your `UserProfile` store
  - My `UserProfile` stores favorite genre and mood, target energy, and whether acoustic is liked or not. Additonal information are target valence, danceability, tempo, disliked generes, favorite artists, and context.
- How does your `Recommender` compute a score for each song
  - My `Recommender` computes a score for each song by adding 2.0 points if the song's genre matches the user's favorite genre, add 1.0 point if the mood matches, and up to 2.0 points based on how close the song's energy is to the user's target energy. It also adds a +0.5 bonus if the user likes acoustic music and the song's acousticness is high, and subtracts 3.0 points if the song's genre is on the user's disliked list. The score is not capped at 1.0. A perfect match across genre, mood, and energy goes around 5.0.
- How do you choose which songs to recommend
  - Every song in the catalog gets scored against the user profile, the list is sorted by score descending, and the top `k` (default 5) are returned as recommendations.

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



