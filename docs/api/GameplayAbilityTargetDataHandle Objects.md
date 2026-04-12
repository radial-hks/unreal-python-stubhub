## GameplayAbilityTargetDataHandle Objects

```python
class GameplayAbilityTargetDataHandle(StructBase)
```

Handle for Targeting Data. This servers two main purposes:
        -Avoid us having to copy around the full targeting data structure in Blueprints
        -Allows us to leverage polymorphism in the target data structure
        -Allows us to implement NetSerialize and replicate by value between clients/server

        -Avoid using UObjects could be used to give us polymorphism and by reference passing in blueprints.
        -However we would still be screwed when it came to replication

        -Replication by value
        -Pass by reference in blueprints
        -Polymophism in TargetData structure

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayAbilityTargetTypes.h

<a id="unreal.GameplayAbilityTargetDataHandle.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.GameplayTagRequirements"></a>