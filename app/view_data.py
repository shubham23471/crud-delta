from deltalake import DeltaTable


def view_sample_data(input_data_path):
	dt = DeltaTable(input_data_path)
	df = dt.to_pandas()
	return df.to_json()