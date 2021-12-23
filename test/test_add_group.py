def test_add_group(app, exel_group):
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(exel_group)
    new_list = app.groups.get_group_list()
    old_list.append(exel_group)
    assert sorted(old_list) == sorted(new_list)
