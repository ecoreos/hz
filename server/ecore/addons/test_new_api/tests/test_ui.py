import ecore.tests

@ecore.tests.common.at_install(False)
@ecore.tests.common.post_install(True)
class TestUi(ecore.tests.HttpCase):
    def test_01_admin_widget_x2many(self):
        self.phantom_js("/web#action=test_new_api.action_discussions",
                        "ecore.__DEBUG__.services['web.Tour'].run('widget_x2many', 'test')",
                        "ecore.__DEBUG__.services['web.Tour'].tours.widget_x2many",
                        login="admin")
