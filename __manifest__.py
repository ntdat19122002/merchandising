{
    'name': "Merchandising",
    'summary': """
        Optimize user experience for upselling    
    """,
    'description': """
        
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu_items.xml',
        'views/setting_views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'merchandising.pv_js_package_assets': [
            'merchandising/static/js/index.js'
        ]
    }
}
