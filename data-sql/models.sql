BEGIN;
--
-- Create model Permit
--
CREATE TABLE "bldg_permit" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "date" varchar(100) NOT NULL, 
    "number" varchar(100) NOT NULL, 
    "type" varchar(100) NOT NULL, 
    "subtype" varchar(100) NOT NULL, 
    "description" varchar(100) NOT NULL);
COMMIT;