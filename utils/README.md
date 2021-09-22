# TastyIgniter API

## Generate Token

run the following command

```bash
    python gen_token.py
```

## Coupon

show existing coupons

```bash
    pyhton coupon.py --show
```

add new coupons

```bash
    pyhton coupon.py --add coupon_model.json 2 # Use coupon_model as template to generate 2 coupon clones
```

Sample file for coupon_model.json

```json
{
  "name": "API-test",
  "type": "F",
  "discount": 10,
  "redemptions": 10,
  "customer_redemptions": 5,
  "validity": "forever",
  "status": 1
}
```

| Name                   | Type      | Description                                                                                   |
| ---------------------- | --------- | --------------------------------------------------------------------------------------------- |
| `name`                 | string    | **Required**. The coupon's name.                                                              |
| `type`                 | character | **Required**. `F`for fixed value, `P` for percentage.                                         |
| `discount`             | float     | **Required**. The discount value or percentage.                                               |
| `redemptions`          | integer   | **Required**. The total number of times this coupon can be redeemed                           |
| `customer_redemptions` | integer   | **Required**. The number of times a specific customer can redeem this coupon                  |
| `validity`             | string    | One of: forever, fixed, period or recurring                                                   |
| `status`               | boolean   | Has the value `true` if the coupon is enabled or the value `false` if the coupon is disabled. |
