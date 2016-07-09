from ecore.api import Environment
import ecore.tests
@ecore.tests.common.at_install(False)
@ecore.tests.common.post_install(True)
class TestWebsiteHrRecruitmentForm(ecore.tests.HttpCase):
    def test_tour(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('website_hr_recruitment_tour', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.website_hr_recruitment_tour")

        # get test cursor to read from same transaction browser is writing to
        cr = self.registry.cursor()
        assert cr == self.registry.test_cr
        env = Environment(cr, self.uid, {})

        record = env['hr.applicant'].search([('description', '=', '### HR RECRUITMENT TEST DATA ###')])
        assert len(record) == 1
        assert record.partner_name == "John Smith"
        assert record.email_from == "john@smith.com"
        assert record.partner_phone == '118.218'
