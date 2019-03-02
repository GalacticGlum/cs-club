import urllib.request, urllib.parse
import argparse
import json

parser = argparse.ArgumentParser(description='Calculate the final scores for the SLPR contests.')
parser.add_argument('-c', '--contests', type=str, nargs='+', required=True, help='A contest code')
parser.add_argument('-w', '--weights', type=float, nargs='+', required=True, help='The weight for each contest')
parser.add_argument('-d', '--domain', type=str, default='https://ssoj.ca/', help='The base domain.')
parser.add_argument('-api', '--apiurl', type=str, default='/api/contest/info/', help='The API URL for contests.')
parser.add_argument('-rhtml', '--rankinghtmlurl', type=str, default='/contest/{0}/ranking', help='The URL for the ranking HTML; compatible with string formatting, "{0}" is the contest code.')
parser.add_argument('-rname', '--rankingjsonname', type=str, default='rankings', help='The JSON field name for the rankings in the contest API JSON object.')
parser.add_argument('-tlname', '--timelimitjsonname', type=str, default='time_limit', help='The JSON field name for the time limit in the contest API JSON object.')
args = parser.parse_args()

def get_contest_scores(contest_code):
    scores = {}

    api_resource_path = urllib.parse.urljoin(urllib.parse.urljoin(args.domain, args.apiurl), contest_code)
    with urllib.request.urlopen(api_resource_path) as json_url:
        data = json.loads(json_url.read().decode())
        rankings = data[args.rankingjsonname]

        html_resource_path = urllib.parse.urljoin(args.domain, args.rankinghtmlurl.format(contest_code))
        problem_count = 0
        with urllib.request.urlopen(html_resource_path) as html_url:
            html_data = html_url.read().decode()
            problem_count = html_data.count('class="points header"')

        max_cumtime = (data[args.timelimitjsonname] * problem_count) / 60
        max_score = max(rankings, key=lambda x: x['points'])['points']
        max_distance = (max_score**2 + max_cumtime**2)**0.5

        for ranking in rankings:
            distance = ((ranking['points'] - max_score)**2 + (ranking['cumtime'] / 60)**2)**0.5
            score = 1 - distance / max_distance
            scores[ranking['user']] = score
            
        return scores

if len(args.contests) != len(args.weights):
    print('There must be the same number of weights defined as contest codes.')
    exit(1)

user_scores = {}
for i in range(len(args.contests)):
    contest = args.contests[i]

    scores = get_contest_scores(contest)
    for user in scores:
        if user not in user_scores:
            user_scores[user] = []
        
        user_scores[user].append((i, scores[user]))

final_scores = {}
for user in user_scores:
    final_scores[user] = 100 * sum(args.weights[entry[0]] * entry[1] for entry in user_scores[user])

final_rankings = sorted(final_scores, key=final_scores.get, reverse=True)