from app.models.product import Product
from app.models.product_variant import ProductVariant
from sqlmodel import select


def test_products_create(client, db):
    # assert db(select(Product))
    # assert db(select(ProductVariant))
    data = {
        "name": "Standard-hilt lightsaber",
        "uom": "pcs",
        "category_name": "lightsaber",
        "is_producible": True,
        "is_purchasable": True,
        "type": "product",
        "purchase_uom": "pcs",
        "purchase_uom_conversion_rate": 1,
        "batch_tracked": False,
        "variants": [
            {
                "id": 1,
                "sku": "EM",
                "sales_price": 40,
                "product_id": 1,
                "purchase_price": 0,
                "type": "product",
                "created_at": "2020-10-23T10:37:05.085Z",
                "updated_at": "2020-10-23T10:37:05.085Z",
                "config_attributes": [
                    {
                        "config_name": "Type",
                        "config_value": "Standard"
                    }
                ]
            }
        ],
        "additional_info": "additional info",
        "created_at": "2020-10-23T10:37:05.085Z",
        "updated_at": "2020-10-23T10:37:05.085Z"
    }
    res = client.post("/v1/products/create", json=data)
    assert res.status_code == 200
    # assert session.query(Product).count() == 1
    # assert session.query(ProductVariant).count() == 1