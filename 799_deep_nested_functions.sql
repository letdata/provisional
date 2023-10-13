use utah; -- lm-ws2012-1
go
/* -------------------------------------------------------------
    indentation is only to help our eyes/brain
    this could be flattened and it will work just the same
-- ------------------------------------------------------------- */
select
	salary6 as salary
from ( -- s6
	select
		cast(salary5 as decimal(10,2)) as salary6
	from ( -- s5
		select
			rtrim(salary4) as salary5
		from ( -- s4
			select
				replace(salary3, ',', '') as salary4
			from ( -- s3
				select
					ltrim(salary2) as salary3
				from ( -- s2
					select
						replace(salary1, '$', '') as salary2
					from ( -- s1
						select '$    65,999.00   ' as salary1 -- MOST INNER QUERY - FIRST TO RUN AND RETURN SOMETHING
					) s1
				) s2
			) s3
		) s4
		-- 65,999
	) s5
) s6
