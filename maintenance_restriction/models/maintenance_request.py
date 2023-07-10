# Copyright 2023 Tecnativa - Víctor Martínez
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import fields, models


class MaintenanceRequest(models.Model):
    _inherit = "maintenance.request"

    user_id = fields.Many2one(
        domain="[('id', 'in', allowed_user_ids)]",
    )
    allowed_user_ids = fields.Many2many(
        comodel_name="res.users", compute="_compute_allowed_user_ids"
    )

    def _compute_allowed_user_ids(self):
        group = self.env.ref("maintenance.group_equipment_manager")
        for item in self:
            item.allowed_user_ids = group.users
