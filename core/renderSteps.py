import re
from jinja2 import Environment, FileSystemLoader, BaseLoader

# ENV = Environment(loader=FileSystemLoader('templates/'))
# TEMPLATE = ENV.get_template('chapterQuestion.html')
# FILENAME = "answers.html"

def format_steps(answer, total):
    reg = '(https?://+)'
    steps = {step + 1: str(re.subn('png', 'png">', str(re.sub(
        reg, '<img src="https://', answerRaw[step]))))[2:-5] for step in range(0, total)}
    
    return steps


def write_to_template(context):
    env = Environment(loader=FileSystemLoader('templates/'))
    temp = env.get_template('chapterQuestion.html')
    results_filename = "answers.html"


    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(temp.render(context))
        print(f'... wrote {results_filename}')
