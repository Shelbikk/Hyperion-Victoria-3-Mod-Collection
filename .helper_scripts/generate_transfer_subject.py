import os


option_count = 100
scope_name = "subject_autonomy_event_transfer_subject_0"
scope_name_placeholder = "subject_autonomy_event_transfer_subject_{0}"
option_name = "SM_subject_autonomy_event_transfer_text_0"
option_name_placeholder = "SM_subject_autonomy_event_transfer_text_{0}"

option_template = """	option = {
		trigger = {
			exists = scope:subject_autonomy_event_transfer_subject_0
		}
		name = SM_subject_autonomy_event_transfer_text_0
		scope:SM_transfer_target = {
			if = {
				limit = {
					is_country_type = unrecognized
				}
				if = {
					limit = {
						scope:subject_autonomy_event_transfer_subject_0 = {
							or = {
								is_subject_type = subject_type_vassal
								is_subject_type = subject_type_puppet
							}
						}
					}
					create_diplomatic_pact = {
						country = scope:subject_autonomy_event_transfer_subject_0
						type = vassal
					}
				}
				else_if = {
					limit = {
						scope:subject_autonomy_event_transfer_subject_0 = {
							or = {
								is_subject_type = subject_type_dominion
								is_subject_type = subject_type_protectorate
								is_subject_type = subject_type_tributary
							}
						}
					}
					create_diplomatic_pact = {
						country = scope:subject_autonomy_event_transfer_subject_0
						type = tributary
					}
				}
			}
			else = {
				if = {
					limit = {
						scope:subject_autonomy_event_transfer_subject_0 = {
							or = {
								is_subject_type = subject_type_vassal
								is_subject_type = subject_type_puppet
							}
						}
					}
					create_diplomatic_pact = {
						country = scope:subject_autonomy_event_transfer_subject_0
						type = puppet
					}
				}
				else_if = {
					limit = {
						scope:subject_autonomy_event_transfer_subject_0 = {
							is_subject_type = subject_type_dominion
						}
					}
					create_diplomatic_pact = {
						country = scope:subject_autonomy_event_transfer_subject_0
						type = dominion
					}
				}
				else_if = {
					limit = {
						scope:subject_autonomy_event_transfer_subject_0 = {
							or = {
								is_subject_type = subject_type_protectorate
								is_subject_type = subject_type_tributary	
							}
						}
					}
					create_diplomatic_pact = {
						country = scope:subject_autonomy_event_transfer_subject_0
						type = protectorate
					}
	
				}
			}
		}
	}
"""

list_appender_template = """
else_if = {
    limit = {
        NOT = {
            exists = scope:subject_autonomy_event_transfer_subject_0
        }
    }
    this = {
        save_scope_as = subject_autonomy_event_transfer_subject_0
    }
}
"""

localization_template = """SM_subject_autonomy_event_transfer_text_0:0 "Transfer [SCOPE.sCountry('subject_autonomy_event_transfer_subject_0').GetName]" """

options_output = ""
list_appenders_output = ""
localization_output = ""

def replace_scope(input, new_scope_name, new_option_name):
    generated_input = input.replace(scope_name, new_scope_name).replace(option_name, new_option_name)
    stripped_input = generated_input.replace("\t", " ").replace("\n", " ")
    return stripped_input


for option_index in range(1, option_count + 1):
    scope_name_indexed = scope_name_placeholder.format(option_index)
    option_name_indexed = option_name_placeholder.format(option_index)

    options_output += replace_scope(option_template, scope_name_indexed, option_name_indexed) + "\n"
    list_appenders_output += replace_scope(list_appender_template, scope_name_indexed, option_name_indexed) + "\n"
    localization_output += replace_scope(localization_template, scope_name_indexed, option_name_indexed) + "\n"

output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "outputs")

with open(os.path.join(output_path, "generate_transfer_options.txt"), "w") as f:
    f.write(options_output)
    
with open(os.path.join(output_path, "generate_transfer_list_appenders.txt"), "w") as f:
    f.write(list_appenders_output)
    
with open(os.path.join(output_path, "generate_transfer_localization.txt"), "w") as f:
    f.write(localization_output)