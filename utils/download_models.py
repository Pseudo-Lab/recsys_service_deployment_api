import os

import boto3
from dotenv import load_dotenv

load_dotenv('.env.dev')


class ModelDownloader:
    def __init__(self):
        self.kprn_location = 'pytorch_models/kprn/kprn.pt'
        self.kprn_dir = 'pytorch_models/kprn'
        self.sasrec_location = 'pytorch_models/sasrec/sasrec.pth'
        self.sasrec_dir = 'pytorch_models/sasrec'
        self.ngcf_dir = 'pytorch_models/ngcf/model'
        self.ngcf_location = 'pytorch_models/ngcf/model/NGCF.pkl'

    def get_s3_client(self):
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        )
        return s3

    def download_kprn_model(self):
        if not os.path.exists(self.kprn_location):
            if not os.path.exists(self.kprn_dir):
                os.makedirs(self.kprn_dir)
            s3 = self.get_s3_client()
            print(f"Download KPRN model")
            s3.download_file(Bucket='pseudorec-models', Key='kprn/kprn.pt', Filename=self.kprn_location)
        else:
            print(f"KPRN model exists.")

    def download_sasrec_model(self):
        if not os.path.exists(self.sasrec_location):
            if not os.path.exists(self.sasrec_dir):
                os.makedirs(self.sasrec_dir)
            s3 = self.get_s3_client()
            print(f"Download sasrec model")
            s3.download_file(Bucket='pseudorec-models', Key='SASRec/init/sasrec.pth', Filename=self.sasrec_location)
            s3.download_file(Bucket='pseudorec-models', Key='SASRec/init/movie_id_dict.pkl',
                             Filename='pytorch_models/sasrec/movie_id_dict.pkl')
            s3.download_file(Bucket='pseudorec-models', Key='SASRec/init/params.json',
                             Filename='pytorch_models/sasrec/params.json')
            s3.download_file(Bucket='pseudorec-models', Key='SASRec/init/args.py',
                             Filename='pytorch_models/sasrec/args.py')
        else:
            print(f"SASRec model exists.")

    def download_ngcf_model(self):
        if not os.path.exists(self.ngcf_location):
            if not os.path.exists(self.ngcf_dir):
                os.makedirs(self.ngcf_dir)
            s3 = self.get_s3_client()
            print(f"Download NGCF model")
            s3.download_file(Bucket='pseudorec-models', Key='ngcf/NGCF.pkl', Filename=self.ngcf_location)
        else:
            print(f"NGCF model exists.")


if __name__ == "__main__":
    print(os.getcwd())
    model_downloader = ModelDownloader()
    model_downloader.download_sasrec_model()
    model_downloader.download_kprn_model()
    model_downloader.download_ngcf_model()
