from fastapi import APIRouter
from endpoints import get_queries, post_queries, root

main_router = APIRouter()
main_router.include_router(root.router)
main_router.include_router(get_queries.router)
main_router.include_router(post_queries.router)