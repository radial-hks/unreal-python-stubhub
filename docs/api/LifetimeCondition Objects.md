## LifetimeCondition Objects

```python
class LifetimeCondition(EnumBase)
```

Secondary condition to check before considering the replication of a lifetime property.

**C++ Source:**

- **Module**: CoreUObject
- **File**: CoreNetTypes.h

<a id="unreal.LifetimeCondition.COND_NONE"></a>

#### COND_NONE

0

<a id="unreal.LifetimeCondition.COND_INITIAL_ONLY"></a>

#### COND_INITIAL_ONLY

1: This property has no condition, and will send anytime it changes

<a id="unreal.LifetimeCondition.COND_OWNER_ONLY"></a>

#### COND_OWNER_ONLY

2: This property will only attempt to send on the initial bunch

<a id="unreal.LifetimeCondition.COND_SKIP_OWNER"></a>

#### COND_SKIP_OWNER

3: This property will only send to the actor's owner

<a id="unreal.LifetimeCondition.COND_SIMULATED_ONLY"></a>

#### COND_SIMULATED_ONLY

4: This property send to every connection EXCEPT the owner

<a id="unreal.LifetimeCondition.COND_AUTONOMOUS_ONLY"></a>

#### COND_AUTONOMOUS_ONLY

5: This property will only send to simulated actors

<a id="unreal.LifetimeCondition.COND_SIMULATED_OR_PHYSICS"></a>

#### COND_SIMULATED_OR_PHYSICS

6: This property will only send to autonomous actors

<a id="unreal.LifetimeCondition.COND_INITIAL_OR_OWNER"></a>

#### COND_INITIAL_OR_OWNER

7: This property will send to simulated OR bRepPhysics actors

<a id="unreal.LifetimeCondition.COND_CUSTOM"></a>

#### COND_CUSTOM

8: This property will send on the initial packet, or to the actors owner

<a id="unreal.LifetimeCondition.COND_REPLAY_OR_OWNER"></a>

#### COND_REPLAY_OR_OWNER

9: This property has no particular condition, but wants the ability to toggle on/off via SetCustomIsActiveOverride

<a id="unreal.LifetimeCondition.COND_REPLAY_ONLY"></a>

#### COND_REPLAY_ONLY

10: This property will only send to the replay connection, or to the actors owner

<a id="unreal.LifetimeCondition.COND_SIMULATED_ONLY_NO_REPLAY"></a>

#### COND_SIMULATED_ONLY_NO_REPLAY

11: This property will only send to the replay connection

<a id="unreal.LifetimeCondition.COND_SIMULATED_OR_PHYSICS_NO_REPLAY"></a>

#### COND_SIMULATED_OR_PHYSICS_NO_REPLAY

12: This property will send to actors only, but not to replay connections

<a id="unreal.LifetimeCondition.COND_SKIP_REPLAY"></a>

#### COND_SKIP_REPLAY

13: This property will send to simulated Or bRepPhysics actors, but not to replay connections

<a id="unreal.DataValidationUsecase"></a>