## AvaNormalModifierSplitMethod Objects

```python
class AvaNormalModifierSplitMethod(EnumBase)
```

EAva Normal Modifier Split Method

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaNormalModifier.h

<a id="unreal.AvaNormalModifierSplitMethod.NONE"></a>

#### NONE

0: Do not split, leave as it is

<a id="unreal.AvaNormalModifierSplitMethod.VERTEX"></a>

#### VERTEX

1: Each vertex will have a split normal between tris

<a id="unreal.AvaNormalModifierSplitMethod.TRIANGLE"></a>

#### TRIANGLE

2: Shared vertex between triangles will have a split normal

<a id="unreal.AvaNormalModifierSplitMethod.POLY_GROUP"></a>

#### POLY_GROUP

3: Vertices of a same face grouped together will have a split normal

<a id="unreal.AvaNormalModifierSplitMethod.THRESHOLD"></a>

#### THRESHOLD

4: Vertices above a certain angle threshold will have a split normal

<a id="unreal.AvaOutlineMode"></a>