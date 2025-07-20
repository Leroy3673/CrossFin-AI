# FastAPI Modules
from fastapi import HTTPException, Request

# Clerk authentication modules
from clerk_backend_api import Clerk, AuthenticateRequestOptions

# Environment variables
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Clerk with the secret key
clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))


# Middleware to authenticate requests using Clerk
def authenticate_and_get_user_details(request: Request):
    try:
        request_state = clerk_sdk.authenticate_request(
            request,
            AuthenticateRequestOptions(
                authorized_parties=["http://localhost:3000"], 
                jwt_key=os.getenv("JWT_KEY")
            )
        )

        if not request_state.is_signed_in:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized: User not signed in"
            )

        user_id = request_state.payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Unauthorized: User ID not found in token"
            )

        return {"user_id": user_id}

    except HTTPException:
        raise  # Re-raise expected HTTPExceptions
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Authentication error: {str(e)}"
        )
