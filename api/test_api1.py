from fastapi import FastAPI
import uvicorn 
import os 

app = FastAPI()

@app.get("/test1")
def test1():
    return {"message": "hi helo"}



if __name__ == "__main__":
    module_name = os.path.basename(__file__).split(".")[0]
    print(f"{module_name} is current program")

    # uvicorn_config = {
    #     "host": "127.0.0.1",
    #     "port": 8000,
    #     "reload": True
    # }
    # uvicorn.run("test_api1:app",**uvicorn_config)

    # uvicorn_config = {
    #     "host": "127.0.0.1",
    #     "port": 8000,
    #     "reload": True
    # }    
    
    # uvicorn.run("test_api1:app",**uvicorn_config)
    # uvicorn.run(app, host: "127.0.0.1", port: 8000, reload: True ) 
    # uvicorn.run("test_api1:app", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run(f"{module_name}:app", host="127.0.0.1", port=8000, reload=True)

