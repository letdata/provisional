use utah; -- lm-ws2012-1
go

declare @first numeric(10,2)
declare @second decimal(10,2)
declare @flag int = 1

set @first = (select cast(rtrim(replace(ltrim(replace('$    65,999.00   ', '$', '')), ',', '')) as decimal(10,2)))

if @flag = 1
begin
	set @second = (select cast(replace(rtrim(ltrim(replace('$    65,999.00   ', '$', ''))), ',', '') as decimal(10,2)))
end
else if @flag = 2
begin
	set @second = 999.48
end

if @first = @second
select '@first = ' + cast(@first as varchar(128)) + ' and @second = ' + cast(@second as varchar(64))
else
select '@first = ' + cast(@first as varchar(128)) + ' and @second = ' + cast(isnull(@second, '0') as varchar(64))
