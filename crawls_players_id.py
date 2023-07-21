import requests
from bs4 import BeautifulSoup

def get_player_refs(base_url):
  """Retorna uma lista de refs de jogadores da Basketball Reference.

  Args:
    base_url: A URL da página principal da Basketball Reference.

  Returns:
    Uma lista de refs de jogadores.
  """

  response = requests.get(base_url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    refs = []
    for a in soup.find_all("a", class_="player"):
      ref = a["href"]
      refs.append(ref)
    return refs
  else:
    raise Exception("Falha na solicitação: {}".format(response.status_code))

if __name__ == "__main__":
  base_url = "https://www.basketball-reference.com/players/"
  refs = get_player_refs(base_url)
  for ref in refs:
    print(ref)
