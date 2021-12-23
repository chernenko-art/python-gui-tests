import random


def test_modify_group(app):
    if len(app.groups.get_group_list()) < 2:
        app.groups.add_new_group("new group")
    old_list = app.groups.get_group_list()
    group_index = random.randrange(len(old_list))
    app.groups.modify_group_by_index(group_index, "modify_group")
    new_list = app.groups.get_group_list()
    old_list[group_index] = "modify_group"
    assert sorted(old_list) == sorted(new_list)
