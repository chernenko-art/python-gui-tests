import random


def test_del_group(app, exel_group):
    if len(app.groups.get_group_list()) < 2:
        app.groups.add_new_group(exel_group)
    old_list = app.groups.get_group_list()
    group_index = random.randrange(len(old_list))
    app.groups.del_group_by_index(group_index)
    new_list = app.groups.get_group_list()
    old_list.pop(group_index)
    assert sorted(old_list) == sorted(new_list)
