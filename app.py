if not os.path.exists("final_model.h5"):
    url = "https://drive.google.com/uc?id=1kjLDHmw4kU8385zQ8ZOllAIX1XDm6GTP"
    gdown.download(url, "final_model.h5", quiet=False)

model = load_model("final_model.h5", compile=False)




