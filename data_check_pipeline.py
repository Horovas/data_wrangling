import json
import psycopg2
from credentials import server, database, login, password

connection = psycopg2.connect(host=server, port='xxx', database=database, user=login, password=password)
connection.autocommit = True
c = connection.cursor()

filename = "source_data.json"

table_1 = '''
    CREATE TABLE IF NOT EXISTS postgres.public.suppliers (
        id int PRIMARY KEY,
        name text,
        inn text
    )
'''

table_2 = '''
    CREATE TABLE IF NOT EXISTS postgres.public.bulk_supply (
        id int PRIMARY KEY,
        name text,
        type text,
        min_weight text,
        supplier_id int REFERENCES suppliers (id)        
    )
'''

table_3 = '''
    CREATE TABLE IF NOT EXISTS postgres.public.sale_items (
        id int PRIMARY KEY,
        package_id int,
        bulk_supply_id int REFERENCES bulk_supply (id),
        delivery_time timestamp,
        need_special_registration bool,
        registration_info text    
    )
'''

c.execute(table_1)
c.execute(table_2)
c.execute(table_3)


insert_suppliers = '''
    INSERT INTO postgres.public.suppliers
        (id, name, inn)
    VALUES
        (%s, %s, %s)
'''

insert_bulk_supply = '''
    INSERT INTO postgres.public.bulk_supply
        (id, name, type, min_weight, supplier_id)
    VALUES
        (%s, %s, %s, %s, %s)
'''

insert_sale_items = '''
    INSERT INTO postgres.public.sale_items
        (id, package_id, bulk_supply_id, delivery_time, need_special_registration)
    VALUES
        (%s, %s, %s, %s, %s)
'''

with open(filename, encoding='utf-8') as file:
    dictionary = json.load(file)

    for supplier in dictionary["suppliers"]:
        c.execute(
            insert_suppliers, 
            (supplier["id"], supplier["name"], supplier["inn"],)
        )


    for bulk_supply in dictionary["bulk_supply"]:
        c.execute(
            insert_bulk_supply, 
            (bulk_supply["id"], bulk_supply["name"], bulk_supply["type"], bulk_supply["minWeight"], bulk_supply["supplierId"],)
        )

    
    for merch in dictionary["sale_items"]:
        c.execute(
            insert_sale_items, 
            (merch["id"], merch["packageId"], merch["bulk_supplyId"], merch["deliveryTime"],
                merch["specialRegistrationData"])
        )


most_popular = """
    SELECT 
        count(p.id),
        p.bulk_supply_id,
        s.name,
        o."name"
    FROM sale_items si
    JOIN bulk_supply bs ON si.bulk_supply_id = bs.id
    JOIN suppliers sup ON bs.supplier_id = sup.id
    GROUP BY si.bulk_supply_id, bs.name, sup.name
    ORDER BY count(si.id) desc
    LIMIT 15
"""
print("Most popular events")
c.execute(most_popular)
data = c.fetchall()
for line in data:
	print(line)
print()


age_range = """
	SELECT distinct(min_weight) 
	FROM postgres.public.bulk_supply
	ORDER BY min_weight
"""
c.execute(age_range)
data = c.fetchall()
for line in data:
	print(f"Weight category: {line[0]}")
print()


inn_types = """
	SELECT
		count(inn),
		CHAR_LENGTH(inn)
	FROM postgres.public.suppliers
	GROUP BY CHAR_LENGTH(inn);
"""

c.execute(inn_types)
data = c.fetchall()
for line in data:
	print(f"INN type. count: {line[0]}, length: {line[1]}")



c.close()
connection.close()

