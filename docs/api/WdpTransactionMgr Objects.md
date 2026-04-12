## WdpTransactionMgr Objects

```python
class WdpTransactionMgr(Object)
```

Wdp Transaction Mgr

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: TransactionMgr.h

<a id="unreal.WdpTransactionMgr.set_undo_stack_size"></a>

#### set\_undo\_stack\_size

```python
def set_undo_stack_size(size: int) -> bool
```

x.set_undo_stack_size(size) -> bool
Set Undo Stack Size

Args:
    size (int32): 

Returns:
    bool:

<a id="unreal.WdpTransactionMgr.set_transaction_feature_enable"></a>

#### set\_transaction\_feature\_enable

```python
def set_transaction_feature_enable(bool: bool) -> bool
```

x.set_transaction_feature_enable(bool) -> bool
Set Transaction Feature Enable

Args:
    bool (bool): 

Returns:
    bool:

<a id="unreal.WdpTransactionMgr.is_transaction_feature_enable"></a>

#### is\_transaction\_feature\_enable

```python
def is_transaction_feature_enable() -> bool
```

x.is_transaction_feature_enable() -> bool
Is Transaction Feature Enable

Returns:
    bool:

<a id="unreal.WdpTransactionMgr.get_undo_stack_size"></a>

#### get\_undo\_stack\_size

```python
def get_undo_stack_size() -> int
```

x.get_undo_stack_size() -> int32
Get Undo Stack Size

Returns:
    int32:

<a id="unreal.WdpTransactionMgr.get_transaction_list"></a>

#### get\_transaction\_list

```python
def get_transaction_list() -> Array[str]
```

x.get_transaction_list() -> Array[str]
Get Transaction List

Returns:
    Array[str]:

<a id="unreal.WdpTransactionMgr.get_in_progress_tc_id"></a>

#### get\_in\_progress\_tc\_id

```python
def get_in_progress_tc_id() -> Guid
```

x.get_in_progress_tc_id() -> Guid
Get in Progress Tc Id

Returns:
    Guid:

<a id="unreal.WdpTransactionMgr.get_in_progress_tc_group_id"></a>

#### get\_in\_progress\_tc\_group\_id

```python
def get_in_progress_tc_group_id() -> Guid
```

x.get_in_progress_tc_group_id() -> Guid
Get in Progress Tc Group Id

Returns:
    Guid:

<a id="unreal.WdpTransactionMgr.get_current_transaction_index"></a>

#### get\_current\_transaction\_index

```python
def get_current_transaction_index() -> int
```

x.get_current_transaction_index() -> int32
Get Current Transaction Index

Returns:
    int32:

<a id="unreal.WdpTransactionMgr.create_transaction_group"></a>

#### create\_transaction\_group

```python
def create_transaction_group(name: str,
                             can_undo: bool = True,
                             can_assemble: bool = True) -> Guid
```

x.create_transaction_group(name, can_undo=True, can_assemble=True) -> Guid
Create Transaction Group

Args:
    name (str): 
    can_undo (bool): 
    can_assemble (bool): 

Returns:
    Guid:

<a id="unreal.WdpTransactionMgr.create_transaction"></a>

#### create\_transaction

```python
def create_transaction(name: str,
                       can_undo: bool = True,
                       can_commit: bool = True) -> Guid
```

x.create_transaction(name, can_undo=True, can_commit=True) -> Guid
Create Transaction

Args:
    name (str): 
    can_undo (bool): 
    can_commit (bool): 

Returns:
    Guid:

<a id="unreal.WdpTransactionMgr.can_undo"></a>

#### can\_undo

```python
def can_undo() -> bool
```

x.can_undo() -> bool
Can Undo

Returns:
    bool:

<a id="unreal.WdpTransactionMgr.can_redo"></a>

#### can\_redo

```python
def can_redo() -> bool
```

x.can_redo() -> bool
Can Redo

Returns:
    bool:

<a id="unreal.UniqueEntityBase"></a>