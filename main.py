from importlib.resources import read_text
from jinja2 import Environment, FileSystemLoader, BaseLoader

import cheinsteinpy
import json
import re

with open("config.json", "r") as f:
    config = json.load(f)

with open("cookie.txt", 'r') as f:
    cookieTxt = f.read()

# env = Environment(loader=FileSystemLoader('templates/'))
# temp = env.get_template('chapterQuestion.html')
# results_filename = "steps.html"
# # url = 'https://www.chegg.com/homework-help/refer-example-1-find-equation-tangent-line-curve-y-1-t-paral-chapter-c-problem-2e-solution-9781133112280-exc'
# url = 'https://www.chegg.com/homework-help/a-brief-introduction-to-criminal-law-2nd-edition-chapter-2-problem-19pt-solution-9781284056112'
# answerRaw = cheinsteinpy.answer(url, cookieTxt, config['userAgent'])
# questionRaw = cheinsteinpy.question(url, cookieTxt, config['userAgent'])
# total = len(answerRaw)
reg = '(https?://+)'
# steps = {step + 1: str(re.subn('png', 'png">', str(re.sub(
#     reg, '<img src="https://', answerRaw[step]))))[2:-5] for step in range(0, total)}
# print(steps)

myStr = 'When https://media.cheggcdn.com/study/50d/50d35c53-975e-4469-8d96-7642946680ee/5077-C-2E-i9.png, https://media.cheggcdn.com/study/35b/35b789f5-873b-4ca9-9ca3-b783aeb3f085/5077-C-2E-i10.png respectively. So, the points where the tangents to the curve https://media.cheggcdn.com/study/6a6/6a66e7f8-7707-40a1-9411-606e07c21c85/5077-C-2E-i11.png are parallel to AD are https://media.cheggcdn.com/study/d3c/d3c5ac1a-eecf-4112-9f3b-0cdc95cf1ca3/5077-C-2E-i12.png and https://media.cheggcdn.com/study/cad/cad909ba-fbce-48c5-8f85-0f95ec9dce3b/5077-C-2E-i13.png Using slope-point form to write the equations of the tangent lines at these points while the slope is https://media.cheggcdn.com/study/8c7/8c751618-57de-4108-baa5-0452ffd28bcf/5077-C-2E-i14.png. https://media.cheggcdn.com/study/43d/43d7333c-bdce-49ed-8cbe-117ae3e40eef/5077-C-2E-i15.png https://media.cheggcdn.com/study/c96/c96c3805-873b-4064-a643-d88edbc1ef18/5077-C-2E-i16.png'
# # images = re.findall("(?P<url>https?://[^\s]+)", myStr)
# mystr = 'ksdjskdsj'
# x = re.sub(reg,'<img src="https://',mytr)
# print(x)
x = re.sub(reg, '<img src="https://', myStr)
y = re.subn('png', 'png">', str(x))
print(str(y)[2:-5])
# for s in steps:
#     images = re.findall("(?P<url>https?://[^\s]+)", str(steps[s]))
#     images_dict = {step+1: images[step] for step in range(len(images))}

# embed = '<img src="https://media.cheggcdn.com/study/50d/50d35c53-975e-4469-8d96-7642946680ee/5077-C-2E-i9.png">'

# context = {
#     'problemTitle': questionRaw,
#     'steps': steps,
#     'totalSteps': total,
# }
# with open(results_filename, mode="w", encoding="utf-8") as results:
#     results.write(temp.render(context))
#     print(f'... wrote {results_filename}')
