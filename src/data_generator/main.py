import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="data_generator.server:app",
        host="0.0.0.0",
        port=8082,
        debug=True,
        reload=True,
        workers=10,
    )
