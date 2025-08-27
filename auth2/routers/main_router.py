from fastapi import APIRouter

from auth2.routers import login, signup, logout, me, refresh

router = APIRouter(prefix="auth/v1")

router.include_router(login)
router.include_router(logout)
router.include_router(me)
router.include_router(refresh)
router.include_router(signup)
