import ecore.tests
# Part of eCore. See LICENSE file for full copyright and licensing details.


@ecore.tests.common.at_install(False)
@ecore.tests.common.post_install(True)
class TestUi(ecore.tests.HttpCase):

    def test_01_admin_survey_tour(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('test_survey', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.test_survey", login="admin")

    def test_02_demo_survey_tour(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('test_survey', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.test_survey", login="demo")

    def test_03_public_survey_tour(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('test_survey', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.test_survey")
