"""
Engeto_Python_project_3: Elections scraper
author = Martin Kucirek
email = martin.kucirek89@gmail.com
Discord = Martin K.#3205
"""


import csv
import requests
import sys
from bs4 import BeautifulSoup

# Funkce pro zobrazení průběhu stahování dat v procentech
def print_progress(percent_done):
    print(f"Stahování dat: {percent_done:.2f}%", end='\r')
    sys.stdout.flush()

def election_scraper(argv: str):
    """
    Hlavní funkce pro web scraping.
    """
    url_to_scrape, file_name = check_input_arguments(argv)
    urls, partial_dict_1 = get_urls_codes_names(url_to_scrape)
    partial_dict_2 = get_votes_envelopes(urls, partial_dict_1)
    election_results_dict = get_parties_votes(urls, partial_dict_2)
    save_to_csv(file_name, election_results_dict)


def check_input_arguments(argv: str) -> (str, str):
    """
    Kontrola správnosti vstupních argumentů.
    """
    if len(argv) != 2:
        print("ŠPATNÁ VSTUPNÍ DATA")
        sys.exit()

    url = str(argv[0])
    file_name = str(argv[1])

    if not url.startswith('https://volby.cz/pls/ps2017nss'):
        print("ŠPATNÁ URL")
        sys.exit()

    response_check = check_if_website_exists(url)
    if response_check is False:
        print("ŠPATNÁ URL")
        sys.exit()
    elif not file_name.endswith('.csv'):
        print("ŠPATNÝ TYP SOUBORU")
        sys.exit()
    else:
        print(f"STAHUJI DATA Z VYBRANÉHO URL: {url}")
        return url, file_name


def check_if_website_exists(url: str) -> bool:
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False


def get_urls_codes_names(url: str) -> (list, list):
    """
    Procházení tagů tr a získání seznamu slovníků obsahujících kód a název každé obce.
    Získání seznamu URL výsledků voleb.
    """
    election_results_partial = []
    urls = []
    root = "https://volby.cz/pls/ps2017nss/"
    parsed_html = BeautifulSoup(requests.get(url).text, features="html.parser")
    tr_tags = parsed_html.find_all('tr')

    for tr_tag in tr_tags:
        code_and_name_row = dict()
        code = tr_tag.find('td', {'class': 'cislo'})
        for number in range(1, 4):
            name = tr_tag.find('td', {'headers': f't{number}sa1 t{number}sb2'}) or tr_tag.find('td', {'headers': 's3'})
            if code and name is not None:
                code_and_name_row["code"] = code.text
                code_and_name_row["name"] = name.text
                election_results_partial.append(code_and_name_row)
                urls.append(root + code.find('a')['href'])
                break
    return urls, election_results_partial


def get_votes_envelopes(urls: list, election_results_partial: list) -> list:
    """
    Procházení URL každé obce. Hledání tagů td a přidávání informací o volbách do seznamu slovníků.
    """
    for index, code_and_name in enumerate(election_results_partial):
        url = urls[index]
        parsed_html = BeautifulSoup(requests.get(url).text, features="html.parser")
        code_and_name["registered"] = parsed_html.find("td", {"headers": "sa2"}).text.replace("\xa0", "")
        code_and_name["envelopes"] = parsed_html.find("td", {"headers": "sa5"}).text.replace("\xa0", "")
        code_and_name["valid"] = parsed_html.find("td", {"headers": "sa6"}).text.replace("\xa0", "")
        
        # Výpis procentuálního průběhu
        percent_done = (index + 1) / len(election_results_partial) * 100
        print_progress(percent_done)

    return election_results_partial


def get_parties_votes(urls: list, election_results: list) -> list:
    """
    Procházení URL každé obce. Hledání tagů td a přidávání názvů volebních stran a počtu hlasů do seznamu slovníků.
    """
    for index, row_dict in enumerate(election_results):
        url = urls[index]
        parsed_html = BeautifulSoup(requests.get(url).text, features="html.parser")
        div_tags = parsed_html.find("div", {"id": "inner"})
        tr_tags = div_tags.find_all("tr")
        for tr_tag in tr_tags:
            party_name = tr_tag.find("td", {"class": "overflow_name"})
            for number in range(1, 4):
                party_votes = tr_tag.find("td", {"headers": f"t{number}sa2 t{number}sb3"})
                if party_name is not None and party_votes is not None:
                    row_dict[party_name.text] = party_votes.text.replace("\xa0", "")
                    break
    return election_results


def save_to_csv(file_name: str, election_results: list):
    """
    Uložení načtených dat do souboru CSV.
    """
    with open(file_name, 'w', encoding="utf-8-sig", newline="") as elections_file:
        fieldnames = election_results[0].keys()
        writer = csv.DictWriter(elections_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(election_results)
        print(f"UKLÁDÁM DO SOUBORU: {file_name}",
              "UKONČUJI PROGRAM",
              sep="\n")


if __name__ == "__main__":
    election_scraper(sys.argv[1:])
