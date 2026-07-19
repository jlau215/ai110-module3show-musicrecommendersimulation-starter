# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
**MuseRec 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
  - The recommender generates recommendations based on acoustic values, mood, genre, and more.
- What assumptions does it make about the user  
  - The user wants to be recommended songs based on preferences.
- Is this for real users or classroom exploration 
  - Classroom exploration 

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
  - Features of each song that are used are genre, energy, mood, and acoustic.
- What user preferences are considered  
  - Favorite mood and genre, target energy, likes acoustic, disliked genres, and favorite artists.
- How does the model turn those into a score  
- What changes did you make from the starter logic  
  - Removed the use of valence, tempo, and daceability in the score calculation. Then added an extra function to calculate scores.

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
  - 20 songs.
- What genres or moods are represented  
  - Pop, lofi, rock, ambient, jazz, synthwave, indie pop, classical, hip hop, country, reggae, metal, blues, k-pop, house, punk latin.
- Did you add or remove data  
  - Add data.
- Are there parts of musical taste missing in the dataset  
  - Yes, I could've added more to the dataset to make each song more specific.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
  - User types that have more preferences into mood, genre, and energy tend to get more reasonable results.
- Any patterns you think your scoring captures correctly 
  - Patterns I think is scored correctly is how matching genre and mood tend to get higher scores. 
- Cases where the recommendations matched your intuition  
  - Lack of songs with the same main genre causes the recommendations to have a large gap in scores.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
   - No constraints for diversity so genre repeats are left unchecked.
   - Case and whitespace sensitivity.
- Genres or moods that are underrepresented  
  - Metal, angry mood, and energy around 0.6.
- Cases where the system overfits to one preference  
  - The system overfits to "sum of positives", causing lack of weight for one explicit negative such as dislike a user gave.
  - Energy alone drives ranking when genre and or mood are absent.
  - The acoustic bonus double counts genre.
- Ways the scoring might unintentionally favor some users  
  - Users who favorite a common genre or mood get more advantages than users who favorite less common ones.
  - Users who set more disliked_genres gets less reliable results than a user who states none.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
  - I tested High-Energy Pop, Chill Lofi, and Deep Intense Rock user profiles.
- What you looked for in the recommendations  
  - I looked for accuracy and reasons for each score.
- What surprised you  
  - Each user profile shows very different results for their top 5 recommended songs.
- Any simple tests or comparisons you ran  
  - Tested removing the mood feature to see how the results change. I noticed that the scores for all recommendations were significantly lower.

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
  - Add more preferences to utilize the features such as tempo, valence, danceability, and more to help differentiate songs better.
- Better ways to explain recommendations  
  - Have more reasons to why recommendations were given the score that was shown.
- Improving diversity among the top results  
  - Add more preferences and songs to create more diversity.
- Handling more complex user tastes  
  - Add more features that each song can have.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
  - Recommender systems are complex and require a lot time and thinking to create reliable and accurate ones.
- Something unexpected or interesting you discovered 
  -  Setting up a separate function just for score calculations makes the code cleaner since it can be reused in other functions.
- How this changed the way you think about music recommendation apps  
  - This made me think more about how music recommendations apps come up with reliable algorithms to recommend songs to users based on their preferences and actions.
