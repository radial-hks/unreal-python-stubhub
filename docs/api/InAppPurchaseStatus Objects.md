## InAppPurchaseStatus Objects

```python
class InAppPurchaseStatus(EnumBase)
```

State of a purchase transaction

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: InAppPurchaseDataTypes.h

<a id="unreal.InAppPurchaseStatus.INVALID"></a>

#### INVALID

0

<a id="unreal.InAppPurchaseStatus.FAILED"></a>

#### FAILED

1: purchase completed but failed

<a id="unreal.InAppPurchaseStatus.DEFERRED"></a>

#### DEFERRED

2: purchase has been deferred (neither failed nor completed)

<a id="unreal.InAppPurchaseStatus.CANCELED"></a>

#### CANCELED

3: purchase canceled by user

<a id="unreal.InAppPurchaseStatus.PURCHASED"></a>

#### PURCHASED

4: purchase succeeded

<a id="unreal.InAppPurchaseStatus.RESTORED"></a>

#### RESTORED

5: restore succeeded

<a id="unreal.ACLVisualFidelityChangeResult"></a>