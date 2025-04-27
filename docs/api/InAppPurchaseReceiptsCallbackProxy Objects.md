## InAppPurchaseReceiptsCallbackProxy Objects

```python
class InAppPurchaseReceiptsCallbackProxy(Object)
```

In App Purchase Receipts Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseReceiptsCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (OnlineProxyInAppReceiptsResult):  [Read-Write] Called when there is an unsuccessful In-App Purchase transaction
- ``on_success`` (OnlineProxyInAppReceiptsResult):  [Read-Write] Called when there is a successful In-App Purchase transaction

<a id="unreal.InAppPurchaseReceiptsCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> OnlineProxyInAppReceiptsResult
```

(OnlineProxyInAppReceiptsResult):  [Read-Write] Called when there is a successful In-App Purchase transaction

<a id="unreal.InAppPurchaseReceiptsCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: OnlineProxyInAppReceiptsResult) -> None
```

<a id="unreal.InAppPurchaseReceiptsCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> OnlineProxyInAppReceiptsResult
```

(OnlineProxyInAppReceiptsResult):  [Read-Write] Called when there is an unsuccessful In-App Purchase transaction

<a id="unreal.InAppPurchaseReceiptsCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: OnlineProxyInAppReceiptsResult) -> None
```

<a id="unreal.InAppPurchaseReceiptsCallbackProxy.create_proxy_object_for_in_app_purchase_restore_owned_products"></a>

#### create_proxy_object_for_in_app_purchase_restore_owned_products

```python
@classmethod
def create_proxy_object_for_in_app_purchase_restore_owned_products(
        cls, player_controller: PlayerController
) -> InAppPurchaseReceiptsCallbackProxy
```

X.create_proxy_object_for_in_app_purchase_restore_owned_products(player_controller) -> InAppPurchaseReceiptsCallbackProxy
Create Proxy Object for in App Purchase Restore Owned Products

Args:
    player_controller (PlayerController): 

Returns:
    InAppPurchaseReceiptsCallbackProxy:

<a id="unreal.InAppPurchaseReceiptsCallbackProxy.create_proxy_object_for_in_app_purchase_query_owned_products"></a>

#### create_proxy_object_for_in_app_purchase_query_owned_products

```python
@classmethod
def create_proxy_object_for_in_app_purchase_query_owned_products(
        cls, player_controller: PlayerController
) -> InAppPurchaseReceiptsCallbackProxy
```

X.create_proxy_object_for_in_app_purchase_query_owned_products(player_controller) -> InAppPurchaseReceiptsCallbackProxy
Create Proxy Object for in App Purchase Query Owned Products

Args:
    player_controller (PlayerController): 

Returns:
    InAppPurchaseReceiptsCallbackProxy:

<a id="unreal.InAppPurchaseReceiptsCallbackProxy.create_proxy_object_for_in_app_purchase_get_known_receipts"></a>

#### create_proxy_object_for_in_app_purchase_get_known_receipts

```python
@classmethod
def create_proxy_object_for_in_app_purchase_get_known_receipts(
        cls, player_controller: PlayerController
) -> InAppPurchaseReceiptsCallbackProxy
```

X.create_proxy_object_for_in_app_purchase_get_known_receipts(player_controller) -> InAppPurchaseReceiptsCallbackProxy
Create Proxy Object for in App Purchase Get Known Receipts

Args:
    player_controller (PlayerController): 

Returns:
    InAppPurchaseReceiptsCallbackProxy:

<a id="unreal.InAppPurchaseRestoreCallbackProxy2"></a>