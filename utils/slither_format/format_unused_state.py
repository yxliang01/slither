class FormatUnusedState:

    @staticmethod
    def format(slither, patches, elements):
        for element in elements:
            FormatUnusedState.create_patch(slither, patches, element['source_mapping']['filename'], element['source_mapping']['start'])

    @staticmethod
    def create_patch(slither, patches, _in_file, _modify_loc_start):
        in_file_str = slither.source_code[_in_file]
        old_str_of_interest = in_file_str[_modify_loc_start:]
        patches[_in_file].append({
            "detector" : "unused-state",
            "start" : _modify_loc_start,
            "end" : _modify_loc_start + len(old_str_of_interest.partition(';')[0]) + 1,
            "old_string" : old_str_of_interest.partition(';')[0] + old_str_of_interest.partition(';')[1],
            "new_string" : ""
        })

