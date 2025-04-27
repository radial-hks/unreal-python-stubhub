## InAppPurchaseFinalizeProxy Objects

```python
class InAppPurchaseFinalizeProxy(Object)
```

In App Purchase Finalize Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseFinalizeProxy.h

<a id="unreal.InAppPurchaseFinalizeProxy.create_proxy_object_for_in_app_purchase_finalize"></a>

#### create_proxy_object_for_in_app_purchase_finalize

```python
@classmethod
def create_proxy_object_for_in_app_purchase_finalize(
        cls, app_purchase_receipt: InAppPurchaseReceiptInfo2,
        player_controller: PlayerController) -> InAppPurchaseFinalizeProxy
```

X.create_proxy_object_for_in_app_purchase_finalize(app_purchase_receipt, player_controller) -> InAppPurchaseFinalizeProxy
Finalizes a transaction for the provided transaction identifier

Args:
    app_purchase_receipt (InAppPurchaseReceiptInfo2): 
    player_controller (PlayerController): 

Returns:
    InAppPurchaseFinalizeProxy:

<a id="unreal.InAppPurchaseQueryCallbackProxy2"></a>