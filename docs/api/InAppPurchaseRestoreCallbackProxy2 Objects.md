## InAppPurchaseRestoreCallbackProxy2 Objects

```python
class InAppPurchaseRestoreCallbackProxy2(Object)
```

In App Purchase Restore Callback Proxy 2

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseRestoreCallbackProxy2.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (InAppPurchaseRestoreResult2):  [Read-Write] Called when there is an unsuccessful In-App Purchase transaction
- ``on_success`` (InAppPurchaseRestoreResult2):  [Read-Write] Called when there is a successful In-App Purchase transaction

<a id="unreal.InAppPurchaseRestoreCallbackProxy2.on_success"></a>

#### on_success

```python
@property
def on_success() -> InAppPurchaseRestoreResult2
```

(InAppPurchaseRestoreResult2):  [Read-Write] Called when there is a successful In-App Purchase transaction

<a id="unreal.InAppPurchaseRestoreCallbackProxy2.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: InAppPurchaseRestoreResult2) -> None
```

<a id="unreal.InAppPurchaseRestoreCallbackProxy2.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> InAppPurchaseRestoreResult2
```

(InAppPurchaseRestoreResult2):  [Read-Write] Called when there is an unsuccessful In-App Purchase transaction

<a id="unreal.InAppPurchaseRestoreCallbackProxy2.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: InAppPurchaseRestoreResult2) -> None
```

<a id="unreal.InAppPurchaseRestoreCallbackProxy2.create_proxy_object_for_in_app_purchase_restore"></a>

#### create_proxy_object_for_in_app_purchase_restore

```python
@classmethod
def create_proxy_object_for_in_app_purchase_restore(
        cls, consumable_product_flags: Array[InAppPurchaseProductRequest2],
        player_controller: PlayerController
) -> InAppPurchaseRestoreCallbackProxy2
```

X.create_proxy_object_for_in_app_purchase_restore(consumable_product_flags, player_controller) -> InAppPurchaseRestoreCallbackProxy2
Kicks off a transaction for the provided product identifier
deprecated: Please use 'Restore Owned In-App Products' and remember to pass the output receipts to 'Finalize In-App Purchase Transaction' after being validated and processed

Args:
    consumable_product_flags (Array[InAppPurchaseProductRequest2]): 
    player_controller (PlayerController): 

Returns:
    InAppPurchaseRestoreCallbackProxy2:

<a id="unreal.JoinSessionCallbackProxy"></a>