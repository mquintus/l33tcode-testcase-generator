import requests
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

print(r.status_code)
print(r.text)
import json
answer = json.loads(r.text)
print(answer['data']['activeDailyCodingChallengeQuestion'])

data = answer['data']['activeDailyCodingChallengeQuestion']

def camelCaseWithUnderScore(orig):
    sub = orig.split('-')
    return '_'.join([s[0].upper() + s[1:].lower() for s in sub])

def updateReadmeMd(data):
    date = data['date']
    number = data['question']['frontendQuestionId'] 
    title = data['question']['title']
    myTitleSlug = number + '_' + data['question']['title'].replace(' ', '_')
    readmeLink = './Daily_Challenge/' + myTitleSlug + '.md'
    solutionLink = './Daily_Challenge/' + myTitleSlug + '.py'
    difficulty = data['question']['difficulty'] 

    table_row = f"| {date} | {number} | [{title}]({readmeLink}) | [Python]({solutionLink}) | {difficulty} |"

    import datetime
    Previous_Date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

    previous_date_row_begin = f'| {Previous_Date} |'

    table_top = '''## Daily Challenges\n\n| Date       |   #  | Title                         | Solution | Difficulty |\n|------------|------| ----------------------------- | -------- | ---------- | \n'''

    readmeFilePath = '../l33tcode/README.md'
    f = open(readmeFilePath, "r+")
    readmeFileContent = f.read().replace('\r', '')
    readmeFileContent = readmeFileContent.replace(table_top + previous_date_row_begin, table_top + table_row + '\n' + previous_date_row_begin)
    f.truncate(0)
    f.seek(0)
    f.write(readmeFileContent)
    f.close()

updateReadmeMd(data)

