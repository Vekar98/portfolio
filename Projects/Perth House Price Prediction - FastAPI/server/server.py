from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import util

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get('/get_location_names')
def get_location_names():
    return {'locations': util.get_location_names()}

@app.post('/predict_home_price')
async def predict_home_price(
    location: str = Form(...),
    bedrooms: int = Form(...),
    bathrooms: int = Form(...),
    garage: int = Form(...),
    land_area: int = Form(...),
    floor_area: int = Form(...),
    build_year: int = Form(...),
):
    estimated_price = util.get_estimated_price(location, bedrooms, bathrooms, garage, land_area, floor_area, build_year)
    return {'estimated_price': estimated_price}

if __name__ == "__main__":
    print("Starting Python FastAPI Server For Home Price Prediction")
    util.load_saved_artifacts()
