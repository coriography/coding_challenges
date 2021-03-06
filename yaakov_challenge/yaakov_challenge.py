import json

class Candidate:

    def __init__(self) -> None:
        pass

    def is_senior_role(self, role): #?? how can this refer to self??
        pass
        # returns Boolean - contains "senior"

    def is_data_role():
        pass
        # returns Boolean - contains "data," "analyst," or "analytics"

    def is_leadership_role():
        pass
        # returns Boolean - contains "manager"

    def get_years_experience():
        pass
        # get years in each job (need to pass to average function later)
        # total years
        # years in senior role
        # years in data role
        # years in leadership

    def get_current_job():
        pass
        # get job with end date "null"
        # get title
        # get length in position

    def get_average_years_in_job():
        pass
        # take years in each job from get_years_experience

class RecruitingTool:

    def __init__(self) -> None:
        self.candidate_data_path = None
        self.candidate_data = None
        # set all attributes to 0 or None

    def import_candidate_data(self, path):
        # read json file and set data as attribute
        
        self.candidate_data_path = path
        json_file = open(self.candidate_data_path)
        self.candidate_data = json.load(json_file)

    def print_screened_candidate_info():
        pass
        # print candidate info


r = RecruitingTool()
r.import_candidate_data("work_experience.json")
r.print_screened_candidate_info()
# print(r.__dict__)
# print(type(r.candidate_data))