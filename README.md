### Michaela Downer Final-Project 
NHL Team Search Web Application 

## 1. Project Overview
I created a NHL Team Search Web Application using FastAPI, and the purpose of the project is to fetch and display information about a user's favorite NHL team. On the front end, the users will interact with an HTML form that prompts them to enter their favorite NHL team. On the back end, once the form is submitted, the application will use the input from the user to call the external NHL API I am using and fetch information about the team. Finally, the information will be displayed to the user using HTML. In instances where the user input is not found, an HTML page will be displayed to the user containing a "team not found" message. 
 
## 2. Usage Guidelines
Users can interact with my application by following the steps outlined below: 

# Acessing the Application:
Users can begin their interaction by navigating to the NHL search page using their web browser at the URL (http://127.0.0.1:8000/nhlteamsearch).

# Viewing the Search Form:
The application renders an HTML page from nhlteam-form.html that displays a search form prompting users to enter the name of an NHL team.

# Input Requirements:
Users are required to enter valid NHL team name as input in the text field, and will see a placeholder text that indicates the expected format i.e. Boston Bruins. The input is case-insensitive. 

# Submitting the Form:
After entering the team name, users click the “Get Info” button to submit the form. This triggers an HTTP POST request to the /nhlteaminfo endpoint with the provided team name. If a user attempts to submit the form with the input field blank, an alert will appear letting the user know that they need to enter a team name. 

# Processing the Request:
Upon submission, the application processes the request in the team_info function, retrieves the input from the form, and uses the get_team_info_by_name function from the nhlteams.py module to fetch relevant data about the specified team.

# Displaying Results:
If the Team is Found: The application displays a results page nhlteam-result.html detailing the team’s information, such as the team name, abbreviation, location, primary color, and alternate color.

If the Team is Not Found: If the specified team does not exist, the application redirects the user to a “Team Not Found” page nhlteam-not-found.html, informing them that the team could not be located and gives the user the option to navigate back to the search page.

# Handling Not Found Errors:
If a user attempt to access a non-existent URL, a custom 404 error page is displayed, providing a message saying "Sorry, Not Found! 😭".

## 3. Dependencies 
FastAPI: Used as the main framework to create my web application and provides features for my project to function. 

Uvicorn: Server for running the FastAPI application. Handles the web browser serving of my APIs and templates.

Jinja2: Templating engine used through FastAPI for rendering the HTML templates I created based on data from the back end of my application.
  
API used to fetch NHL team information: (https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/teams) 

Git/GitHub: Used to organize and keep my repository clean and exclude any unnecessary files that do not need to be committed.  

pip: Package tool used for installing Python libraries. 

CSS/HTML/JavaScript: I used these tools to enhance the user's experience when navigating my web application. For example, I used JavaScript embedded in my HTML form for enhanced usability when user's vist this page. 

## 4. Project Stucture 
My project is structed as followed: 

# Key File: 'main.py'
This file is part of the back end of my project and is the main entry point for my FastAPI application. It defines the FastAPI app, includes route handlers GET and POST for managing user requests and returning responses, and contains 404 error handling. 

# Key File: 'nhlteams.py'
This file is also part of the back end of my application, and is a separate module that contains all logic related to NHL teams. This includes retreiving data from my external API, processing the information, and providing the function, 'get_team_info_by_name' used in my FastAPI routes.

# Key Directory: 'templates'
This directory holds my HTML files used by FastAPI for rendering responses and contains the front-end of my application. Inside this directory contains the following:
    -nhlteam-form.html: The HTML form where users input an NHL team.
    -nhlteam-result.html: This HTML page is used to display the team information if the team entered by the user is sucessfully found. 
    -nhlteam-not-found.html: This HTML page returns a "team not found" message for cases where the team name entered by the user cannot be found in the NHL API. 

# Key Directory: 'css'
This directory holds a file named styles.css and contains the CSS styles used to enhance the appearance of the HTML pages. 

## 5. Acknowledgements
The cite in which I found the external API: (https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b)

The specific external API endpoint link I used in my application: (https://site.api.espn.com/apis/site/v2/sports/hockey/nhl/teams)  

I used this fastapi static file tutorial, (https://fastapi.tiangolo.com/tutorial/static-files/), to serve static files in my application. 

Image link used for the background of my application: (https://static.vecteezy.com/system/resources/previews/003/386/400/non_2x/ice-hockey-arena-background-concept-free-vector.jpg) 

I used ChatGPT to add additional features to my code. It helped in embedding JavaScript into the HTML form page to create an alert if a user tries to sumbit the form with out entering a team name to prevent accidental form submissions. It also helped to organize README.md file and create clear instructions for using my application. 

## 6. Relection 
I started this project by thinking of my hobbies and interests, and I used ChatGPT to help generate ideas of how I could create an application around these specific things. I enjoy being creative, but this project was intimidating to begin. I learned that dividing the project into manageable steps helped with organization and relieved stress over the complexity of the final project. It was essential to begin creating nhlteams.py before creating any other pages because I needed to make sure the API works. I also found that creating html pages after I created functions in main.py was much easier than trying to create the html pages before functions/routes were defined. 

One of the first challenges that I faced was creating the scope of my web application. I first was going to create a search application for all professional sport players, but I realized this to be far too complicated for my skillset. The next idea I had was to focus on the NHL and create a search tool for players in the league, but I had trouble finding an API. Finally, I found an external API URL endpoint containing information about NHL teams and decided to do a search application on the team instead of a player. In future projects, I would start by keeping the scope of the project basic and later adding more complicated elements. 

Another challenge I faced was problem solving when receiving error messages. Some of the errors I was able to fix on my own; others I needed additional clarification. Professor Zhi helped by giving suggestions and asking questions that allowed me to dig deeper to determine what the issue was, and he helped by pointing out minor errors that made the entire web application fail to run properly. Although ChatGPT lacks the human understanding of my entire application, it assisted in solving some specific error messages. For example, it helped resolve a "Method Not Allowed" error by suggesting I direct my form.html to my FASTAPI application route that handles the POST request to properly "post" the correct data. This was a minor mistake, but ChatGPT allowed me to resolve the issue much faster than I would have without it's assistance. 



 