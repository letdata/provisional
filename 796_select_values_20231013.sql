use master;
go

if object_id('yellow..sales') is not null drop table yellow..sales;
select
	item_id,
	item_name,
	price
into yellow..sales
from ( values (394, 'one', 14.99),
			(348, null, 29.48),
			(439, 'three', 38.98)
) as sales(item_id, item_name, price)
where 1 = 1
-- and price > 30

insert into yellow..sales (item_id, price) values(893, 49.99)
-- select * from yellow..sales

select
	table_catalog as database_,
	table_schema as schema_,
	table_name as table_,
	column_name as column_,
	ordinal_position as position,
	column_default as default_,
	is_nullable,
	data_type,
	character_maximum_length as max_length,
	numeric_precision as precision_,
	numeric_scale as scale,
	collation_name
from yellow.INFORMATION_SCHEMA.columns
where 1 = 1
and table_name = 'sales'
