import urllib.request
import json
import pprint


def get_data_from_url(url):
    """
    This function attempts to get data from the provided URL and handles potential errors.
    """
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8")
            data = json.loads(response_text)
        return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ValueError(f"Data not found for the given URL: {url}")
        else:
            raise RuntimeError(f"HTTP Error occurred: {e.code}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Failed to reach the server: {e.reason}")
    except json.JSONDecodeError:
        raise ValueError("Failed to parse JSON response.")


def get_team_info_by_name(team_name):
    """
    Retrieve information about a specified NHL team.

    This function fetches data from the ESPN API and searches for the team
    information based on the provided display name from the user.

    Key Argument:
        team_name (str): The display name of the NHL team (e.g., 'Boston Bruins').

    Returns:
        dict: A dictionary containing the team's information, or None if not found.
    """

    api_url = "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/teams"  # Assign api_url to the external ESPN API URL

    # Get data from the API URL and store returned data in data
    data = get_data_from_url(api_url)

    # Search through the API response for the specified NHL team's information using the display name
    for sport in data["sports"]:
        for league in sport["leagues"]:
            for team in league["teams"]:
                if team["team"]["displayName"].lower() == team_name.lower():
                    return team["team"]  # Return the team data if found


def main():
    """
    Main function to drive the program.

    This function prompts the user to enter an NHL team name and retrieves
    information about the specified team. It then displays the team's name,
    abbreviation, location, and colors if the information is found.

    The user is prompted to input the team name, which is then passed to
    the `get_team_info_by_name` function to retrieve the data.

    Returns:
        None
    """
    team_name = input("Enter a NHL team (e.g., 'Boston Bruins'):")
    team_info = get_team_info_by_name(team_name)  # return information about the team

    # If the team_info is not empty and contains data, print out retrieved information about the team
    if team_info:
        print(f"Team Name: {team_info['displayName']}")
        print(f"Abbreviation: {team_info['abbreviation']}")
        print(f"Location: {team_info['location']}")
        print(f"Primary Color: {team_info['color']}")
        print(f"Alternate Color: {team_info['alternateColor']}")


if __name__ == "__main__":
    main()
