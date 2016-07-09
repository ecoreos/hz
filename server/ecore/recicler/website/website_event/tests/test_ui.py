import ecore.tests

@ecore.tests.common.at_install(False)
@ecore.tests.common.post_install(True)
class TestUi(ecore.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('event', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.event", login='admin')
