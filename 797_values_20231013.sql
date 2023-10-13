--

select
	item_id,
	name_
from (values
		(3943, 'first'),
		(3493, 'second'),
		(8994, 'third'),
		(7989, 'fourth')
) as items(item_id, name_);
