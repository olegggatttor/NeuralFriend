from fastapi import APIRouter
from endpoints.routers import post_queries, root, get_queries

main_router = APIRouter()
main_router.include_router(root.router)
main_router.include_router(get_queries.router)
main_router.include_router(post_queries.router)