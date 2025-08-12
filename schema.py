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
    predicted_Outcome : int = Field(..., 
                                      description= "Predicted outcome: 0 = No diabetes, 1 = Diabetes",
                                      ge=0, le=1, example=[0,1])
    

    # Age pregnancies  glucose  BloodPrerssure  insulin BMI DiabetesPedigreeFunction SkinThickness
# create the model request object
class ModelRequest(BaseModel):
    """
    creates the request object for the model prediction
    """
    Pregnancies: int = Field(...,
                             description="Number of times the client has been pregnant.",
                             example=2)
    Glucose: int = Field(..., description="glucose concentration in mg/dL",
                                          example=110)
    BloodPressure: int = Field(...,  description="Diastolic blood pressure in mm Hg",
                                                example=92)
    SkinThickness: int = Field(...,
                               description="Triceps skinfold thickness in millimeters, used as a measure of body fat.",
                               example=23)
    Insulin: int = Field(..., description="serum insulin in mL",
                              example=94)
    BMI: float = Field(..., description="bmi of the client",
                     gt=5, lt=100, example=35.4)  
    DiabetesPedigreeFunction: float = Field(...,
                                            description="A continuous measure of the patient's genetic predisposition to diabetes.",
                                            example=0.627)
    Age: int = Field(..., description="Age of the client",
                     gt=5, lt=100, example=45)
    
    
    
    