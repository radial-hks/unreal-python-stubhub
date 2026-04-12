## WdpTransactionAPI Objects

```python
class WdpTransactionAPI(StandardApiClassBase)
```

Wdp Transaction API

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpTransactionAPI.h

<a id="unreal.WdpTransactionAPI.undo"></a>

#### undo

```python
def undo(undo_transaction_params: ParamsBase) -> Optional[ResultBase]
```

x.undo(undo_transaction_params) -> ResultBase or None
Undo

Args:
    undo_transaction_params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpTransactionAPI.set_transaction_enable"></a>

#### set\_transaction\_enable

```python
def set_transaction_enable(
        transaction_params: TransactionParams) -> Optional[ResultBase]
```

x.set_transaction_enable(transaction_params) -> ResultBase or None
APIs

Args:
    transaction_params (TransactionParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpTransactionAPI.rollback_transaction"></a>

#### rollback\_transaction

```python
def rollback_transaction(
        roll_back_transaction_params: ParamsBase) -> Optional[ResultBase]
```

x.rollback_transaction(roll_back_transaction_params) -> ResultBase or None
Rollback Transaction

Args:
    roll_back_transaction_params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpTransactionAPI.redo"></a>

#### redo

```python
def redo(redo_transaction_params: ParamsBase) -> Optional[ResultBase]
```

x.redo(redo_transaction_params) -> ResultBase or None
Redo

Args:
    redo_transaction_params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpTransactionAPI.get_transaction_list"></a>

#### get\_transaction\_list

```python
def get_transaction_list(
        get_transaction_list_params: ParamsBase
) -> Optional[GetTransactionResult]
```

x.get_transaction_list(get_transaction_list_params) -> GetTransactionResult or None
Get Transaction List

Args:
    get_transaction_list_params (ParamsBase): 

Returns:
    GetTransactionResult or None: 

    out_result (GetTransactionResult):

<a id="unreal.WdpTransactionAPI.create_transaction"></a>

#### create\_transaction

```python
def create_transaction(
    transaction_create_params_params: TransactionCreateParams
) -> Optional[ResultBase]
```

x.create_transaction(transaction_create_params_params) -> ResultBase or None
Create Transaction

Args:
    transaction_create_params_params (TransactionCreateParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpTransactionAPI.commit_transaction"></a>

#### commit\_transaction

```python
def commit_transaction(
        commit_transaction_params: ParamsBase) -> Optional[ResultBase]
```

x.commit_transaction(commit_transaction_params) -> ResultBase or None
Commit Transaction

Args:
    commit_transaction_params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpTransactionAPI.clear_transactions"></a>

#### clear\_transactions

```python
def clear_transactions(
        clear_transaction_params: ParamsBase) -> Optional[ResultBase]
```

x.clear_transactions(clear_transaction_params) -> ResultBase or None
Clear Transactions

Args:
    clear_transaction_params (ParamsBase): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.WdpTransactionAPI.can_undo"></a>

#### can\_undo

```python
def can_undo(
    can_undo_transaction_params: ParamsBase
) -> Optional[TransactionBoolResult]
```

x.can_undo(can_undo_transaction_params) -> TransactionBoolResult or None
Can Undo

Args:
    can_undo_transaction_params (ParamsBase): 

Returns:
    TransactionBoolResult or None: 

    out_result (TransactionBoolResult):

<a id="unreal.WdpTransactionAPI.can_redo"></a>

#### can\_redo

```python
def can_redo(
    can_redo_transaction_params: ParamsBase
) -> Optional[TransactionBoolResult]
```

x.can_redo(can_redo_transaction_params) -> TransactionBoolResult or None
Can Redo

Args:
    can_redo_transaction_params (ParamsBase): 

Returns:
    TransactionBoolResult or None: 

    out_result (TransactionBoolResult):

<a id="unreal.WdpWebSocketServer"></a>