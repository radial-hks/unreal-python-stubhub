## InAppPurchaseProductRequest2 Objects

```python
class InAppPurchaseProductRequest2(StructBase)
```

Micro-transaction request information

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseDataTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_consumable`` (bool):  [Read-Write] Flag to determine whether this is a consumable purchase, or not.
- ``product_identifier`` (str):  [Read-Write] The unique product identifier that matches the one from your targeted store.

<a id="unreal.InAppPurchaseProductRequest2.__init__"></a>

#### __init__

```python
def __init__(product_identifier: str = "",
             is_consumable: bool = False) -> None
```

<a id="unreal.InAppPurchaseProductRequest2.product_identifier"></a>

#### product_identifier

```python
@property
def product_identifier() -> str
```

(str):  [Read-Write] The unique product identifier that matches the one from your targeted store.

<a id="unreal.InAppPurchaseProductRequest2.product_identifier"></a>

#### product_identifier

```python
@product_identifier.setter
def product_identifier(value: str) -> None
```

<a id="unreal.InAppPurchaseProductRequest2.is_consumable"></a>

#### is_consumable

```python
@property
def is_consumable() -> bool
```

(bool):  [Read-Write] Flag to determine whether this is a consumable purchase, or not.

<a id="unreal.InAppPurchaseProductRequest2.is_consumable"></a>

#### is_consumable

```python
@is_consumable.setter
def is_consumable(value: bool) -> None
```

<a id="unreal.InAppPurchaseProductInfo2"></a>