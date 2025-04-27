## LevelVisibilityDirtyMode Objects

```python
class LevelVisibilityDirtyMode(EnumBase)
```

ELevel Visibility Dirty Mode

**C++ Source:**

- **Module**: UnrealEd
- **File**: EditorLevelUtils.h

<a id="unreal.LevelVisibilityDirtyMode.MODIFY_ON_CHANGE"></a>

#### MODIFY_ON_CHANGE

0: Use when the user is causing the visibility change.  Will update transaction state and mark the package dirty.

<a id="unreal.LevelVisibilityDirtyMode.DONT_MODIFY"></a>

#### DONT_MODIFY

1: Use when code is causing the visibility change.

<a id="unreal.AssetEditorOpenLocation"></a>