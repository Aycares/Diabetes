from pydantic import BaseModel,Field
from typing import Literal


# create a root response object
class RootResponse(BaseModel):
    """creates the payload for the root endpoint."""
    message: str = Field(..., description="root message",
                         examples=["we are live!"])
    

# create a model response object
class ModelResponse(BaseModel):
    """
    creates a response object for the model prediction.
    """
    predicted_diabetes : float = Field(..., 
                                      description= "The model's predicted diabetes",
                                      gt= 0, examples=[55.3, 44.2])
    

    # Age pregnancies  glucose  BloodPrerssure  insulin BMI Diabetes
# create the model request object
class ModelRequest(BaseModel):
    """
    creates the request object for the model prediction
    """
    age: int = Field(..., description="Age of the client",
                     gt=5, lt=100, examples=[35])
    BMI: float = Field(..., description="bmi of the client",
                     gt=5, lt=100, examples=[35.4])  
    
    Diabetes: Literal['No','Yes'] = Field(..., description="indicates if the client has diabetes (No) or (Yes)",
                                           examples=["No","Yes"])
    Glucose: Literal['No', 'Yes'] = Field(..., 
                                          description="Indicates if the client's glucose level is normal (No) or high (Yes)",
                                          examples=["No", "Yes"])
    BloodPressure: Literal['Yes', 'No'] = Field(..., 
                                                description="Indicates if the client has high blood pressure (Yes) or (No)",
                                                examples=["Yes", "No"])
    Insulin: Literal['Normal', 'High', 'Low'] = Field(..., 
                                                      description="Indicates the insulin level status of the client",
                                                      examples=["Normal", "High"])
    Pregnancies: Literal['Yes', 'No'] = Field(..., 
                                              description="Indicates whether the client has ever been pregnant (Yes or No)",
                                              examples=["Yes", "No"])