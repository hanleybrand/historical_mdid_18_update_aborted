BEGIN;
# edit the database name (rooibos) below to match your table name
USE rooibos;
ALTER TABLE `data_field`
	ADD `visible` bool;
ALTER TABLE `data_fieldsetfield`
	MODIFY `importance` smallint;
ALTER TABLE `data_fieldvalue`
	MODIFY `date_start` numeric(12, 0);
ALTER TABLE `data_fieldvalue`
	MODIFY `date_end` numeric(12, 0);
ALTER TABLE `data_fieldvalue`
	MODIFY `numeric_value` numeric(18, 4);
ALTER TABLE `data_fieldvalue`
	MODIFY `context_id` integer UNSIGNED;
COMMIT;
UPDATE rooibos.data_field SET visible=1;  
