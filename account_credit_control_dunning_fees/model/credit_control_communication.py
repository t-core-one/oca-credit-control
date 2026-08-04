# Copyright 2014-2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, models


class CreditCommunication(models.Model):
    _inherit = "credit.control.communication"

    @api.model
    def _get_total_due(self):
        balance_field = "credit_control_line_ids.balance_due_total"
        return sum(self.mapped(balance_field))

    @api.model
    def _get_line_balance_due(self, line):
        return line.balance_due_total
