select idEmpleado, sum(cantidad) as suma from venta group by idEmpleado order by suma asc;

SELECT
  EXTRACT(year FROM Fecha) AS year,
  SUM(cantidad) AS cantidad
FROM venta
GROUP BY EXTRACT(year FROM Fecha)
ORDER BY cantidad;

Select IdCanal,
  EXTRACT(year FROM Fecha) AS year,
  SUM(cantidad) AS cantidad
  FROM venta
  GROUP BY IdCanal, EXTRACT(year FROM Fecha)
	ORDER BY year, cantidad;
    
    select * from canal_venta;
    
select IDProducto from producto
where concepto = "PARLANTE JBL GO ORANGE BLUETOOTH";
  
select EXTRACT(year FROM Fecha) AS year, avg(datediff(Fecha_Entrega, Fecha)) as media from venta
GROUP BY EXTRACT(year FROM Fecha) order by media;