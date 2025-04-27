## DisplayClusterEditorPropertyReference Objects

```python
class DisplayClusterEditorPropertyReference(StructBase)
```

A dummy structure used to reference properties of subobjects to be displayed at the root level in a details panel.

When placed within an Unreal class or struct, the property reference is replaced with the referenced property in the
type's details panel. The display name, tooltip, category, and accessiblity of the property reference will be applied
to the referenced property when provided, overwriting the property's own specifiers. If the property path contains lists
(arrays, maps, or sets), then each element of the list will be iterated over, and all properties within that list will
be displayed together in a group.

Use the PropertyPath metadata specifier to specify the path to the referenced property, relative to the object that owns
the property reference.

Additionally, this type supports using property paths within its EditCondition specifier, allowing the edit condition
of the referenced property within a details panel to depend on other referenced properties. The && operator is supported,
allowing multiple property paths to be used to construct the edit condition.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterEditorPropertyReference.h

<a id="unreal.DisplayClusterEditorPropertyReference.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.DisplayClusterComponentRef"></a>