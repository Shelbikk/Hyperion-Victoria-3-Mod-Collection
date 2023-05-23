import os


laws_categories = {
    "power_structure_laws": {
        "lawgroup_governance_principles": [
            "law_monarchy",
            "law_presidential_republic",
            "law_parliamentary_republic",
            "law_theocracy",
            "law_council_republic",
            "law_chiefdom",
        ],
        "lawgroup_distribution_of_power": [
            "law_autocracy",
            "law_technocracy",
            "law_oligarchy",
            "law_landed_voting",
            "law_wealth_voting",
            "law_census_voting",
            "law_universal_suffrage",
            "law_anarchy",
            "law_single_party_state",
            "law_elder_council",
        ],
        "lawgroup_citizenship": [
            "law_ethnostate",
            "law_national_supremacy",
            "law_racial_segregation",
            "law_cultural_exclusion",
            "law_multicultural",
        ],
        "lawgroup_church_and_state": [
            "law_state_religion",
            "law_freedom_of_conscience",
            "law_total_separation",
            "law_state_atheism",
        ],
        "lawgroup_bureaucracy": [
            "law_hereditary_bureaucrats",
            "law_appointed_bureaucrats",
            "law_elected_bureaucrats",
        ],
        "lawgroup_army_model": [
            "law_peasant_levies",
            "law_national_militia",
            "law_mass_conscription",
            "law_professional_army",
        ],
        "lawgroup_internal_security": [
            "law_no_home_affairs",
            "law_national_guard",
            "law_secret_police",
            "law_guaranteed_liberties",
        ],
    },
    "economic_laws": {
        "lawgroup_economic_system": [
            "law_traditionalism",
            "law_interventionism",
            "law_agrarianism",
            "law_industry_banned",
            "law_laissez_faire",
            "law_cooperative_ownership",
            "law_command_economy",
        ],
        "lawgroup_trade_policy": [
            "law_free_trade",
            "law_protectionism",
            "law_isolationism",
            "law_mercantilism",
        ],
        "lawgroup_taxation": [
            "law_consumption_based_taxation",
            "law_land_based_taxation",
            "law_per_capita_based_taxation",
            "law_proportional_taxation",
            "law_graduated_taxation",
        ],
        "lawgroup_land_reform": [
            "law_serfdom",
            "law_tenant_farmers",
            "law_homesteading",
            "law_commercialized_agriculture",
            "law_collectivized_agriculture",
        ],
        "lawgroup_colonization": [
            "law_no_colonial_affairs",
            "law_colonial_resettlement",
            "law_colonial_exploitation",
        ],
        "lawgroup_policing": [
            "law_no_police",
            "law_local_police",
            "law_dedicated_police",
            "law_militarized_police",
        ],
        "lawgroup_education_system": [
            "law_no_schools",
            "law_religious_schools",
            "law_private_schools",
            "law_public_schools",
        ],
        "lawgroup_health_system": [
            "law_no_health_system",
            "law_charitable_health_system",
            "law_private_health_insurance",
            "law_public_health_insurance",
        ],
    },
    "human_rights_laws": {
        "lawgroup_free_speech": [
            "law_outlawed_dissent",
            "law_censorship",
            "law_right_of_assembly",
            "law_protected_speech",
        ],
        "lawgroup_labor_rights": [
            "law_no_workers_rights",
            "law_regulatory_bodies",
            "law_worker_protections",
        ],
        "lawgroup_childrens_rights": [
            "law_child_labor_allowed",
            "law_restricted_child_labor",
            "law_compulsory_primary_school",
        ],
        "lawgroup_rights_of_women": [
            "law_no_womens_rights",
            "law_women_own_property",
            "law_women_in_the_workplace",
            "law_womens_suffrage",
        ],
        "lawgroup_welfare": [
            "law_no_social_security",
            "law_poor_laws",
            "law_wage_subsidies",
            "law_old_age_pension",
        ],
        "lawgroup_migration": [
            "law_no_migration_controls",
            "law_migration_controls",
            "law_closed_borders",
        ],
        "lawgroup_slavery": [
            "law_slavery_banned",
            "law_debt_slavery",
            "law_slave_trade",
            "law_legacy_slavery",
        ],
    },
}

law_category_to_namespace = {
    "economic_laws": "SM_change_economic_laws",
    "human_rights_laws": "SM_change_human_rights_laws",
    "power_structure_laws": "SM_change_power_structure_laws",
}

choice_event_template = """
namespace = {namespace}

{namespace}.1 = {{
	type = country_event
	placement = ROOT

    title = {namespace}.1.t
    desc = {namespace}.1.d
    flavor = {namespace}.1.f

	event_image = {{
		video = "gfx/event_pictures/unspecific_signed_contract.bk2"
	}}

	option = {{
		name = CANCEL
		default_option = yes
	}}

    {options}
}}
"""
choice_event_option_template = """
	option = {{
		name = {lawgroup}
		trigger_event = {{
			id = {namespace}.{lawgroup_index}
			days = 0
			popup = yes
		}}
	}}
"""

sub_choice_event_template = """{namespace}.{lawgroup_index} {{
	type = country_event
	placement = ROOT

    title = {lawgroup}
    desc = {lawgroup}
    flavor = {lawgroup}_desc

	event_image = {{
		video = "gfx/event_pictures/unspecific_signed_contract.bk2"
	}}
	
	option = {{
		name = CANCEL
		default_option = yes
	}}

	{options}
}}
"""

sub_event_option_template = """
	option = {{
		trigger = {{
			scope:SM_change_laws_target = {{
				NOT = {{ has_law = law_type:{law} }}
			}}
		}}
		name = {law}
		scope:SM_change_laws_target = {{
			activate_law = law_type:{law}
		}}
        trigger_event = {{
			id = {namespace}.1
			days = 0
			popup = yes
		}}
	}}
"""


def main():
    output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "outputs")

    for law_category, lawgroups in laws_categories.items():
        namespace = law_category_to_namespace[law_category]
        sub_choice_events = []
        choice_event_options = ""
        lawgroup_index = 2

        for lawgroup, laws in lawgroups.items():
            options = ""
            for law in laws:
                options += sub_event_option_template.format(
                    law=law, namespace=namespace
                )

            sub_choice_event = sub_choice_event_template.format(
                lawgroup_index=lawgroup_index,
                lawgroup=lawgroup,
                options=options,
                namespace=namespace,
            )
            sub_choice_events.append(sub_choice_event)
            choice_event_options += choice_event_option_template.format(
                lawgroup_index=lawgroup_index, lawgroup=lawgroup, namespace=namespace
            )

            lawgroup_index += 1

        choice_event = choice_event_template.format(
            namespace=namespace, options=choice_event_options
        )

        with open(os.path.join(output_path, f"{namespace}.txt"), "w") as f:
            f.write(choice_event)
            f.write("\n".join(sub_choice_events))


main()
