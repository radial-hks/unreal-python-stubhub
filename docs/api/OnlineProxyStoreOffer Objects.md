## OnlineProxyStoreOffer Objects

```python
class OnlineProxyStoreOffer(StructBase)
```

Offer entry for display from online store

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseQueryCallbackProxy2.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``currency_code`` (str):  [Read-Write] Price currency code
- ``description`` (Text):  [Read-Write] Short description for display
- ``discount_type`` (OnlineProxyStoreOfferDiscountType):  [Read-Write] Type of discount currently running on this offer (if any)
- ``dynamic_fields`` (Map[str, str]):  [Read-Write]
- ``expiration_date`` (DateTime):  [Read-Write] Date this information is no longer valid (maybe due to sale ending, etc)
- ``long_description`` (Text):  [Read-Write] Full description for display
- ``numeric_price`` (int32):  [Read-Write] Final-Price (Post-Sales/Discounts) in numeric form for comparison/sorting
- ``offer_id`` (str):  [Read-Write] Unique offer identifier
- ``price_text`` (Text):  [Read-Write] Final-Pricing (Post-Sales/Discounts) as text for display
- ``regular_price`` (int32):  [Read-Write] Regular non-sale price in numeric form for comparison/sorting
- ``regular_price_text`` (Text):  [Read-Write] Regular non-sale price as text for display
- ``release_date`` (DateTime):  [Read-Write] Date the offer was released
- ``title`` (Text):  [Read-Write] Title for display

<a id="unreal.OnlineProxyStoreOffer.__init__"></a>

#### __init__

```python
def __init__(
        offer_id: str = "",
        title: Text = "",
        description: Text = "",
        long_description: Text = "",
        regular_price_text: Text = "",
        regular_price: int = 0,
        price_text: Text = "",
        numeric_price: int = 0,
        currency_code: str = "",
        release_date: DateTime = [],
        expiration_date: DateTime = [],
        discount_type:
    OnlineProxyStoreOfferDiscountType = OnlineProxyStoreOfferDiscountType.
    NOT_ON_SALE,
        dynamic_fields: Map[str, str] = {}) -> None
```

<a id="unreal.OnlineProxyStoreOffer.offer_id"></a>

#### offer_id

```python
@property
def offer_id() -> str
```

(str):  [Read-Only] Unique offer identifier

<a id="unreal.OnlineProxyStoreOffer.title"></a>

#### title

```python
@property
def title() -> Text
```

(Text):  [Read-Only] Title for display

<a id="unreal.OnlineProxyStoreOffer.description"></a>

#### description

```python
@property
def description() -> Text
```

(Text):  [Read-Only] Short description for display

<a id="unreal.OnlineProxyStoreOffer.long_description"></a>

#### long_description

```python
@property
def long_description() -> Text
```

(Text):  [Read-Only] Full description for display

<a id="unreal.OnlineProxyStoreOffer.regular_price_text"></a>

#### regular_price_text

```python
@property
def regular_price_text() -> Text
```

(Text):  [Read-Only] Regular non-sale price as text for display

<a id="unreal.OnlineProxyStoreOffer.regular_price"></a>

#### regular_price

```python
@property
def regular_price() -> int
```

(int32):  [Read-Only] Regular non-sale price in numeric form for comparison/sorting

<a id="unreal.OnlineProxyStoreOffer.price_text"></a>

#### price_text

```python
@property
def price_text() -> Text
```

(Text):  [Read-Only] Final-Pricing (Post-Sales/Discounts) as text for display

<a id="unreal.OnlineProxyStoreOffer.numeric_price"></a>

#### numeric_price

```python
@property
def numeric_price() -> int
```

(int32):  [Read-Only] Final-Price (Post-Sales/Discounts) in numeric form for comparison/sorting

<a id="unreal.OnlineProxyStoreOffer.currency_code"></a>

#### currency_code

```python
@property
def currency_code() -> str
```

(str):  [Read-Only] Price currency code

<a id="unreal.OnlineProxyStoreOffer.release_date"></a>

#### release_date

```python
@property
def release_date() -> DateTime
```

(DateTime):  [Read-Only] Date the offer was released

<a id="unreal.OnlineProxyStoreOffer.expiration_date"></a>

#### expiration_date

```python
@property
def expiration_date() -> DateTime
```

(DateTime):  [Read-Only] Date this information is no longer valid (maybe due to sale ending, etc)

<a id="unreal.OnlineProxyStoreOffer.discount_type"></a>

#### discount_type

```python
@property
def discount_type() -> OnlineProxyStoreOfferDiscountType
```

(OnlineProxyStoreOfferDiscountType):  [Read-Only] Type of discount currently running on this offer (if any)

<a id="unreal.OnlineProxyStoreOffer.dynamic_fields"></a>

#### dynamic_fields

```python
@property
def dynamic_fields() -> Map[str, str]
```

(Map[str, str]):  [Read-Only]

<a id="unreal.InAppPurchaseRestoreInfo2"></a>