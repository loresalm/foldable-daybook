import json
import res.utils as ut

if __name__ == "__main__":
    config_file_path = 'data/inputs/config.json'
    output_file_path = 'data/output/foldable_daybook.pdf'
    with open(config_file_path, 'r') as json_file:
        config = json.load(json_file)
    start_date = config["start_date"]
    nb_weeks = config["nb_weeks"]
    ut.generate_pdf(output_file_path, start_date, nb_weeks)
