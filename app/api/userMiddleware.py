from fastapi import Request, HTTPException 
from jose import jwt, JWTError

SECRET_KEY ="Hello"
ALGORITHM = 'HS256'

async def userMiddleware(request : Request):
    print('inside middle')
    token = request.headers.get('authorization')
    if not token :
        raise HTTPException(status_code=401, detail="Token not provided")
    
    try :
         isValidToken = jwt.decode(token, SECRET_KEY, ALGORITHM)
         if not isValidToken :
           raise HTTPException(status_code=401, detail="Not a valid token")
    
         role = isValidToken["role"]
         if not role == "user":
           raise HTTPException(status_code=401, detail="Invalid role")
    
         request.state.user = isValidToken
         return None
    except JWTError as err1 :
       raise HTTPException(status_code=401, detail="error in decoding the token")
    
    except Exception as err2 :
       raise HTTPException(status_code=500, detail="something went wrong")
    