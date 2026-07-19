from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field, asdict

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    disliked_genres: List[str] = field(default_factory=list)
    favorite_artists: List[str] = field(default_factory=list)
    context: Optional[str] = None

import csv

# Point-based recipe. Genre is the strongest categorical signal, mood is
# softer/fuzzier, and energy similarity is continuous so it contributes
# across every song rather than only on an exact match.
GENRE_POINTS = 2.0
MOOD_POINTS = 1.0
ENERGY_MAX_POINTS = 2.0
ACOUSTIC_BONUS = 0.5
ACOUSTIC_BONUS_THRESHOLD = 0.6
DISLIKED_GENRE_PENALTY = -3.0


def _score_core(song: Dict, user: Dict) -> Tuple[float, List[str]]:
    """
    Shared scoring math for both the dict-based and dataclass-based APIs.
    song / user use the same key names: genre, mood, energy,
    likes_acoustic, disliked_genres.
    Additive point recipe (not normalized to 0-1):
      +2.0 genre match, +1.0 mood match, up to +2.0 for energy closeness,
      +0.5 acoustic bonus, -3.0 disliked genre penalty.
    """
    reasons: List[str] = []
    score = 0.0

    genre = user.get("genre")
    if genre is not None and song.get("genre") == genre:
        score += GENRE_POINTS
        reasons.append(f"matches your favorite genre ({genre})")

    mood = user.get("mood")
    if mood is not None and song.get("mood") == mood:
        score += MOOD_POINTS
        reasons.append(f"matches your favorite mood ({mood})")

    target_energy = user.get("energy")
    song_energy = song.get("energy")
    if target_energy is not None and song_energy is not None:
        sim = max(0.0, 1 - abs(target_energy - song_energy))
        score += ENERGY_MAX_POINTS * sim
        if sim >= 0.8:
            reasons.append("energy closely matches your preference")

    if user.get("likes_acoustic") and (song.get("acousticness") or 0) >= ACOUSTIC_BONUS_THRESHOLD:
        score += ACOUSTIC_BONUS
        reasons.append("acoustic sound matches your taste")

    if song.get("genre") in (user.get("disliked_genres") or []):
        score += DISLIKED_GENRE_PENALTY
        reasons.append(f"genre ({song.get('genre')}) is on your disliked list")

    if not reasons:
        reasons.append("limited overlap with your preferences")

    return round(score, 2), reasons


def _user_profile_to_dict(user: "UserProfile") -> Dict:
    """Converts a UserProfile into the plain dict shape _score_core expects."""
    return {
        "genre": user.favorite_genre,
        "mood": user.favorite_mood,
        "energy": user.target_energy,
        "likes_acoustic": user.likes_acoustic,
        "disliked_genres": user.disliked_genres,
    }


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Scores every song against the user profile and returns the top k."""
        user_dict = _user_profile_to_dict(user)
        scored = [
            (song, _score_core(asdict(song), user_dict)[0])
            for song in self.songs
        ]
        scored.sort(key=lambda pair: pair[1], reverse=True)
        return [song for song, _score in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable reason string for why a song was scored as it was."""
        _score, reasons = _score_core(asdict(song), _user_profile_to_dict(user))
        return "; ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    numeric_fields = {"energy", "tempo_bpm", "valence", "danceability", "acousticness"}
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for key in numeric_fields:
                row[key] = float(row[key])
            row["id"] = int(row["id"])
            songs.append(row)
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    return _score_core(song, user_prefs)


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    scored.sort(key=lambda triple: triple[1], reverse=True)
    return [(song, score, "; ".join(reasons)) for song, score, reasons in scored[:k]]
