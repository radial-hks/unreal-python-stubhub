## TransactionParams Objects

```python
class TransactionParams(ParamsBase)
```

Transaction Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpTransactionAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enable_transaction`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.TransactionParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(enable_transaction: bool = False) -> None
```

<a id="unreal.TransactionParams.enable_transaction"></a>

#### enable\_transaction

```python
@property
def enable_transaction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TransactionParams.enable_transaction"></a>

#### enable\_transaction

```python
@enable_transaction.setter
def enable_transaction(value: bool) -> None
```

<a id="unreal.TransactionCreateParams"></a>