from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# from predictors.ngcf_predictor import ngcf_predictor
from predictors.kprn_predictor import kprn_predictor
from predictors.sasrec_predictor import sasrec_predictor
from utils.download_models import ModelDownloader

from utils.log_config import logger

app = FastAPI()


class SasrecRequest(BaseModel):
    movie_ids: List[int] = [1, 2, 3, 4]

class KPRNRequest(BaseModel):
    movie_ids: List[int] = [1, 2, 3, 4]

class NGCFRequest(BaseModel):
    movie_ids: List[int] = [1, 2, 3, 4]


@app.post("/sasrec/")
async def read_item(sasrec_request: SasrecRequest):
    logger.info(f"sasrec_request : {sasrec_request}")
    try:
        sasrec_recomm_mids = sasrec_predictor.predict(sasrec_request.movie_ids)
        sasrec_recomm_mids = [int(mid) for mid in sasrec_recomm_mids]  # numpy.int64 타입을 Python의 int 타입으로 변환
        logger.info(f"sasrec_recomm_mids : {sasrec_recomm_mids}")
        return {"sasrec_recomm_mids": sasrec_recomm_mids}
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/kprn/")
async def read_item(kprn_request: KPRNRequest):
    logger.info(f"kprn_request : {kprn_request}")
    try:
        kprn_recomm_mids = kprn_predictor.predict(kprn_request.movie_ids)
        kprn_recomm_mids = [int(mid) for mid in kprn_recomm_mids]  # numpy.int64 타입을 Python의 int 타입으로 변환
        logger.info(f"kprn_recomm_mids : {kprn_recomm_mids}")
        return {"kprn_recomm_mids": kprn_recomm_mids}
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# @app.post("/ngcf/")
# async def read_item(ngcf_request: NGCFRequest):
#     logger.info(f"ngcf_request : {ngcf_request}")
#     try:
#         ngcf_recomm_mids = ngcf_predictor.predict(ngcf_request.movie_ids)
#         ngcf_recomm_mids = [int(mid) for mid in ngcf_recomm_mids]  # numpy.int64 타입을 Python의 int 타입으로 변환
#         logger.info(f"ngcf_recomm_mids : {ngcf_recomm_mids}")
#         return {"ngcf_recomm_mids": ngcf_recomm_mids}
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    model_downloader = ModelDownloader()
    model_downloader.download_sasrec_model()
    uvicorn.run(app, host="127.0.0.1", port=7001)
