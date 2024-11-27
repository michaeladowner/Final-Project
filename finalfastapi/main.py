from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from nhlteams import get_team_info_by_name
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/nhlteamsearch", response_class=HTMLResponse)
async def searchpage(request: Request):
    """
    Show the form to input an NHL team name to the user.

    This function returns the NHL team search form page where users can
    enter the name of their favorite NHL team.

    Key Argument:
        request (Request): The HTTP request that is sent to the server.

    Returns:
        HTMLResponse: The rendered HTMl page for the team search form.
    """
    return templates.TemplateResponse("nhlteam-form.html", {"request": request})


@app.post("/nhlteaminfo", response_class=HTMLResponse)
async def team_info(request: Request):
    """
    Process the NHL team information request.

    This function retrieves the data submitted from the NHL team search form,
    fetches team information based on the team name entered by the user, and
    renders the correct template based on the search result.

    Key Argument:
        request (Request): The request that is sent to the server containing the data from the team search form

    Returns:
        HTMLResponse:
            - The rendered HTML page displaying the team information if the team is found.
            - The rendered HTML page displaying team not found message if no matching team is found.
    """
    # Get the data from the form
    form = await request.form()
    team_name = form.get("team_name")
    print(team_name)

    # Get the team information by calling the function get_team_info_by_name from nhlteams.py
    team_info = get_team_info_by_name(team_name)
    print(team_info)

    # if the NHL team entered by the user is found, display the team information
    if team_info:
        return templates.TemplateResponse(
            "nhlteam-result.html",
            {
                "request": request,
                "team_name": team_info["displayName"],
                "abbreviation": team_info["abbreviation"],
                "location": team_info["location"],
                "primary_color": team_info["color"],
                "alternate_color": team_info["alternateColor"],
            },
        )
    else:
        return templates.TemplateResponse(
            "nhlteam-not-found.html",
            {"request": request, "team_name": team_name},
        )


@app.exception_handler(404)
def custom_404(request, e):
    """
    Custom 404 page to handle 404 Not Found errors.

    This function runs when a user tries to access a page
    that does not exist. It returns a HTML response message saying the
    page was not found.

    Key Arguments:
        request: The request that caused the 404 error.
        e: The 404 error that occured.

    Returns:
        HTMLResponse: A HTML response with a message saying "Sorry, Not Found! 😭".
    """
    return HTMLResponse("Sorry, Not Found! 😭")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
