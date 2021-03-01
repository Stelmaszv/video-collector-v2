from app.db.models import Stars
from view.menu.class_createria import CriterionSearch
class AddStarToModelNoSave(CriterionSearch):

    def submit_click(self, values):
        if self.if_empty_value(values[0]['value']):
            if self.if_value_exist_in_model(Stars,values[0]['value']):
                self.add_data('Stars',values[0]['value'])