from ecore.api import Environment
import ecore.tests
@ecore.tests.common.at_install(False)
@ecore.tests.common.post_install(True)
class TestWebsiteCrm(ecore.tests.HttpCase):
    def test_tour(self):
        self.phantom_js("/", "ecore.__DEBUG__.services['web.Tour'].run('website_crm_tour', 'test')", "ecore.__DEBUG__.services['web.Tour'].tours.website_crm_tour")

        # need environment using the test cursor as it's not committed
        cr = self.registry.cursor()
        assert cr is self.registry.test_cr
        env = Environment(cr, self.uid, {})
        record = env['crm.lead'].search([('description', '=', '### TOUR DATA ###')])
        assert len(record) == 1
        assert record.contact_name == 'John Smith'
        assert record.email_from == 'john@smith.com'
        assert record.partner_name == 'eCore S.A.'
