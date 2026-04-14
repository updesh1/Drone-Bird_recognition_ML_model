import os
import gdown

if not os.path.exists("best_model.h5"):
    url = "https://drive.google.com/uc?id=1mmDg2CZ2b4rlNdmFulpFRkHXCL9n_9mo"
    gdown.download(url, "best_model.h5", quiet=False)


