GET_FIRMANTES_AVISO = """
select f.codigo
from firmantes_aviso_acto_administrativo a
inner join firmante_acto_administrativo f
on a.firmante_acto_administrativo_id = f.id
where a.aviso_id = ?
order by orden asc
"""

GET_ID_PUBLICACION = """
select metadata 
from aviso 
where id=?
 """