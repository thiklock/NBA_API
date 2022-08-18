from nba_api.stats.static import players
import spark
# Get all players.
players_ = players.get_players()

print(players_)

# >>> data = [ { "a": "01", "b": "teste01" }, { "a": "02", "b": "teste02" } ]
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("JsonToParquetPysparkExample") \
    .getOrCreate()

json_df = spark.read.json("C://python/test.json", multiLine=True,) 
json_df.printSchema()
json_df.write.parquet("C://python/output.parquet")