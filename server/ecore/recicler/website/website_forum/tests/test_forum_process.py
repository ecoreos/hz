import ecore.tests

@ecore.tests.common.at_install(False)
@ecore.tests.common.post_install(True)
class TestUi(ecore.tests.HttpCase):
    def test_01_admin_forum_tour(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('question', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.question", login="admin")

    def test_02_demo_question(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('forum_question', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.forum_question", login="demo")

