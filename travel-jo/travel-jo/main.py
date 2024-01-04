# main.py

from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.security import OAuth2PasswordBearer
from models import Hotel, User
from fastapi.middleware.cors import CORSMiddleware
import pyrebase

config = {
  "apiKey": "AIzaSyCtTTzzAjIee0eNUPYYKCCQciN95cm-KtQ",
  "authDomain": "graduproject-736aa.firebaseapp.com",
  "databaseURL": "https://graduproject-736aa-default-rtdb.firebaseio.com",
  "storageBucket": "graduproject-736aa.appspot.com",
  "serviceAccount": "graduproject-736aa-firebase-adminsdk-sd1if-1783d25148.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
auth = firebase.auth()

origins = [
    "http://localhost:3000",  # Update with your frontend's origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Adjust based on your requirements
    allow_headers=["*"],  # Adjust based on your requirements
)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        user = auth.verify_id_token(token)
        return user
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/signup")
async def signup(user: User):
    try:
        if len(user.password) < 6:
            raise HTTPException(status_code=400, detail="Password must be at least 6 characters long")
        
        user_info = auth.create_user_with_email_and_password(user.email, user.password)
        # You can save additional user information to your database here
        # For example, use Firebase Realtime Database to store user details
        user_data = {
            "full_name": user.full_name,
            "email": user.email,
            "phone_number": user.phone_number,
            "national_id": user.national_id
        }
        db.child("users").child(user_info["localId"]).set(user_data)

        return {"user_id": user_info["localId"]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to create user: {e.detail}")

@app.post("/login")
async def login(email: str, password: str):
    try:
        user_info = auth.sign_in_with_email_and_password(email, password)
        if user_info['localId']:
            return user_info
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
            
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid credentials")


def get_places():
    try:
        response = []
        places = db.child("places").get()
        for place in places.each():
            place_info = {"id": place.key(), **place.val()}
            response.append(place_info)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving places: {e}")

@app.get("/places")
async def read_places():
    return get_places()


def search_places_by_name(name_query: str = Query(..., description="Search query for place names")):
    try:
        # Query places by the "name" field
        places_query = db.child("places").order_by_child("title").start_at(name_query).get()
        
        # Extract results
        places = []
        for place in places_query.each():
            place_info = {"id": place.key(), **place.val()}
            if place_info["title"].lower().find(name_query.lower()) != -1:
                places.append(place_info)

        return places
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error searching places: {e}")

@app.get("/places/search", response_model=list)
async def search_places(name_query: str = Depends(search_places_by_name)):
    return name_query

@app.get("/hotels/", response_model=list[Hotel])
async def get_all_hotels():
    return hotels_db

@app.get("/hotels/{hotel_id}", response_model=Hotel)
async def get_hotel(hotel_id: int):
    hotel = next((h for h in hotels_db if h["id"] == hotel_id), None)
    if hotel:
        return hotel
    raise HTTPException(status_code=404, detail="Hotel not found")