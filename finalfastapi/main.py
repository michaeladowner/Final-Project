from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from nhlteams import get_team_info_by_name
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")


"""
Get NHL team information through HTML Form page and display information to users through HTML Result page 

"""

# Display the form when users visit the search page via /nhlteamsearch
@app.get("/nhlteamsearch", response_class=HTMLResponse)
async def searchpage(request: Request):
    # Return nhlteam-form.html stored in templates 
    return templates.TemplateResponse("nhlteam-form.html", {"request": request})


@app.post("/nhlteaminfo", response_class=HTMLResponse)
async def team_info(request: Request):
    # Get the data from the form
    form = await request.form()
    team_name = form.get("team_name")
    print(team_name)

    # Get the team information by calling the function get_team_info_by_name
    team_info = get_team_info_by_name(team_name)
    print(team_info) 

    # if the NHL team entered by the user is found, display the team information in the template 'nhlteam-result.html'
    if team_info:
        return templates.TemplateResponse(
            "nhlteam-result.html",
            {
                "request": request,
                "team_name": team_info["displayName"],
                "abbreviation": team_info["abbreviation"],
                "location": team_info["location"],
                "primary color": team_info["color"],
                "alternate_color": team_info["alternateColor"],
            },
        )


"""
Custom 404 page
"""
@app.exception_handler(404)
def custom_404(request, e):
    return HTMLResponse("Sorry, Not Found! 😭")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
