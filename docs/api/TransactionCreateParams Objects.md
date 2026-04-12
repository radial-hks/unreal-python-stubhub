## TransactionCreateParams Objects

```python
class TransactionCreateParams(ParamsBase)
```

Transaction Create Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpTransactionAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``can_commit`` (bool):  [Read-Write]
- ``can_undo`` (bool):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``transaction_group`` (bool):  [Read-Write]
- ``transaction_name`` (str):  [Read-Write]

<a id="unreal.TransactionCreateParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(transaction_name: str = "",
             can_commit: bool = False,
             can_undo: bool = False,
             transaction_group: bool = False) -> None
```

<a id="unreal.TransactionCreateParams.transaction_name"></a>

#### transaction\_name

```python
@property
def transaction_name() -> str
```

(str):  [Read-Write]

<a id="unreal.TransactionCreateParams.transaction_name"></a>

#### transaction\_name

```python
@transaction_name.setter
def transaction_name(value: str) -> None
```

<a id="unreal.TransactionCreateParams.can_commit"></a>

#### can\_commit

```python
@property
def can_commit() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TransactionCreateParams.can_commit"></a>

#### can\_commit

```python
@can_commit.setter
def can_commit(value: bool) -> None
```

<a id="unreal.TransactionCreateParams.can_undo"></a>

#### can\_undo

```python
@property
def can_undo() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TransactionCreateParams.can_undo"></a>

#### can\_undo

```python
@can_undo.setter
def can_undo(value: bool) -> None
```

<a id="unreal.TransactionCreateParams.transaction_group"></a>

#### transaction\_group

```python
@property
def transaction_group() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TransactionCreateParams.transaction_group"></a>

#### transaction\_group

```python
@transaction_group.setter
def transaction_group(value: bool) -> None
```

<a id="unreal.GetTransactionResult"></a>