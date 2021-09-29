import graphene
from fastapi import APIRouter
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

from endpoints.graphql.greetings_generator import Query
from endpoints.routers import post_queries, root, get_queries

main_router = APIRouter()
main_router.include_router(root.router)
main_router.include_router(get_queries.router)
main_router.include_router(post_queries.router)
main_router.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query), executor_class=AsyncioExecutor))
