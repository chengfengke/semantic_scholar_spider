import requests
import time


def get_paper_details(paper_id):
    time.sleep(1)
    url = f"https://api.semanticscholar.org/v1/paper/{paper_id}"
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        title = data.get('title', 'No Title')
        abstract = data.get('abstract', 'No Abstract Available')
        year = data.get('year', 'No Year Provided')
        return {
            'title': title,
            'abstract': abstract,
            'year': year
        }
    else:
        print(f"Failed to retrieve data for paper ID: {paper_id}. Status code: {response.status_code}")
        return None
    
def get_citations(paper_id, year_filter=2023):
    # API URL to get citation details of a paper
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/citations"
    limit = 100
    offset = 0
    headers = {
        'Accept': 'application/json'
    }
    params = {
            'limit': limit,
            'offset': offset
        }
    response = requests.get(url, headers=headers, params=params)
    data = response.json().get('data', [])
    output_file = "citations_output.txt"
    with open(output_file, 'w', encoding='utf-8') as file:
        while(len(data)!=0):
            if response.status_code == 200:
                data = response.json().get('data', [])
                if len(data) == 0:
                    break
                else:
                    offset  += 100
                for paper in data:
                    time.sleep(1)
                    # Filtering papers based on year
                    paper_json = paper.get('citingPaper', 0)
                    paper_details  = get_paper_details(paper_json.get('paperId',[]))
                    year = paper_details["year"]
                    
                    if year >= year_filter:
                        title = paper_details["title"]
                        abstract = paper_details["abstract"]
                        print(f"Year: {year}")
                        print(f"Title: {title}")
                        print(f"Abstract: {abstract}")
                        print('-' * 80)
                        file.write(f"Year: {year}\n")
                        file.write(f"Title: {title}\n")
                        file.write(f"Abstract: {abstract}\n")
                        file.write('-' * 80 + '\n')
                headers = {
                'Accept': 'application/json'
                }
                params = {
                'limit': limit,
                'offset': offset
                }
                response = requests.get(url, headers=headers, params=params)
                data = response.json().get('data', [])
            else:
                print("Failed to retrieve citations. Status code:", response.status_code)

if __name__ == "__main__":
    # Replace this with the ID of the paper you want to query
    paper_id = input("Enter the Semantic Scholar paper ID: ")
    paper_id = "2a47759c48bf8d14d2caa54bcc4bd03c1eee6135"
    get_citations(paper_id)