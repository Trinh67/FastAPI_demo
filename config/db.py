from sqlalchemy import create_engine, MetaData
import json

engine = create_engine("mysql+pymysql://root:@localhost:3306/demo-api")

meta = MetaData()
conn = engine.connect()

# Get config json
with open("config/bff.json", encoding="utf8") as f:
    data = json.load(f)
data_config = data["data"]
