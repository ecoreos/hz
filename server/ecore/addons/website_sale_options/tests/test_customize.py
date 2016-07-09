import ecore.tests

@ecore.tests.common.at_install(False)
@ecore.tests.common.post_install(True)
class TestUi(ecore.tests.HttpCase):
    def test_01_admin_shop_customize_tour(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('shop_customize', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.shop_customize", login="admin")
