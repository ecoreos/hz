# -*- encoding: utf-8 -*-

{
    'name': 'Ingreso rapido de datos',
    'version': '1',
    "author" : "Avalos Corp.",
    "category" : "Tools",
    'description': """
    
    VENTAS DE MOTRADOR:
    
    Modulo que permite Capturar Lineas de Forma Rapida solo Agregando la Cantidad y el Producto.
    
    Funciona para Ventas, Facturacion y Compras.

    Funcionamiento:
        -En los Formularios antes del Apartado de Lineas(Detalle), existen 2 Campos, Cantidad y Producto. Al seleccionar el Producto se agregara la linea de Forma Automatica, tomando como referencia principal los detalles de la Ficha del Producto.

    """,
    "depends" : ["account","sale","purchase"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [
                    "sale_view.xml",
                    "purchase_view.xml",
                    "invoice_view.xml",
                    ],
    "installable" : True,
    "active" : False,
}
