import requests
import datetime
import json

def camelCaseWithUnderScore(orig):
    sub = orig.split('-')
    return '_'.join([s[0].upper() + s[1:].lower() for s in sub])


url = 'https://leetcode.com/graphql'

query = '''query questionOfToday {
	activeDailyCodingChallengeQuestion {
		date
		userStatus
		link
		question {
			acRate
			difficulty
			freqBar
			frontendQuestionId: questionFrontendId
			isFavor
			paidOnly: isPaidOnly
			status
			title
			titleSlug
			hasVideoSolution
			hasSolution
			topicTags {
				name
				id
				slug
			}
		}
	}
}
'''
r = requests.get(url, json={'query': query})
answer = json.loads(r.text)
data = answer['data']['activeDailyCodingChallengeQuestion']
number = data['question']['frontendQuestionId'] 
titleSlug = data['question']['titleSlug'] 

def updateReadmeMd(data):
    date = data['date']
    number = data['question']['frontendQuestionId'] 
    title = data['question']['title']
    myTitleSlug = number + '_' + data['question']['title'].replace(' ', '_')
    readmeLink = './Daily_Challenge/' + myTitleSlug + '.md'
    solutionLink = './Daily_Challenge/' + myTitleSlug + '.py'
    difficulty = data['question']['difficulty'] 

    table_row = f"| {date} | {number} | [{title}]({readmeLink}) | [Python]({solutionLink}) | {difficulty} |"

    Previous_Date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    previous_date_row_begin = f'| {Previous_Date} |'
    print(previous_date_row_begin)

    table_top = '''## Daily Challenges\n\n| Date       |   #  | Title                         | Solution | Difficulty |\n|------------|------| ----------------------------- | -------- | ---------- | \n'''

    readmeFilePath = '../l33tcode/README.md'
    f = open(readmeFilePath, "r+")
    readmeFileContent = f.read()
    readmeFileContent = readmeFileContent.replace(table_top + previous_date_row_begin, table_top + table_row + '\n' + previous_date_row_begin)
    f.truncate(0)
    f.seek(0)
    f.write(readmeFileContent)
    f.close()


def updateSolutionMd(data):
    number = data['question']['frontendQuestionId'] 
    title = data['question']['title']
    myTitleSlug = number + '_' + data['question']['title'].replace(' ', '_')
    readmeLink = './Daily_Challenge/' + myTitleSlug + '.md'
    solutionLink = './Daily_Challenge/' + myTitleSlug + '.py'
    
    queryJson = {
        "operationName": "questionContent",
        "query":  " query questionContent($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    content\n    mysqlSchemas\n  }\n}\n    ",
        "variables":  {"titleSlug": titleSlug},
        "titleSlug": titleSlug
    }
    r2 = requests.get(url, json=queryJson)
    answer2 = json.loads(r2.text)
    content = answer2['data']['question']['content']

    md = f'# {number}. {title}\n\n'
    has_markdownify = False
    try:
        import markdownify
        has_markdownify = True
        md += markdownify.markdownify(content, heading_style="ATX")
    except:
        md += content
        pass
    
    f = open("../l33tcode/" + readmeLink, "w")
    f.write(md)
    f.close()


def updateSolutionPy(data):
    number = data['question']['frontendQuestionId'] 
    myTitleSlug = number + '_' + data['question']['title'].replace(' ', '_')
    solutionLink = './Daily_Challenge/' + myTitleSlug + '.py'

    #query3 = {"query":"\n    query syncedCode($questionId: Int!, $lang: Int!) {\n  syncedCode(questionId: $questionId, lang: $lang) {\n    timestamp\n    code\n  }\n}\n    ","variables":{"lang":11,"questionId":number},"operationName":"syncedCode"}
    #r3  = requests.get(url, json=query3)
    #content = answer['data']['syncedCode']['code']

    f = open("../l33tcode/" + solutionLink, "w")
    f.write("")
    f.close()


updateReadmeMd(data)
updateSolutionMd(data)
updateSolutionPy(data)

