import pandas as pd
df = pd.read_excel('MET001.xlsx')

def VentaTDTC(): 
    
    # Venta TD Banda Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['METODO'] == 90) & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Venta TD Banda Aprobada")
    else:
        print("[Correcto] Venta TD Banda Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TD Banda Aprobada.xlsx')

    # Venta TD Banda Reversada

    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['METODO'] == 90)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]

    count_row = df_temp.shape[0]

    if df_temp.empty:
        print("[Falta] Venta TD Banda Reversada")
    else:
        print("[Correcto] Venta TD Banda Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TD Banda Reversada.xlsx')


    # Venta TC Banda Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                     & (df['METODO'] == 90)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Venta TC Banda Aprobada")
    else:
        print("[Correcto] Venta TC Banda Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TC Banda Aprobada.xlsx')


    # Venta TC Banda Reversada
    df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                     & (df['METODO'] == 90)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]
    count_row = df_temp.shape[0]  

    if df_temp.empty:
        print("[Falta] Venta TC Banda Reversada")
    else:
        print("[Correcto] Venta TC Banda Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TC Banda Reversada.xlsx')


    #########################################################################################################
    #########################################################################################################

    # Venta TD Chip Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['METODO'] == 5)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Venta TD Chip Aprobada")
    else:
        print("[Correcto] Venta TD Chip Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TD Chip Aprobada.xlsx')


    # Venta TD Chip Reversada

    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['METODO'] == 5)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]

    count_row = df_temp.shape[0]  

    if df_temp.empty:
        print("[Falta] Venta TD Chip Reversada")
    else:
        print("[Correcto] Venta TD Chip Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TD Chip Reversada.xlsx')


    # Venta TC Chip Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                     & (df['METODO'] == 5)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Venta TC Chip Aprobada")
    else:
        print("[Correcto] Venta TC Chip Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TC Chip Aprobada.xlsx')


    # Venta TC Chip Reversada
    df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                     & (df['METODO'] == 5)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]
    count_row = df_temp.shape[0]  

    if df_temp.empty:
        print("[Falta] Venta TC Chip Reversada")
    else:
        print("[Correcto] Venta TC Chip Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TC Chip Reversada.xlsx')

    #########################################################################################################
    #########################################################################################################

    # Venta TD CTLS Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Venta TD CTLS Aprobada")
    else:
        print("[Correcto] Venta TD CTLS Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TD CTLS Aprobada.xlsx')


    # Venta TD CTLS Reversada

    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]

    count_row = df_temp.shape[0]  

    if df_temp.empty:
        print("[Falta] Venta TD CTLS Reversada")
    else:
        print("[Correcto] Venta TD CTLS Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TD CTLS Reversada.xlsx')


    # Venta TC CTLS Aprobada
    df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Venta TC CTLS Aprobada")
    else:
        print("[Correcto] Venta TC CTLS Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TC CTLS Aprobada.xlsx')


    # Venta TC CTLS Reversada
    df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')]
    count_row = df_temp.shape[0]  

    if df_temp.empty:
        print("[Falta] Venta TC CTLS Reversada")
    else:
        print("[Correcto] Venta TC CTLS Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Venta TC CTLS Reversada.xlsx')

    print("\n")