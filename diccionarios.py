def run():
    poblacion_paises = {
        'Venezuela': 35150000,
        'Argentina': 44938000,
        'Brasil': 210014000
    }

    # print(poblacion_paises[Venezuela])
    
    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for poblacion in poblacion_paises.values():
    #     print(poblacion)

    for pais, habitantes in poblacion_paises.items():
        print(pais , 'tiene' , habitantes , 'habitantes')


if __name__ == '__main__':
    run()