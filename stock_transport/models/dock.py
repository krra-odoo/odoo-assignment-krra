from odoo import fields, models

class Dock(models.Model):
    _name = "dock"
    _description = "Dock"

    name = fields.Char(string="Dock")
