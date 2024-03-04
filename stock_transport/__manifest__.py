{
    'name': "stock transport",
    'version': '1.0',
    'depends': ['base', 'stock_picking_batch', 'fleet'],
    'application': True,
    'installable': True,
    'data': [
        'views/inherit_fleet_vehicle_category_view.xml',
        'views/inherit_stock_picking_batch_views.xml',
        'views/inherit_stock_picking_view.xml',
    ],
    'author': "krra",
}
