## InAppPurchaseQueryCallbackProxy2 Objects

```python
class InAppPurchaseQueryCallbackProxy2(Object)
```

In App Purchase Query Callback Proxy 2

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseQueryCallbackProxy2.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (InAppPurchaseQuery2Result):  [Read-Write] Called when there is an unsuccessful InAppPurchase query
- ``on_success`` (InAppPurchaseQuery2Result):  [Read-Write] Called when there is a successful InAppPurchase query

<a id="unreal.InAppPurchaseQueryCallbackProxy2.on_success"></a>

#### on_success

```python
@property
def on_success() -> InAppPurchaseQuery2Result
```

(InAppPurchaseQuery2Result):  [Read-Write] Called when there is a successful InAppPurchase query

<a id="unreal.InAppPurchaseQueryCallbackProxy2.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: InAppPurchaseQuery2Result) -> None
```

<a id="unreal.InAppPurchaseQueryCallbackProxy2.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> InAppPurchaseQuery2Result
```

(InAppPurchaseQuery2Result):  [Read-Write] Called when there is an unsuccessful InAppPurchase query

<a id="unreal.InAppPurchaseQueryCallbackProxy2.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: InAppPurchaseQuery2Result) -> None
```

<a id="unreal.InAppPurchaseQueryCallbackProxy2.create_proxy_object_for_in_app_purchase_query"></a>

#### create_proxy_object_for_in_app_purchase_query

```python
@classmethod
def create_proxy_object_for_in_app_purchase_query(
        cls, player_controller: PlayerController,
        product_identifiers: Array[str]) -> InAppPurchaseQueryCallbackProxy2
```

X.create_proxy_object_for_in_app_purchase_query(player_controller, product_identifiers) -> InAppPurchaseQueryCallbackProxy2
Queries a InAppPurchase for an integer value

Args:
    player_controller (PlayerController): 
    product_identifiers (Array[str]): 

Returns:
    InAppPurchaseQueryCallbackProxy2:

<a id="unreal.InAppPurchaseReceiptsCallbackProxy"></a>