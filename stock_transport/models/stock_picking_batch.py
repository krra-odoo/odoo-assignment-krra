from odoo import fields, models, api

class StockPickingBatch(models.Model):
    _inherit = "stock.picking.batch"

    vehicle_id = fields.Many2one("fleet.vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category")
    dock_id = fields.Many2one("dock", string='Dock')

    weight = fields.Float(compute="_compute_weight", readonly=True, store=True)
    volume = fields.Float(compute="_compute_volume", readonly=True, store=True)
    no_of_transfers = fields.Float(compute="_compute_no_of_transfers", store=True)
    no_of_lines = fields.Float(compute="_compute_no_of_lines", store=True)

    @api.depends("move_line_ids","vehicle_category_id")
    def _compute_weight(self):
        w = 0
        for record in self:
            temp = record.move_line_ids
            for product in temp:
                w = w + product.product_id.weight*product.quantity

        if self.vehicle_category_id.max_weight>0:
            self.weight = (w/self.vehicle_category_id.max_weight)*100
        else:
            self.weight = w

    @api.depends("move_line_ids", "vehicle_category_id")
    def _compute_volume(self):
        v = 0
        for record in self:
            temp = record.move_line_ids
            for product in temp:
                v = v + product.product_id.volume*product.quantity

        if self.vehicle_category_id.max_volume>0:
            self.volume = (v/self.vehicle_category_id.max_volume)*100
        else:
            self.volume = v

    @api.depends('picking_ids')
    def _compute_no_of_transfers(self):
        for record in self:
            record.no_of_transfers = len(record.picking_ids)

    @api.depends('move_line_ids')
    def _compute_no_of_lines(self):
        for record in self:
            record.no_of_lines = len(record.move_line_ids)

    @api.depends('weight','volume','name')
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name
            if record.weight:
                record.display_name += f' ({record.weight} kg)'
            if record.volume:
                record.display_name += f' ({record.volume} m^3)'
