from importlib.resources import read_text
from jinja2 import Environment, FileSystemLoader, BaseLoader

import cheinsteinpy
import json

with open("config.json", "r") as f:
    config = json.load(f)

with open("cookie.txt", 'r') as f:
    cookieTxt = f.read()

env = Environment(loader=FileSystemLoader('templates/'))
temp = env.get_template('chapterQuestion.html')
results_filename = "steps.html"  
url = "https://www.chegg.com/homework-help/a-brief-introduction-to-criminal-law-2nd-edition-chapter-2-problem-19pt-solution-9781284056112"

answerRaw = cheinsteinpy.answer(url, cookieTxt, config['userAgent'])
questionRaw = cheinsteinpy.question(url, cookieTxt, config['userAgent'])
# print(answerRaw)
total = len(answerRaw)
steps = {step + 1:answerRaw[step] for step in range(0, total )}
context = {
    'problemTitle': questionRaw,
    'steps': steps,
    'totalSteps': total
}
with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(temp.render(context))
    print(f"... wrote {results_filename}")
