class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        groups = self.get_groups_pywinauto_object()
        group_list = [node.text() for node in groups]
        self.close_group_editor()
        return group_list

    def add_new_group(self, name):
        self.open_group_editor()
        # click add New group
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        self.set_group_name(name)
        self.close_group_editor()

    def set_group_name(self, name):
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")

    def del_first_group_by_name(self, name):
        self.open_group_editor()
        self.select_first_group_by_name(name)
        self.delete_group()
        self.close_group_editor()

    def delete_group(self):
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        confirm_delete_form = self.app.application.window(title="Delete group")
        confirm_delete_form.window(auto_id="uxOKAddressButton").click()

    def select_first_group_by_name(self, name):
        groups = self.get_groups_pywinauto_object()
        for node in groups:
            if node.text() == name:
                node.select()

    def get_groups_pywinauto_object(self):
        # get main tree element
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        # return children elements
        return root.children()

    def del_group_by_index(self, index):
        self.open_group_editor()
        self.select_group_by_index(index)
        self.delete_group()
        self.close_group_editor()

    def select_group_by_index(self, index):
        groups = self.get_groups_pywinauto_object()
        groups[index].select()

    def modify_group_by_index(self, index, new_name):
        self.open_group_editor()
        self.select_group_by_index(index)
        self.group_editor.window(auto_id="uxEditAddressButton").click()
        self.set_group_name(new_name)
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait("visible")

    def close_group_editor(self):
        self.group_editor.close()
