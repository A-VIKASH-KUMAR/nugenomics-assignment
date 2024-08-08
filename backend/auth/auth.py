from fastapi import APIRouter,  HTTPException
from datetime import datetime, timedelta, timezone
from pymongo import MongoClient
import os
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt
from dotenv import load_dotenv
from bson import json_util

def parse_json(data):
    return json_util.loads(json_util.dumps(data))

load_dotenv()
auth_router = APIRouter(prefix="/auth",responses={404: {"description": "Not found"}})

SECRET_KEY = os.environ.get("JWT_SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

mongo_connect_string = os.environ.get("MONGODB_URL")
mongo_client = MongoClient(mongo_connect_string)
db = mongo_client["nugen_auth"]
users_collection = db["users"]

class User(BaseModel):
   first_name:str
   last_name:str
   email:str
   password:str
   dob:str

class Login(BaseModel):
   email:str
   password:str

class resetPassword(BaseModel):
   email:str
   password:str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserInDB(User):
    hashed_password: str

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
    
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=120)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@auth_router.post("/register")
async def register(user:User):
    try:
     user_exists = users_collection.find_one({"email":user.email})
     if user_exists:
        raise HTTPException(status_code=409, detail="Email already registered")
     else:
        hashed_password = get_password_hash(user.password)
        del user.password
        user_collection_update = users_collection.update_one({"email":user.email},{"$set":dict(user, password=hashed_password)}, upsert=True) 
        print("user create", user_collection_update)
        return {"message":"successfully registered user"}, 200
    except Exception as error:
        print("error occoured to register user", error)
        return {"error":"error occoured to register user"}, 500
    
@auth_router.post("/login")
async def login(user_login_details:Login):
   try:
      user_exists = users_collection.find_one({"email":user_login_details.email})

      if user_exists is None: 
        return {"error":"no user found for the email address please register"}, 404
      del user_exists["_id"]
      
      verify_hashed_password = verify_password(user_login_details.password, user_exists.get("password"))
      
      if verify_hashed_password:
         access_token = create_access_token(user_exists)
      else: return {"message":"password did not match"}, 403

      return {"message":"successfully logged in user", "token":access_token}, 200
   except Exception as error:
      print("error occoured to login user", error)
      return {"error":"error occoured to login user"}, 500
   
@auth_router.post("/reset-password")
def reset_password(resetPassword:resetPassword):
   try:
      user_exists = users_collection.find_one({"email":resetPassword.email})

      if user_exists is None: 
        return {"error":"no user found for the email address please register"}, 404
      del user_exists["_id"]
      
      hashed_password =  get_password_hash(resetPassword.password)
      update_user_password = users_collection.update_one({"email":resetPassword.email}, {"$set":{"password":hashed_password}})
      print("update password", update_user_password)
      return {"successfully updated user password"}, 201
   except Exception as error:
      print("error occoured to reset password", error)
      return {"error":"error occoured to reset password"}, 500