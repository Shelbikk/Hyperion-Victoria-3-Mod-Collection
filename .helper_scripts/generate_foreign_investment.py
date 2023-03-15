import os


investment_periods = {
    "short": 1,
    "medium": 3,
    "long": 10,
}

investment_intensities = {"low": 5, "medium": 20, "high": 100, "very_high": 500}


investment_option_template = """
	option = {{
		trigger = {{
			modifier:country_construction_add >= {investment_intensity}
		}}
		name = SM_foreign_investment.{investment_intensity_name}_investment.{investment_period_name}_term
		scope:target_country = {{
			add_modifier = {{
				name = SM_foreign_investment_receiver_{investment_intensity_name}
				years = {investment_period}
			}}
		}}
		add_modifier = {{
			name = SM_foreign_investment_provider_{investment_intensity_name}
			years = {investment_period}
		}}
	}}
"""

localization_template = '\n SM_foreign_investment.{investment_intensity_name}_investment.{investment_period_name}_term:0 "Invest {investment_intensity} [concept_construction] for {investment_period}."'


def pluralize(word, count):
    if count == 1:
        return word
    return word + "s"


def main():
    output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "outputs")
    output = ""
    output_localization = ""

    for (
        investment_intensity_name,
        investment_intensity,
    ) in investment_intensities.items():
        for investment_period_name, investment_period in investment_periods.items():
            output += investment_option_template.format(
                investment_intensity_name=investment_intensity_name,
                investment_period_name=investment_period_name,
                investment_period=investment_period,
                investment_intensity=investment_intensity,
            )
            output_localization += localization_template.format(
                investment_intensity_name=investment_intensity_name,
                investment_period_name=investment_period_name,
                investment_period=f"{investment_period} {pluralize('year', investment_period)}",
                investment_intensity=investment_intensity,
            )

    with open(
        os.path.join(output_path, "SM_foreign_investment_options.txt"),
        "w",
        encoding="utf-8-sig",
    ) as f:
        f.write(output)

    with open(
        os.path.join(output_path, "SM_foreign_investment_localization.txt"),
        "w",
        encoding="utf-8-sig",
    ) as f:
        f.write(output_localization)


main()
