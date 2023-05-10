import pandas as pd
df = pd.read_excel('MET001.xlsx')

def TransaccionesAgiles(): 
    # Transacción Ágil TD Aprobada 
    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')
                     & (df['FLAG_SIN_PIN'] == 1)]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Transacción Ágil TD Aprobada")
    else:
        print("[Correcto] Transacción Ágil TD Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Transacción Ágil TD Aprobada.xlsx')

    # Transacción Ágil TD PIN Aprobada 
    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')
                     & (df['FLAG_SIN_PIN'] == 0)]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Transacción Ágil TD PIN Aprobada")
    else:
        print("[Correcto] Transacción Ágil TD PIN Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Transacción Ágil TD PIN Aprobada.xlsx')


    # Transacción Ágil TD Reversada 

    df_temp = df.loc[(df['PRESTACION'] == 'TD  ')
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')
                     & (df['FLAG_SIN_PIN'] == 1)]
    
    count_row = df_temp.shape[0]  

    if df_temp.empty:
        print("[Falta] Transacción Ágil TD Reversada")
    else:
        print("[Correcto] Transacción Ágil TD Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Transacción Ágil TD Reversada.xlsx')


    # Transacción Ágil TC Aprobada 
    df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')
                     & (df['FLAG_SIN_PIN'] == 1)]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Transacción Ágil TC Aprobada")
    else:
        print("[Correcto] Transacción Ágil TC Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Transacción Ágil TC Aprobada.xlsx')

    # Transacción Ágil TC PIN Aprobada 
    df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == '    ')
                     & (df['FLAG_SIN_PIN'] == 0)]

    count_row = df_temp.shape[0]  
    if df_temp.empty:
        print("[Falta] Transacción Ágil TC PIN Aprobada")
    else:
        print("[Correcto] Transacción Ágil TC PIN Aprobada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Transacción Ágil TC PIN Aprobada.xlsx')




    # Transacción Ágil TC Reversada 
    df_temp = df.loc[(df['PRESTACION'] == 'TC  ')
                     & (df['METODO'] == 7)
                     & (df['COD_RE'] == 00)
                     & (df['COD_REEXT'] == 'R001')
                     & (df['FLAG_SIN_PIN'] == 1)]
                         
    count_row = df_temp.shape[0]  

    if df_temp.empty:
        print("[Falta] Transacción Ágil TC Reversada")
    else:
        print("[Correcto] Transacción Ágil TC Reversada", "|", count_row, "Caso(s) encontrado(s)")
        df_temp.to_excel('Transacción Ágil TC Reversada.xlsx')



    print("\n")