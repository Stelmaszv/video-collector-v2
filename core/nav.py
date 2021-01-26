class NavStars:

    def __init__(self):
        self.buttons=[
                {
                    "name": "Add to favorits",
                    "item_name": "add_to_favorits",
                    "button": self.add_favorits
                },
                {
                    "name": "Add like",
                    "item_name": "add_like",
                    "button": self.add_like
                },
                {
                    "name": "Edit",
                    "item_name": "edit",
                    "button": self.edit
                }
            ]

    def return_buttons(self):
        return  [
                {
                    "name": "Add to favorits",
                    "item_name": "add_to_favorits",
                    "button": self.add_favorits
                },
                {
                    "name": "Add like",
                    "item_name": "add_like",
                    "button": self.add_like
                },
                {
                    "name": "Edit",
                    "item_name": "edit",
                    "button": self.edit
                }
        ]

    def add_favorits(self):
        print('add f')

    def add_like(self):
        print('add_like')

    def edit(self):
        print('edit')

