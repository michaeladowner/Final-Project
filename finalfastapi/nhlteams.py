import urllib.request
import json
import pprint


def get_data_from_url(url):
    """
    Get data from a URL and handle potential errors.
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
    """Retreives information about a specified NHL team using the team's display name as an input (e.g., 'Boston Bruins')

    team_name (str): The display name of the NHL team (e.g., 'Boston Bruins').

    """

    api_url = "https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/teams"  # Assign api_url to the external ESPN API URL

    data = get_data_from_url(
        api_url
    )  # Get data from the API URL and store returned data in data

    # if data is None:
    #    print("No data retrieved from the API.")
    #    return None

    # Search through the API using loops, for the specified NHL team's information using the display name
    for sport in data["sports"]:
        for league in sport["leagues"]:
            for team in league["teams"]:
                if (
                    team["team"]["displayName"].lower() == team_name.lower()
                ):  # check if the displayName of the team matches the team_name provided by the user by being case sensitive
                    return team["team"]  # Return the team data if found

    # print(f"'{team_name}' not found in external NHL API.") #if the team name is not found in the API
    # return None


def main():
    """
    Main function to drive the program.
    Prompts the user to enter a NHL team name and stores the user input in team_name
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
