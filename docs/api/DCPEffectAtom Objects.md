## DCPEffectAtom Objects

```python
class DCPEffectAtom(EntityAtomBase)
```

DCPEffect Atom

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPEffectAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bim_highlight_style`` (HierarchyMeshHighlightStyle):  [Read-Write]
- ``dcp_effect_setting_names`` (Map[DCPEffectMaterialType, str]):  [Read-Write]

<a id="unreal.DCPEffectAtom.dcp_effect_setting_names"></a>

#### dcp\_effect\_setting\_names

```python
@property
def dcp_effect_setting_names() -> Map[DCPEffectMaterialType, str]
```

(Map[DCPEffectMaterialType, str]):  [Read-Only]

<a id="unreal.DCPEffectAtom.bim_highlight_style"></a>

#### bim\_highlight\_style

```python
@property
def bim_highlight_style() -> HierarchyMeshHighlightStyle
```

(HierarchyMeshHighlightStyle):  [Read-Only]

<a id="unreal.HierarchyMeshEntityAtom"></a>