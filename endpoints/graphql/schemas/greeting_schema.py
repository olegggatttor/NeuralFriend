from graphene import String, ObjectType, Int, Field


class Prediction(ObjectType):
    prefix = String()
    predicted_value = String()


class Greeting(ObjectType):
    user = Int()
    title = String()
    prediction = Field(Prediction)
