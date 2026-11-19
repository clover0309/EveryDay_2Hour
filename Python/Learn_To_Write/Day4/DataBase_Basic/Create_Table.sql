    CREATE TABLE order_items (
        id INTEGER PRIMARY KEY,
        product_name VARCHAR(100) NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER NOT NULL
    );