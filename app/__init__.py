
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("__init__:app", host="0.0.0.0", port=5000)