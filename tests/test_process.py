import pandas as pd
from app.process import validate

def test_validation():
    df=pd.DataFrame([{
        "name":"Lamp","url":"https://example.com/p/1","price":"10"
    }])
    out=validate(df)
    assert bool(out.iloc[0]["valid"])
