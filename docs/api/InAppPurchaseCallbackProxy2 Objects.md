## InAppPurchaseCallbackProxy2 Objects

```python
class InAppPurchaseCallbackProxy2(Object)
```

In App Purchase Callback Proxy 2

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseCallbackProxy2.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (InAppPurchaseResult2):  [Read-Write] Called when there is an unsuccessful In-App Purchase transaction
- ``on_success`` (InAppPurchaseResult2):  [Read-Write] Called when there is a successful In-App Purchase transaction

<a id="unreal.InAppPurchaseCallbackProxy2.on_success"></a>

#### on_success

```python
@property
def on_success() -> InAppPurchaseResult2
```

(InAppPurchaseResult2):  [Read-Write] Called when there is a successful In-App Purchase transaction

<a id="unreal.InAppPurchaseCallbackProxy2.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: InAppPurchaseResult2) -> None
```

<a id="unreal.InAppPurchaseCallbackProxy2.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> InAppPurchaseResult2
```

(InAppPurchaseResult2):  [Read-Write] Called when there is an unsuccessful In-App Purchase transaction

<a id="unreal.InAppPurchaseCallbackProxy2.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: InAppPurchaseResult2) -> None
```

<a id="unreal.InAppPurchaseCallbackProxy2.create_proxy_object_for_in_app_purchase_unprocessed_purchases"></a>

#### create_proxy_object_for_in_app_purchase_unprocessed_purchases

```python
@classmethod
def create_proxy_object_for_in_app_purchase_unprocessed_purchases(
        cls,
        player_controller: PlayerController) -> InAppPurchaseCallbackProxy2
```

X.create_proxy_object_for_in_app_purchase_unprocessed_purchases(player_controller) -> InAppPurchaseCallbackProxy2
Create Proxy Object for in App Purchase Unprocessed Purchases
deprecated: Please use 'Get known In-App Receipts' and remember to pass the output receipts to 'Finalize In-App Purchase Transaction' after being validated and processed

Args:
    player_controller (PlayerController): 

Returns:
    InAppPurchaseCallbackProxy2:

<a id="unreal.InAppPurchaseCallbackProxy2.create_proxy_object_for_in_app_purchase_query_owned"></a>

#### create_proxy_object_for_in_app_purchase_query_owned

```python
@classmethod
def create_proxy_object_for_in_app_purchase_query_owned(
        cls,
        player_controller: PlayerController) -> InAppPurchaseCallbackProxy2
```

X.create_proxy_object_for_in_app_purchase_query_owned(player_controller) -> InAppPurchaseCallbackProxy2
Create Proxy Object for in App Purchase Query Owned
deprecated: Please use 'Query for Owned In-App Products' and remember to pass the output receipts to 'Finalize In-App Purchase Transaction' after being validated and processed

Args:
    player_controller (PlayerController): 

Returns:
    InAppPurchaseCallbackProxy2:

<a id="unreal.InAppPurchaseCallbackProxy2.create_proxy_object_for_in_app_purchase"></a>

#### create_proxy_object_for_in_app_purchase

```python
@classmethod
def create_proxy_object_for_in_app_purchase(
    cls, player_controller: PlayerController,
    product_request: InAppPurchaseProductRequest2
) -> InAppPurchaseCallbackProxy2
```

X.create_proxy_object_for_in_app_purchase(player_controller, product_request) -> InAppPurchaseCallbackProxy2
Kicks off a transaction for the provided product identifier
deprecated: Please use 'Start an In-App Purchase' and remember to pass the output receipts to 'Finalize In-App Purchase Transaction' after being validated and processed

Args:
    player_controller (PlayerController): 
    product_request (InAppPurchaseProductRequest2): 

Returns:
    InAppPurchaseCallbackProxy2:

<a id="unreal.InAppPurchaseCheckoutCallbackProxy"></a>