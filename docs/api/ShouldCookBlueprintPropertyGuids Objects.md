## ShouldCookBlueprintPropertyGuids Objects

```python
class ShouldCookBlueprintPropertyGuids(EnumBase)
```

EShould Cook Blueprint Property Guids

**C++ Source:**

- **Module**: Engine
- **File**: Blueprint.h

<a id="unreal.ShouldCookBlueprintPropertyGuids.NO"></a>

#### NO

0: Don't cook the property GUIDs for this Blueprint

<a id="unreal.ShouldCookBlueprintPropertyGuids.YES"></a>

#### YES

1: Cook the property GUIDs for this Blueprint (see UCookerSettings::BlueprintPropertyGuidsCookingMethod)

<a id="unreal.ShouldCookBlueprintPropertyGuids.INHERIT"></a>

#### INHERIT

2: Inherit whether to cook the property GUIDs for this Blueprint from the parent Blueprint (behaves like 'No' if there is no parent Blueprint)

<a id="unreal.BlueprintCompileMode"></a>