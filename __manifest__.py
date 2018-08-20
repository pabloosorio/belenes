# -*- coding: utf-8 -*-
{
    'name': "BELENES",

    'summary': """
        Personalizaciones para Belenes""",

    'description': """
         - Add checkbox to validate if the user authorize purchase
         - Add model Purchase Type
         - Add model Purchase Type Users (Sublist)
         - Add field Purchase type to purchase order
         - Add confirmation to purchase order
         - Add submenu on configuration purchase menu
         - Add submenu on purchase menu
         
    """,

    'author': "Pablo Osorio",
    'website': "https://xmarts.com",

    'category': 'Uncategorized',
    'version': '0.2',

    'depends': ['base','purchase'],

    'data': [
        'views/views.xml',
        #'views/templates.xml',
    ],
    'demo': [
        #'demo/demo.xml',
    ],
}