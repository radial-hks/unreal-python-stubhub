## GeometryScriptIndexType Objects

```python
class GeometryScriptIndexType(EnumBase)
```

By default structs exposed to Python will use a per-UPROPERTY comparison. When this doesn't give correct results
(e.g., for structs with no properties, which will compare equal in all cases because there are no properties to
compare), it is necessary to define explicit equality operators and add the following WithIdenticalViaEquality trait.
Note that users can write blueprints/python scripts which pass these lists to many function calls so we would like to
avoid copying them (very slow if they have millions of elements) so we defined the equality operations using pointer
equality but this is potentially confusing if users expect that different lists with the same elements compare equal.

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

<a id="unreal.GeometryScriptIndexType.ANY"></a>

#### ANY

0: Index lists of Any type are compatible with any other index list type

<a id="unreal.GeometryScriptIndexType.TRIANGLE"></a>

#### TRIANGLE

1

<a id="unreal.GeometryScriptIndexType.EDGE"></a>

#### EDGE

2

<a id="unreal.GeometryScriptIndexType.VERTEX"></a>

#### VERTEX

3

<a id="unreal.GeometryScriptIndexType.MATERIAL_ID"></a>

#### MATERIAL_ID

4

<a id="unreal.GeometryScriptIndexType.POLYGROUP_ID"></a>

#### POLYGROUP_ID

5

<a id="unreal.GeometryScriptDebugMessageType"></a>