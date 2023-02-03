from utils.utils import save_file

target_count = 100

buildings_categories = {
    "agriculture": {
        "event_index": 100,
        "count": [1, 5, 25, 200],
        "buildings": {
            "building_rye_farm",
            "building_wheat_farm",
            "building_rice_farm",
            "building_maize_farm",
            "building_millet_farm",
            "building_livestock_ranch",
        },
    },
    "plantations": {
        "event_index": 200,
        "count": [1, 5, 25, 200],
        "buildings": {
            "building_coffee_plantation",
            "building_cotton_plantation",
            "building_dye_plantation",
            "building_opium_plantation",
            "building_tea_plantation",
            "building_tobacco_plantation",
            "building_sugar_plantation",
            "building_banana_plantation",
            "building_silk_plantation",
        },
    },
    "resources": {
        "event_index": 300,
        "count": [1, 5, 15, 50],
        "buildings": {
            "building_logging_camp",
            "building_rubber_plantation",
            "building_fishing_wharf",
            "building_whaling_station",
            "building_oil_rig",
            "building_gold_mine",
            "building_coal_mine",
            "building_iron_mine",
            "building_lead_mine",
            "building_sulfur_mine",
        },
    },
    "infrastructure": {
        "event_index": 400,
        "count": [1, 3, 7, 15],
        "buildings": {
            "building_railway",
            "building_port",
            "building_government_administration",
        },
    },
}

building_to_resource_name = {
    "building_coal_mine": "bg_coal_mining",
    "building_fishing_wharf": "bg_fishing",
    "building_gold_mine": "bg_gold_mining",
    "building_iron_mine": "bg_iron_mining",
    "building_lead_mine": "bg_lead_mining",
    "building_logging_camp": "bg_logging",
    "building_oil_rig": "bg_oil_extraction",
    "building_rubber_plantation": "bg_rubber",
    "building_sulfur_mine": "bg_sulfur_mining",
    "building_whaling_station": "bg_whaling",
    "building_banana_plantation": "bg_banana_plantations",
    "building_coffee_plantation": "bg_coffee_plantations",
    "building_cotton_plantation": "bg_cotton_plantations",
    "building_dye_plantation": "bg_dye_plantations",
    "building_livestock_ranch": "bg_livestock_ranches",
    "building_maize_farm": "bg_maize_farms",
    "building_millet_farm": "bg_millet_farms",
    "building_opium_plantation": "bg_opium_plantations",
    "building_rice_farm": "bg_rice_farms",
    "building_rye_farm": "bg_rye_farms",
    "building_silk_plantation": "bg_silk_plantations",
    "building_sugar_plantation": "bg_sugar_plantations",
    "building_tea_plantation": "bg_tea_plantations",
    "building_tobacco_plantation": "bg_tobacco_plantations",
    "building_wheat_farm": "bg_wheat_farms",
}

building_event_template = """
SM_foreign_investment.{event_index} = {{
	type = country_event
	placement = ROOT

    title = SM_foreign_investment.{event_index}.t
    desc = SM_foreign_investment.{event_index}.d
    flavor = SM_foreign_investment.{event_index}.f

	event_image = {{
		video = "gfx/event_pictures/unspecific_signed_contract.bk2"
	}}
	immediate = {{
		scope:SM_foreign_investment_building_target = {{
{immediate}
	    }}
    }}
	option = {{
		name = CANCEL
		default_option = yes
	}}

#	option = {{
#		name = BACK
#		trigger_event = {{
#			id = SM_foreign_investment.20
#			days = 0
#			popup = yes
#		}}
#	}}

{options}
}}
"""

building_option_template_with_check = """
	option = {{
        name = SM_build_{building}_{count_full}
		trigger = {{
			has_local_variable = SM_can_expand_{building}
		}}
		scope:SM_foreign_investment_building_target = {{
			start_building_construction = {building}
			SM_expand_building = {{
				building = {building}
				levels = {count}
			}}
		}}
	}}
"""

