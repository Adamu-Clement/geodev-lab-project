import pandas as pd
import geopandas as gpd
def main():
	gdf = gpd.read_file("nga_north_west_ward_boundary.geojson")
	print(gdf.shape)
	print(gdf.head())



if __name__ == "__main__":
	main()