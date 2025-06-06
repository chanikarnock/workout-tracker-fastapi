from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Request, status
from datetime import timedelta

from app.interfaces.user_controller import UserController
from app.models.req_model import RegisterUserReq, LoginUserReq, UpdateUserReq
from app.models.db.users import User
from app.routers.dependencies import Token, create_access_token, get_current_active_user


user_router = APIRouter()
ACCESS_TOKEN_EXPIRE_MINUTES = 100


@user_router.post("/register")
def register_user(request: Request, request_body: RegisterUserReq):
    result = UserController().register_user(request_body=request_body)
    return result


@user_router.post("/login")
def login(request: Request, request_body: LoginUserReq):
    user = UserController().login_user(request_body=request_body)
    if not user:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=str("User plan not found")
            )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")


@user_router.post("/logout")
def logout(request: Request, current_user: Annotated[User, Depends(get_current_active_user)]):
    return UserController().logout_user()


@user_router.post("/update")
def update_user(request: Request, current_user: Annotated[User, Depends(get_current_active_user)], request_body: UpdateUserReq):
    return UserController().update_user(user_id=current_user.id, request_body=request_body)


@user_router.delete("/delete")
def delete_user(request: Request, current_user: Annotated[User, Depends(get_current_active_user)]):
    return UserController().delete_user(user_id=current_user.id)
