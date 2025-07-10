# match_score.py

import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text.lower())
    return [token.lemma_ for token in doc if token.pos_ in ["NOUN", "PROPN", "VERB", "ADJ"] and not token.is_stop]

def calculate_match_score(resume_text, jd_text):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    all_texts = [" ".join(resume_keywords), " ".join(jd_keywords)]
    vectorizer = CountVectorizer().fit_transform(all_texts)
    vectors = vectorizer.toarray()

    score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    match_score = int(score * 100)

    common_skills = set(resume_keywords) & set(jd_keywords)
    return match_score, list(common_skills)
