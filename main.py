#extract keywords from the job description
import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')

def extract_skills(job_desc_file):
    skills = []
    matcher = PhraseMatcher(nlp.vocab)
    with open('skillset.txt', 'r') as f:
        skill_list = [line.strip() for line in f]
    patterns = [nlp(text) for text in skill_list]
    matcher.add("SKILL", None, *patterns)
    with open(job_desc_file, 'r') as f:
        job_desc_text = f.read()
    doc = nlp(job_desc_text)
    matches = matcher(doc)
    for match_id, start, end in matches:
        skills.append(doc[start:end].text)
    return skills

job_desc_file = 'jd-software role.txt'
skills = extract_skills(job_desc_file)

skills=list(set(skills))
for s in skills:
  print(s)
#best results using pharsematcher







