from app.db.models import Stars
from view.menu.advande_search import AdvanceSearch
from view.menu.class_createria import CriterionSearch
class AddTagToModelNoSave(CriterionSearch):

    def submit_click(self, values):
        if self.if_empty_value(values[0]['value']):
            self.add_data('Tags', values[0]['value'])
