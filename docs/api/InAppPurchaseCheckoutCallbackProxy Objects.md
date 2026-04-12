## InAppPurchaseCheckoutCallbackProxy Objects

```python
class InAppPurchaseCheckoutCallbackProxy(Object)
```

In App Purchase Checkout Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseCheckoutCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (OnlineProxyInAppCheckoutResult):  [Read-Write] Called when there is an unsuccessful In-App Purchase transaction
- ``on_success`` (OnlineProxyInAppCheckoutResult):  [Read-Write] Called when there is a successful In-App Purchase transaction

<a id="unreal.InAppPurchaseCheckoutCallbackProxy.on_success"></a>

#### on\_success

```python
@property
def on_success() -> OnlineProxyInAppCheckoutResult
```

(OnlineProxyInAppCheckoutResult):  [Read-Write] Called when there is a successful In-App Purchase transaction

<a id="unreal.InAppPurchaseCheckoutCallbackProxy.on_success"></a>

#### on\_success

```python
@on_success.setter
def on_success(value: OnlineProxyInAppCheckoutResult) -> None
```

<a id="unreal.InAppPurchaseCheckoutCallbackProxy.on_failure"></a>

#### on\_failure

```python
@property
def on_failure() -> OnlineProxyInAppCheckoutResult
```

(OnlineProxyInAppCheckoutResult):  [Read-Write] Called when there is an unsuccessful In-App Purchase transaction

<a id="unreal.InAppPurchaseCheckoutCallbackProxy.on_failure"></a>

#### on\_failure

```python
@on_failure.setter
def on_failure(value: OnlineProxyInAppCheckoutResult) -> None
```

<a id="unreal.InAppPurchaseCheckoutCallbackProxy.create_proxy_object_for_in_app_purchase_checkout"></a>

#### create\_proxy\_object\_for\_in\_app\_purchase\_checkout

```python
@classmethod
def create_proxy_object_for_in_app_purchase_checkout(
    cls, player_controller: PlayerController,
    product_request: InAppPurchaseProductRequest2
) -> InAppPurchaseCheckoutCallbackProxy
```

X.create_proxy_object_for_in_app_purchase_checkout(player_controller, product_request) -> InAppPurchaseCheckoutCallbackProxy
Kicks off a transaction for the provided product identifier

Args:
    player_controller (PlayerController): 
    product_request (InAppPurchaseProductRequest2): 

Returns:
    InAppPurchaseCheckoutCallbackProxy:

<a id="unreal.InAppPurchaseFinalizeProxy"></a>