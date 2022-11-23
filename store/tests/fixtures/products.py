import pytest


@pytest.fixture
def product_data():
    return {
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
        "variants": [
            {
                "id": 1,
                "sku": "EM",
                "sales_price": 40,
                "product_id": 1,
                "purchase_price": 0,
                "type": "product",
                "created_at": "2020-10-23T10:37:05.085000Z",
                "updated_at": "2020-10-23T10:37:05.085000Z",
                "config_attributes": [
                    {"config_name": "Type", "config_value": "Standard"}
                ],
            }
        ],
        "additional_info": "additional info",
        "created_at": "2020-10-23T10:37:05.085000Z",
        "updated_at": "2020-10-23T10:37:05.085000Z",
    }
