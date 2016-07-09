import ecore.tests

@ecore.tests.common.at_install(False)
@ecore.tests.common.post_install(True)
class TestUi(ecore.tests.HttpCase):
    def test_admin(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('event_buy_tickets', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.event_buy_tickets", login="admin")

    def test_demo(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('event_buy_tickets', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.event_buy_tickets", login="demo")

    def test_public(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('event_buy_tickets', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.event_buy_tickets")
