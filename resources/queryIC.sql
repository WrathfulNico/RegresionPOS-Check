SELECT 
ME01MOVNUM AS Nro_Transaccion,
ME01CCOCOD AS Comercio,
ME01CCOSUC AS Sucursal,
GE65TRACOD AS Cod_Transaccion,
ME10TRDOPE AS Codigo_Operacion,
ME01MOVIMP AS Importe,
ME01MONCOD AS Moneda,
GE50ORICAL AS Id_Origen,
GE49TIPDIS AS Cod_Tipo_Dispositivo,
GE66RESCOD AS Cod_Respuesta,
ME02STSMOV AS Estado_Movimiento,
ME01CUONRO AS Nro_Cuota,
ME01MOVPLA AS Plan,
ME01NROLOT AS Nro_Lote,
ME01TARNRO AS Nro_Tarjeta,
IN01MODCOD AS Codigo_de_Modelo,
IN02INVSER AS Nro_Serie_del_POS,
ME01VRSEQP AS Version_del_Software_en_el_Equipo,
GE42SRVIDE AS Id_Servicio,
GE44CODPRE AS Cod_Prestacion,
GE64PAGCOD AS Cod_Medio_Pago,
ME01MARCOD AS Marca,
ME01PRMCOD AS Producto_de_la_Marca,
ME01MOVFHO AS Fecha_y_Hora_Transaccion,
ME01MOVFEC AS Fecha_Transaccion,
ME01MARLOC AS Marca_Local_Internacional,
ME01ENTEMI AS Entidad_Emisora,
GE70RESEXT AS Cod_Respuesta_Extendida,
ME01TARENM AS Tarjeta_Enmascarado,
GE52CPDPFI AS Cod_Prefijo,
ME01CSHBCK AS CashBack,
GE33BINNRO AS Nro_de_Bin,
GE33CNTDIG AS Cantidad_de_Digitos,
ME01REOTTR AS Nro_Trans_relacionada,
ME01CTANRO AS Cuenta_Nro 
FROM GXSWDTA.MET001 
WHERE GE65TRACOD = 72 AND GE42SRVIDE = 'TIC' AND GE49TIPDIS = 'WEB' 
AND ME01MOVFEC  >= ''
AND ME01CCOCOD = ''
AND ME01CCOSUC = ''
AND GE70RESEXT ='' 