building_option_template = """
	option = {{
        name = SM_build_{building}_{count_full}
		scope:SM_foreign_investment_building_target = {{
			start_building_construction = {building}
			SM_expand_building = {{
				building = {building}
				levels = {count}
			}}
		}}
	}}
"""

bot = {
    "agriculture": building_option_template_with_check,
    "plantations": building_option_template_with_check,
    "resources": building_option_template_with_check,
    "infrastructure": building_option_template,
}

immediate_block_template = """
			if = {{
				limit = {{any_scope_building = {{ is_building_type = {building} }}}}
				set_local_variable = {{
					name = SM_can_expand_{building}
				}}
			}}
			else = {{
				start_building_construction = {building}
				if = {{
					limit = {{any_scope_building = {{ is_building_type = {building} }}}}
					set_local_variable = {{
						name = SM_can_expand_{building}
					}}
					remove_building = {building}
				}}
			}}
"""

ibt = {
    "agriculture": immediate_block_template,
    "plantations": immediate_block_template,
    "resources": immediate_block_template,
    "infrastructure": "",
}

localization_building_option_template = (
    """ SM_build_{building}_{count}:0 "Build #V {count}#! ${building}$" """
)

list_appender_template = """
else_if = {{
	limit = {{
		NOT = {{
			exists = scope:SM_foreign_investment_building_target_{index}
		}}
	}}
	this = {{
		save_scope_as = SM_foreign_investment_building_target_{index}
	}}
}}
"""

list_option_template = """
	option = {{
		trigger = {{
			exists = scope:SM_foreign_investment_building_target_{index}
		}}
		name = SM_foreign_investment_building_target_{index}
		scope:SM_foreign_investment_building_target_{index} = {{
			save_scope_as = SM_foreign_investment_building_target
		}}
		trigger_event = {{
			id = SM_foreign_investment.20
			days = 0
			popup = yes
		}}
	}}
"""

list_localization_template = """SM_foreign_investment_building_target_{index}:0 "Expand buildings in [SCOPE.sState('SM_foreign_investment_building_target_{index}').GetName]" """


def process_list_selection():

    list_appender_template_output = ""
    list_option_template_output = ""
    list_localization_output = ""

    for i in range(1, target_count + 1):
        list_appender_template_output += "\n" + list_appender_template.format(
            index=i
        ).replace("\t", " ").replace("\n", " ")

        list_option_template_output += "\n" + list_option_template.format(
            index=i
        ).replace("\t", " ").replace("\n", " ")

        list_localization_output += "\n " + list_localization_template.format(index=i)

    save_file("SM_list_appender_template_output.txt", list_appender_template_output)
    save_file("SM_list_option_template_output.txt", list_option_template_output)
    save_file("SM_list_localization_output.txt", list_localization_output)


def process_building_events():
    localization = ""
    for building_category_name, building_category in buildings_categories.items():
        filename = "SM_building_" + building_category_name + ".txt"
        options = ""
        immediate = ""

        for building in building_category["buildings"]:
            immediate += "\n" + (
                ibt[building_category_name]
                .format(building=building)
                .replace("\t", " ")
                .replace("\n", " ")
            )
            for building_count in building_category["count"]:
                building_resource = (
                    building_to_resource_name[building]
                    if building in building_to_resource_name
                    else ""
                )

                options += "\n" + (
                    bot[building_category_name]
                    .format(
                        building=building,
                        count_full=building_count,
                        count=building_count - 1,
                        building_resource=building_resource,
                    )
                    .replace("\t", " ")
                    .replace("\n", " ")
                )

                localization += "\n" + localization_building_option_template.format(
                    building=building, count=building_count
                )

        event = building_event_template.format(
            event_index=building_category["event_index"],
            options=options,
            immediate=immediate,
        )
        save_file(filename, event)
    save_file("SM_building_localization.txt", localization)


def main():
    # process_list_selection()
    process_building_events()


main()
