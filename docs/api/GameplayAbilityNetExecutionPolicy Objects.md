## GameplayAbilityNetExecutionPolicy Objects

```python
class GameplayAbilityNetExecutionPolicy(EnumBase)
```

Where does an ability execute on the network. Does a client "ask and predict", "ask and wait", "don't ask (just do it)"

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTypes.h

<a id="unreal.GameplayAbilityNetExecutionPolicy.LOCAL_PREDICTED"></a>

#### LOCAL\_PREDICTED

0: Part of this ability runs predictively on the local client if there is one

<a id="unreal.GameplayAbilityNetExecutionPolicy.LOCAL_ONLY"></a>

#### LOCAL\_ONLY

1: This ability will only run on the client or server that has local control

<a id="unreal.GameplayAbilityNetExecutionPolicy.SERVER_INITIATED"></a>

#### SERVER\_INITIATED

2: This ability is initiated by the server, but will also run on the local client if one exists

<a id="unreal.GameplayAbilityNetExecutionPolicy.SERVER_ONLY"></a>

#### SERVER\_ONLY

3: This ability will only run on the server

<a id="unreal.GameplayAbilityNetSecurityPolicy"></a>