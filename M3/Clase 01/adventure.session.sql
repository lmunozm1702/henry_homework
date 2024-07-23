use adventureworks;

-- 1. Crear un procedimiento que recibe como parámetro una fecha y muestre la cantidad de órdenes ingresadas en esa fecha.
DROP PROCEDURE totalOrdenes;
DELIMITER $$
CREATE PROCEDURE totalOrdenes(IN fechaOrden DATE)
BEGIN
	SELECT count(*)
	FROM salesorderheader
	WHERE DATE(OrderDate) = fechaOrden;
END $$
DELIMITER ;

call totalOrdenes('2001/06/30');

-- 2. Crear una función que calcule el valor nominal de un margen bruto determinado por el usuario a partir del precio de lista de los productos.
SET GLOBAL log_bin_trust_function_creators = 1;

DROP FUNCTION IF EXISTS margenBruto;
DELIMITER $$
CREATE FUNCTION margenBruto(precio DECIMAL(15,3), margen DECIMAL(9,3)) 
RETURNS DECIMAL(15,3)
BEGIN
	DECLARE margenBruto DECIMAL(15,3);
    SET margenBruto = precio * margen;
    RETURN margenBruto;
END $$
DELIMITER ;

Select margenBruto(100.50, 1.2);

-- 3. Obtner un listado de productos en orden alfabético que muestre cuál debería ser el valor de precio de lista, si se quiere aplicar un margen bruto del 20%, 
-- utilizando la función creada en el punto 2, sobre el campo StandardCost. Mostrando tambien el campo ListPrice y la diferencia con el nuevo campo creado.

SELECT productid, 
	   name,
       ListPrice,
       StandardCost,
       margenBruto(StandardCost, 1.2) as 'cost w/margin',
       ListPrice - margenBruto(StandardCost, 1.2) as 'margin'
FROM product order by name

-- Crear un procedimiento que reciba como parámetro una fecha desde y una hasta, y muestre un listado con los Id de los diez Clientes que más costo de transporte 
-- tienen entre esas fechas (campo Freight).

