import psycopg2

class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price
    
    def save(self):
        conn = psycopg2.connect("dbname=your_db_name user=your_username password=your_password")
        cur = conn.cursor()
        query = "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)"
        cur.execute(query, (self.item_name, self.item_price))
        conn.commit()
        cur.close()
        conn.close()
    
    def delete(self):
        conn = psycopg2.connect("dbname=your_db_name user=your_username password=your_password")
        cur = conn.cursor()
        query = "DELETE FROM Menu_Items WHERE item_name = %s"
        cur.execute(query, (self.item_name,))
        conn.commit()
        cur.close()
        conn.close()
    
    def update(self, new_name, new_price):
        conn = psycopg2.connect("dbname=your_db_name user=your_username password=your_password")
        cur = conn.cursor()
        query = "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s"
        cur.execute(query, (new_name, new_price, self.item_name))
        conn.commit()
        cur.close()
        conn.close()

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        conn = psycopg2.connect("dbname=your_db_name user=your_username password=your_password")
        cur = conn.cursor()
        query = "SELECT item_id, item_name, item_price FROM Menu_Items WHERE item_name = %s"
        cur.execute(query, (item_name,))
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result:
            item_id, item_name, item_price = result
            return MenuItem(item_name, item_price)
        else:
            return None
    
    @classmethod
    def all_items(cls):
        conn = psycopg2.connect("dbname=your_db_name user=your_username password=your_password")
        cur = conn.cursor()
        query = "SELECT item_id, item_name, item_price FROM Menu_Items"
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        items = []
        for result in results:
            item_id, item_name, item_price = result
            item = MenuItem(item_name, item_price)
            items.append(item)
        return items

item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuManager.get_by_name('Beef Stew')
items = MenuManager.all_items()
