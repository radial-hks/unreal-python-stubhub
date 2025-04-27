## InAppPurchaseReceiptInfo2 Objects

```python
class InAppPurchaseReceiptInfo2(StructBase)
```

Micro-transaction purchase information

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item_id`` (str):  [Read-Write] The unique product identifier
- ``item_name`` (str):  [Read-Write] The item name
- ``transaction_identifier`` (str):  [Read-Write] the unique transaction identifier
- ``validation_info`` (str):  [Read-Write] the purchase validation information

<a id="unreal.InAppPurchaseReceiptInfo2.__init__"></a>

#### __init__

```python
def __init__(item_name: str = "",
             item_id: str = "",
             validation_info: str = "",
             transaction_identifier: str = "") -> None
```

<a id="unreal.InAppPurchaseReceiptInfo2.item_name"></a>

#### item_name

```python
@property
def item_name() -> str
```

(str):  [Read-Only] The item name

<a id="unreal.InAppPurchaseReceiptInfo2.item_id"></a>

#### item_id

```python
@property
def item_id() -> str
```

(str):  [Read-Only] The unique product identifier

<a id="unreal.InAppPurchaseReceiptInfo2.validation_info"></a>

#### validation_info

```python
@property
def validation_info() -> str
```

(str):  [Read-Only] the purchase validation information

<a id="unreal.InAppPurchaseReceiptInfo2.transaction_identifier"></a>

#### transaction_identifier

```python
@property
def transaction_identifier() -> str
```

(str):  [Read-Only] the unique transaction identifier

<a id="unreal.InputActionValue"></a>