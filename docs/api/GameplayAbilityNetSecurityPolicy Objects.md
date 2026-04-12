## GameplayAbilityNetSecurityPolicy Objects

```python
class GameplayAbilityNetSecurityPolicy(EnumBase)
```

What protections does this ability have? Should the client be allowed to request changes to the execution of the ability?

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTypes.h

<a id="unreal.GameplayAbilityNetSecurityPolicy.CLIENT_OR_SERVER"></a>

#### CLIENT\_OR\_SERVER

0: No security requirements. Client or server can trigger execution and termination of this ability freely.

<a id="unreal.GameplayAbilityNetSecurityPolicy.SERVER_ONLY_EXECUTION"></a>

#### SERVER\_ONLY\_EXECUTION

1: A client requesting execution of this ability will be ignored by the server. Clients can still request that the server cancel or end this ability.

<a id="unreal.GameplayAbilityNetSecurityPolicy.SERVER_ONLY_TERMINATION"></a>

#### SERVER\_ONLY\_TERMINATION

2: A client requesting cancellation or ending of this ability will be ignored by the server. Clients can still request execution of the ability.

<a id="unreal.GameplayAbilityNetSecurityPolicy.SERVER_ONLY"></a>

#### SERVER\_ONLY

3: Server controls both execution and termination of this ability. A client making any requests will be ignored.

<a id="unreal.GameplayAbilityReplicationPolicy"></a>