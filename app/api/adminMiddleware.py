from fastapi import Request,HTTPException
from jose import jwt, JWTError

SECRET_KEY ="Hello"
ALGORITHM = 'HS256'

async def adminMiddleware(request : Request):
    token = request.headers.get('authorization')
    if not token :
        raise HTTPException(status_code=401, detail="user is not authorized")
    
    try :
       isValidToken = jwt.decode(token,SECRET_KEY,ALGORITHM)

       if not isValidToken :
        raise HTTPException(status_code=401, detail="Not authorized")
    
       role = isValidToken["role"]
       if not role == "admin" :
        raise HTTPException(status_code=401, detail="Not authorized to perform this action")
    
       request.state.user = isValidToken
       return None
    except JWTError as err :
       raise HTTPException(status_code=401, detail="Error in decoding the token")
    except  Exception :
      raise HTTPException(status_code=500, detail="Something went wrong")