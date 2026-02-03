# Copyright 2026 Tecnativa - Christian Ramos
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade

field_renames = [
    (
        "product.template",
        "product_template",
        "equipment_category_id",
        "purchase_equipment_category_id",
    ),
]


@openupgrade.migrate()
def migrate(env, version):
    # Bring the category data from maintenance_equipment_category to the product
    openupgrade.rename_fields(env, field_renames)
