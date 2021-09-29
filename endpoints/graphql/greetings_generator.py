import random

from graphene import ObjectType, List, Int, Field
from endpoints.graphql.schemas.greeting_schema import Greeting
from endpoints.methods.model_instance import predictor

prefixes = ["Hello!", "Hey!", "Hi!", "Hola!"]


class Query(ObjectType):
    greetings_list = None
    greetings = Field(List(Greeting), users=List(Int, required=True))

    async def resolve_greetings(self, info, users):
        answer = []
        for user in users:
            answer.append({
                "user": user,
                "title": "kek",
                "prediction": {
                    "prefix": prefixes[random.randint(0, len(prefixes) - 1)],
                    "predicted_value": predictor.predict(user)
                }
            })
        return answer
