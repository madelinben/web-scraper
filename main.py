import pprint, requests
from bs4 import BeautifulSoup

url = "http://www.madelinben.co.uk/"
data = requests.get(url)

# pprint.pprint(data.content)

soup = BeautifulSoup(data.content, "html.parser") # "html.parser" // "html5lib"

""" src = "index.html"
with open(src) as f:
    soup = BeautifulSoup(f, "html.parser") """



# FIND ELEMENTS BY ID
projectSection = soup.find(id="project-container")
# print(projectSection.prettify())

# FIND ELEMENTS BY CLASS NAME
projectList = projectSection.find_all('div', class_="project-content")

for projectContent in projectList:
    # print(projectContent, end="\n"*2)

    projectTitle = projectContent.find("h2", class_="project-title").text
    projectDesc = projectContent.find("p", class_="project-desc").text

    projectLink = projectContent.find("a", string=lambda text: "git" in text.lower())
    projectSrc = projectLink["href"].strip()

    if None in (projectTitle, projectDesc, projectLink):
        continue

    print(f"title= {projectTitle}\ndesc= {projectDesc}\nsrc= {projectSrc}\n")