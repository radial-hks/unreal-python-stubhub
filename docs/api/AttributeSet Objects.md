## AttributeSet Objects

```python
class AttributeSet(Object)
```

Defines the set of all GameplayAttributes for your game
Games should subclass this and add FGameplayAttributeData properties to represent attributes like health, damage, etc
AttributeSets are added to the actors as subobjects, and then registered with the AbilitySystemComponent
It often desired to have several sets per project that inherit from each other
You could make a base health set, then have a player set that inherits from it and adds more attributes

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AttributeSet.h

<a id="unreal.AbilitySystemTestAttributeSet"></a>