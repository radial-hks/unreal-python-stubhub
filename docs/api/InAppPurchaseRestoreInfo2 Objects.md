## InAppPurchaseRestoreInfo2 Objects

```python
class InAppPurchaseRestoreInfo2(StructBase)
```

Micro-transaction purchase information

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseRestoreCallbackProxy2.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``item_id`` (str):  [Read-Write] The unique product identifier
- ``item_name`` (str):  [Read-Write] The item name
- ``validation_info`` (str):  [Read-Write] the unique transaction identifier

<a id="unreal.InAppPurchaseRestoreInfo2.__init__"></a>

#### __init__

```python
def __init__(item_name: str = "",
             item_id: str = "",
             validation_info: str = "") -> None
```

<a id="unreal.InAppPurchaseRestoreInfo2.item_name"></a>

#### item_name

```python
@property
def item_name() -> str
```

(str):  [Read-Only] The item name

<a id="unreal.InAppPurchaseRestoreInfo2.item_id"></a>

#### item_id

```python
@property
def item_id() -> str
```

(str):  [Read-Only] The unique product identifier

<a id="unreal.InAppPurchaseRestoreInfo2.validation_info"></a>

#### validation_info

```python
@property
def validation_info() -> str
```

(str):  [Read-Only] the unique transaction identifier

<a id="unreal.InAppPurchaseReceiptInfo2"></a>