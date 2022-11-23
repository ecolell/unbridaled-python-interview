from app.models.product import Product
from app.models.product_variant import ProductVariant


def test_products_create(client, product_data, db):
    res = client.post("/v1/products/create", json=product_data)
    assert res.status_code == 200
    assert res.json() == {
        "id": 1,
        "name": "Standard-hilt lightsaber",
        "uom": "pcs",
        "category_name": "lightsaber",
        "is_producible": True,
        "is_purchasable": True,
        "type": "product",
        "purchase_uom": "pcs",
        "purchase_uom_conversion_rate": 1,
        "batch_tracked": False,
        "additional_info": "additional info",
        "created_at": "2020-10-23T10:37:05.085000Z",
        "updated_at": "2020-10-23T10:37:05.085000Z",
    }
    assert db.query(Product).count() == 1
    assert db.query(ProductVariant).count() == 1
