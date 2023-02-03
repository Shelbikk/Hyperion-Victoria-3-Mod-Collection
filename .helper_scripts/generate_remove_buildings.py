import os


buildings = [
    "building_food_industry",
    "building_textile_mills",
    "building_furniture_manufacturies",
    "building_glassworks",
    "building_tooling_workshops",
    "building_paper_mills",
    "building_chemical_plants",
    "building_synthetics_plants",
    "building_steel_mills",
    "building_motor_industry",
    "building_shipyards",
    "building_war_machine_industry",
    "building_electrics_industry",
    "building_arms_industry",
    "building_munition_plants",
    # Military shipyards mod
    "building_military_shipyards",
    # Synthethic oil and rubber mod
    "building_synthetic_rubber_plants",
    "building_synthetic_oil_plants",
    # Explosive industry mod
    "building_explosives_industry",
]

building_template = """
				if = {{
					limit = {{
						has_building = {building}
					}}
					remove_building = {building}
				}}
"""


def main():
    output = ""

    for building in buildings:
        output += building_template.format(building=building)

    with open(
        os.path.join(output_path, "SM_generate_remove_buildings.txt"),
        "w",
        encoding="utf-8-sig",
    ) as f:
        f.write(output)


main()
