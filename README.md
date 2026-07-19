# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project is a Python music recommender simulation that loads a catalog of 20 songs from a CSV file. It scores every song based on a user's preference profile using a point system. Songs get points for matching mood, genre, and energy closeness, a bonus for acoustic, and penalty for disliked genre. It then returns the top 5 songs with the highest scores along with reasons why.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
    - My system will use similar features as given but they will have a point system.
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
Loaded songs: 20

=== High-Energy Pop ===
Top recommendations:

Sunrise City - Score: 4.96
Because: matches your favorite genre (pop); matches your favorite mood (happy); energy closely matches your preference

Gym Hero - Score: 3.74
Because: matches your favorite genre (pop); energy closely matches your preference

Rooftop Lights - Score: 2.92
Because: matches your favorite mood (happy); energy closely matches your preference

Night Drive Loop - Score: 1.90
Because: energy closely matches your preference

Concrete Skyline - Score: 1.90
Because: energy closely matches your preference


=== Chill Lofi ===
Top recommendations:

Library Rain - Score: 5.00
Because: matches your favorite genre (lofi); matches your favorite mood (chill); energy closely matches your preference

Midnight Coding - Score: 4.86
Because: matches your favorite genre (lofi); matches your favorite mood (chill); energy closely matches your preference

Focus Flow - Score: 3.90
Because: matches your favorite genre (lofi); energy closely matches your preference

Spacewalk Thoughts - Score: 2.86
Because: matches your favorite mood (chill); energy closely matches your preference

Coffee Shop Stories - Score: 1.96
Because: energy closely matches your preference


=== Deep Intense Rock ===
Top recommendations:

Storm Runner - Score: 4.98
Because: matches your favorite genre (rock); matches your favorite mood (intense); energy closely matches your preference

Gym Hero - Score: 2.94
Because: matches your favorite mood (intense); energy closely matches your preference

Starlight Anthem - Score: 2.00
Because: energy closely matches your preference

Broken Curfew - Score: 1.96
Because: energy closely matches your preference

Concrete Skyline - Score: 1.90
Because: energy closely matches your preference
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
  - Genre becomes a weaker weight than mood. This causes song candidates to be closer in values.
- What happened when you added tempo or valence to the score
  - Tempo becomes redundant with energy and adds bias instead of removing it. Valence seems to be worth adding since it reduces bias with other features. Valence is a good addition to energy.
- How did your system behave for different types of users
  - The system behaved similarly between the different users. The top 5 songs picked are different based on the users' preferences.

---

## Limitations and Risks

Summarize some limitations of your recommender.

- `target_energy` is not validated
- `favorite_artists` and `context` fields exist on user profile but are never used by the scoring logic
- Case/whitespace sensitive
- `likes_acoustic` is redundant
- Genre is the main decider of high scores

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
  - Recommenders take algorithmic logic from given data in order to turn them into predictions. Coming up with a accurate and reliable logic can make predictions good for testing in real-world use cases. With bad logic, recommenders become unreliable and will give misinformation to users. 
- about where bias or unfairness could show up in systems like this
  - Bias and unfairness can show up easily in a lot systems like this because numbers can decide everything. For example, in the recommender, genre adds 2 points to the score if it matches with the user's favorite genre. Since scores are weighted out of 5.0, 2 points is a lot. If preferences have affects on larger numbers, it will cause the top 5 scores to be inaccurate.



