## InAppPurchaseProductInfo2 Objects

```python
class InAppPurchaseProductInfo2(StructBase)
```

Micro-transaction purchase information

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseCallbackProxy2.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``currency_code`` (str):  [Read-Write] The localized currency code of the price
- ``currency_symbol`` (str):  [Read-Write] The localized currency symbol of the price
- ``decimal_separator`` (str):  [Read-Write] The localized decimal separator used in the price
- ``display_description`` (str):  [Read-Write] The localized display description name
- ``display_name`` (str):  [Read-Write] The localized display name
- ``display_price`` (str):  [Read-Write] The localized display price name
- ``dynamic_fields`` (Map[str, str]):  [Read-Write] Dynamic fields from raw Json data.
- ``grouping_separator`` (str):  [Read-Write] The localized grouping separator of the price
- ``identifier`` (str):  [Read-Write] The unique product identifier
- ``raw_price`` (float):  [Read-Write] Raw price without currency code and symbol
- ``receipt_data`` (str):  [Read-Write] Opaque receipt data for the transaction
- ``transaction_identifier`` (str):  [Read-Write] the unique transaction identifier

<a id="unreal.InAppPurchaseProductInfo2.__init__"></a>

#### __init__

```python
def __init__(identifier: str = "",
             transaction_identifier: str = "",
             display_name: str = "",
             display_description: str = "",
             display_price: str = "",
             raw_price: float = 0.000000,
             currency_code: str = "",
             currency_symbol: str = "",
             decimal_separator: str = "",
             grouping_separator: str = "",
             receipt_data: str = "",
             dynamic_fields: Map[str, str] = {}) -> None
```

<a id="unreal.InAppPurchaseProductInfo2.identifier"></a>

#### identifier

```python
@property
def identifier() -> str
```

(str):  [Read-Only] The unique product identifier

<a id="unreal.InAppPurchaseProductInfo2.transaction_identifier"></a>

#### transaction_identifier

```python
@property
def transaction_identifier() -> str
```

(str):  [Read-Only] the unique transaction identifier

<a id="unreal.InAppPurchaseProductInfo2.display_name"></a>

#### display_name

```python
@property
def display_name() -> str
```

(str):  [Read-Only] The localized display name

<a id="unreal.InAppPurchaseProductInfo2.display_description"></a>

#### display_description

```python
@property
def display_description() -> str
```

(str):  [Read-Only] The localized display description name

<a id="unreal.InAppPurchaseProductInfo2.display_price"></a>

#### display_price

```python
@property
def display_price() -> str
```

(str):  [Read-Only] The localized display price name

<a id="unreal.InAppPurchaseProductInfo2.raw_price"></a>

#### raw_price

```python
@property
def raw_price() -> float
```

(float):  [Read-Only] Raw price without currency code and symbol

<a id="unreal.InAppPurchaseProductInfo2.currency_code"></a>

#### currency_code

```python
@property
def currency_code() -> str
```

(str):  [Read-Only] The localized currency code of the price

<a id="unreal.InAppPurchaseProductInfo2.currency_symbol"></a>

#### currency_symbol

```python
@property
def currency_symbol() -> str
```

(str):  [Read-Only] The localized currency symbol of the price

<a id="unreal.InAppPurchaseProductInfo2.decimal_separator"></a>

#### decimal_separator

```python
@property
def decimal_separator() -> str
```

(str):  [Read-Only] The localized decimal separator used in the price

<a id="unreal.InAppPurchaseProductInfo2.grouping_separator"></a>

#### grouping_separator

```python
@property
def grouping_separator() -> str
```

(str):  [Read-Only] The localized grouping separator of the price

<a id="unreal.InAppPurchaseProductInfo2.receipt_data"></a>

#### receipt_data

```python
@property
def receipt_data() -> str
```

(str):  [Read-Only] Opaque receipt data for the transaction

<a id="unreal.InAppPurchaseProductInfo2.dynamic_fields"></a>

#### dynamic_fields

```python
@property
def dynamic_fields() -> Map[str, str]
```

(Map[str, str]):  [Read-Only] Dynamic fields from raw Json data.

<a id="unreal.VariantDependency"></a>