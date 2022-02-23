def facturar(cantidad, iva=21):
    print('{:<10} {:<5}'.format('Cantidad $', 'IVA %'))
    iva = iva/100
    print('{:<10} {:<5}'.format(cantidad, iva))
    print('-------------------')
    print('Factura Total:', cantidad+cantidad*iva)


facturar(90, 0)
print('\n')
facturar(100)