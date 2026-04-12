## Text3DComponent Objects

```python
class Text3DComponent(SceneComponent)
```

Text 3DComponent

**C++ Source:**

- **Plugin**: Text3D
- **Module**: Text3D
- **File**: Text3DComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``back_material`` (MaterialInterface):  [Read-Write] Material for the back part
- ``bevel`` (float):  [Read-Write] Size of bevel
- ``bevel_material`` (MaterialInterface):  [Read-Write] Material for the bevel part
- ``bevel_segments`` (int32):  [Read-Write] Bevel Segments (Defines the amount of tesselation for the bevel part)
- ``bevel_type`` (Text3DBevelType):  [Read-Write] Bevel Type
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``cast_shadow`` (bool):  [Read-Write] Controls whether the text glyphs should cast a shadow or not.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``extrude`` (float):  [Read-Write] Size of the extrude
- ``extrude_material`` (MaterialInterface):  [Read-Write] Material for the extruded part
- ``font`` (Font):  [Read-Write] Text font
- ``front_material`` (MaterialInterface):  [Read-Write] Material for the front part
- ``has_max_height`` (bool):  [Read-Write] Enables a maximum height to the 3D Text
- ``has_max_width`` (bool):  [Read-Write] Enables a maximum width to the 3D Text
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``horizontal_alignment`` (Text3DHorizontalTextAlignment):  [Read-Write] Horizontal text alignment
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``kerning`` (float):  [Read-Write] Text kerning
- ``line_spacing`` (float):  [Read-Write] Extra line spacing
- ``max_height`` (float):  [Read-Write] Sets a maximum height to the 3D Text
- ``max_width`` (float):  [Read-Write] Sets a maximum width to the 3D Text
- ``max_width_handling`` (Text3DMaxWidthHandling):  [Read-Write] Dictates how to handle the text if it exceeds the max width
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``outline`` (bool):  [Read-Write] Generate Outline
- ``outline_expand`` (float):  [Read-Write] Outline expand/offset amount
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``refresh_on_change`` (bool):  [Read-Write] Whether to allow automatic refresh/mesh generation
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``scale_proportionally`` (bool):  [Read-Write] Should the mesh scale proportionally when Max Width/Height is set
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``text`` (Text):  [Read-Write] The text to generate a 3d mesh
- ``text_generated_delegate`` (TextGenerated):  [Read-Write]
- ``typeface`` (Name):  [Read-Write]
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``vertical_alignment`` (Text3DVerticalTextAlignment):  [Read-Write] Vertical text alignment
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``word_spacing`` (float):  [Read-Write] Extra word spacing

<a id="unreal.Text3DComponent.refresh_on_change"></a>

#### refresh\_on\_change

```python
@property
def refresh_on_change() -> bool
```

(bool):  [Read-Write] Whether to allow automatic refresh/mesh generation

<a id="unreal.Text3DComponent.refresh_on_change"></a>

#### refresh\_on\_change

```python
@refresh_on_change.setter
def refresh_on_change(value: bool) -> None
```

<a id="unreal.Text3DComponent.text"></a>

#### text

```python
@property
def text() -> Text
```

(Text):  [Read-Write] The text to generate a 3d mesh

<a id="unreal.Text3DComponent.text"></a>

#### text

```python
@text.setter
def text(value: Text) -> None
```

<a id="unreal.Text3DComponent.extrude"></a>

#### extrude

```python
@property
def extrude() -> float
```

(float):  [Read-Write] Size of the extrude

<a id="unreal.Text3DComponent.extrude"></a>

#### extrude

```python
@extrude.setter
def extrude(value: float) -> None
```

<a id="unreal.Text3DComponent.bevel"></a>

#### bevel

```python
@property
def bevel() -> float
```

(float):  [Read-Write] Size of bevel

<a id="unreal.Text3DComponent.bevel"></a>

#### bevel

```python
@bevel.setter
def bevel(value: float) -> None
```

<a id="unreal.Text3DComponent.bevel_type"></a>

#### bevel\_type

```python
@property
def bevel_type() -> Text3DBevelType
```

(Text3DBevelType):  [Read-Write] Bevel Type

<a id="unreal.Text3DComponent.bevel_type"></a>

#### bevel\_type

```python
@bevel_type.setter
def bevel_type(value: Text3DBevelType) -> None
```

<a id="unreal.Text3DComponent.bevel_segments"></a>

#### bevel\_segments

```python
@property
def bevel_segments() -> int
```

(int32):  [Read-Write] Bevel Segments (Defines the amount of tesselation for the bevel part)

<a id="unreal.Text3DComponent.bevel_segments"></a>

#### bevel\_segments

```python
@bevel_segments.setter
def bevel_segments(value: int) -> None
```

<a id="unreal.Text3DComponent.outline"></a>

#### outline

```python
@property
def outline() -> bool
```

(bool):  [Read-Write] Generate Outline

<a id="unreal.Text3DComponent.outline"></a>

#### outline

```python
@outline.setter
def outline(value: bool) -> None
```

<a id="unreal.Text3DComponent.outline_expand"></a>

#### outline\_expand

```python
@property
def outline_expand() -> float
```

(float):  [Read-Write] Outline expand/offset amount

<a id="unreal.Text3DComponent.outline_expand"></a>

#### outline\_expand

```python
@outline_expand.setter
def outline_expand(value: float) -> None
```

<a id="unreal.Text3DComponent.front_material"></a>

#### front\_material

```python
@property
def front_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] Material for the front part

<a id="unreal.Text3DComponent.front_material"></a>

#### front\_material

```python
@front_material.setter
def front_material(value: MaterialInterface) -> None
```

<a id="unreal.Text3DComponent.bevel_material"></a>

#### bevel\_material

```python
@property
def bevel_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] Material for the bevel part

<a id="unreal.Text3DComponent.bevel_material"></a>

#### bevel\_material

```python
@bevel_material.setter
def bevel_material(value: MaterialInterface) -> None
```

<a id="unreal.Text3DComponent.extrude_material"></a>

#### extrude\_material

```python
@property
def extrude_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] Material for the extruded part

<a id="unreal.Text3DComponent.extrude_material"></a>

#### extrude\_material

```python
@extrude_material.setter
def extrude_material(value: MaterialInterface) -> None
```

<a id="unreal.Text3DComponent.back_material"></a>

#### back\_material

```python
@property
def back_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] Material for the back part

<a id="unreal.Text3DComponent.back_material"></a>

#### back\_material

```python
@back_material.setter
def back_material(value: MaterialInterface) -> None
```

<a id="unreal.Text3DComponent.font"></a>

#### font

```python
@property
def font() -> Font
```

(Font):  [Read-Write] Text font

<a id="unreal.Text3DComponent.font"></a>

#### font

```python
@font.setter
def font(value: Font) -> None
```

<a id="unreal.Text3DComponent.typeface"></a>

#### typeface

```python
@property
def typeface() -> Name
```

(Name):  [Read-Write]

<a id="unreal.Text3DComponent.typeface"></a>

#### typeface

```python
@typeface.setter
def typeface(value: Name) -> None
```

<a id="unreal.Text3DComponent.horizontal_alignment"></a>

#### horizontal\_alignment

```python
@property
def horizontal_alignment() -> Text3DHorizontalTextAlignment
```

(Text3DHorizontalTextAlignment):  [Read-Write] Horizontal text alignment

<a id="unreal.Text3DComponent.horizontal_alignment"></a>

#### horizontal\_alignment

```python
@horizontal_alignment.setter
def horizontal_alignment(value: Text3DHorizontalTextAlignment) -> None
```

<a id="unreal.Text3DComponent.vertical_alignment"></a>

#### vertical\_alignment

```python
@property
def vertical_alignment() -> Text3DVerticalTextAlignment
```

(Text3DVerticalTextAlignment):  [Read-Write] Vertical text alignment

<a id="unreal.Text3DComponent.vertical_alignment"></a>

#### vertical\_alignment

```python
@vertical_alignment.setter
def vertical_alignment(value: Text3DVerticalTextAlignment) -> None
```

<a id="unreal.Text3DComponent.kerning"></a>

#### kerning

```python
@property
def kerning() -> float
```

(float):  [Read-Write] Text kerning

<a id="unreal.Text3DComponent.kerning"></a>

#### kerning

```python
@kerning.setter
def kerning(value: float) -> None
```

<a id="unreal.Text3DComponent.line_spacing"></a>

#### line\_spacing

```python
@property
def line_spacing() -> float
```

(float):  [Read-Write] Extra line spacing

<a id="unreal.Text3DComponent.line_spacing"></a>

#### line\_spacing

```python
@line_spacing.setter
def line_spacing(value: float) -> None
```

<a id="unreal.Text3DComponent.word_spacing"></a>

#### word\_spacing

```python
@property
def word_spacing() -> float
```

(float):  [Read-Write] Extra word spacing

<a id="unreal.Text3DComponent.word_spacing"></a>

#### word\_spacing

```python
@word_spacing.setter
def word_spacing(value: float) -> None
```

<a id="unreal.Text3DComponent.has_max_width"></a>

#### has\_max\_width

```python
@property
def has_max_width() -> bool
```

(bool):  [Read-Write] Enables a maximum width to the 3D Text

<a id="unreal.Text3DComponent.has_max_width"></a>

#### has\_max\_width

```python
@has_max_width.setter
def has_max_width(value: bool) -> None
```

<a id="unreal.Text3DComponent.max_width"></a>

#### max\_width

```python
@property
def max_width() -> float
```

(float):  [Read-Write] Sets a maximum width to the 3D Text

<a id="unreal.Text3DComponent.max_width"></a>

#### max\_width

```python
@max_width.setter
def max_width(value: float) -> None
```

<a id="unreal.Text3DComponent.has_max_height"></a>

#### has\_max\_height

```python
@property
def has_max_height() -> bool
```

(bool):  [Read-Write] Enables a maximum height to the 3D Text

<a id="unreal.Text3DComponent.has_max_height"></a>

#### has\_max\_height

```python
@has_max_height.setter
def has_max_height(value: bool) -> None
```

<a id="unreal.Text3DComponent.max_width_handling"></a>

#### max\_width\_handling

```python
@property
def max_width_handling() -> Text3DMaxWidthHandling
```

(Text3DMaxWidthHandling):  [Read-Write] Dictates how to handle the text if it exceeds the max width

<a id="unreal.Text3DComponent.max_width_handling"></a>

#### max\_width\_handling

```python
@max_width_handling.setter
def max_width_handling(value: Text3DMaxWidthHandling) -> None
```

<a id="unreal.Text3DComponent.max_height"></a>

#### max\_height

```python
@property
def max_height() -> float
```

(float):  [Read-Write] Sets a maximum height to the 3D Text

<a id="unreal.Text3DComponent.max_height"></a>

#### max\_height

```python
@max_height.setter
def max_height(value: float) -> None
```

<a id="unreal.Text3DComponent.scale_proportionally"></a>

#### scale\_proportionally

```python
@property
def scale_proportionally() -> bool
```

(bool):  [Read-Write] Should the mesh scale proportionally when Max Width/Height is set

<a id="unreal.Text3DComponent.scale_proportionally"></a>

#### scale\_proportionally

```python
@scale_proportionally.setter
def scale_proportionally(value: bool) -> None
```

<a id="unreal.Text3DComponent.cast_shadow"></a>

#### cast\_shadow

```python
@property
def cast_shadow() -> bool
```

(bool):  [Read-Write] Controls whether the text glyphs should cast a shadow or not.

<a id="unreal.Text3DComponent.cast_shadow"></a>

#### cast\_shadow

```python
@cast_shadow.setter
def cast_shadow(value: bool) -> None
```

<a id="unreal.Text3DComponent.text_generated_delegate"></a>

#### text\_generated\_delegate

```python
@property
def text_generated_delegate() -> TextGenerated
```

(TextGenerated):  [Read-Write]

<a id="unreal.Text3DComponent.text_generated_delegate"></a>

#### text\_generated\_delegate

```python
@text_generated_delegate.setter
def text_generated_delegate(value: TextGenerated) -> None
```

<a id="unreal.Text3DComponent.set_word_spacing"></a>

#### set\_word\_spacing

```python
def set_word_spacing(value: float) -> None
```

x.set_word_spacing(value) -> None
Set the word spacing value and signal the primitives to be rebuilt
deprecated: Set the property directly

Args:
    value (float):

<a id="unreal.Text3DComponent.set_vertical_alignment"></a>

#### set\_vertical\_alignment

```python
def set_vertical_alignment(value: Text3DVerticalTextAlignment) -> None
```

x.set_vertical_alignment(value) -> None
Set the vertical alignment and signal the primitives to be rebuilt
deprecated: Set the property directly

Args:
    value (Text3DVerticalTextAlignment):

<a id="unreal.Text3DComponent.set_text"></a>

#### set\_text

```python
def set_text(value: Text) -> None
```

x.set_text(value) -> None
Set the text value and signal the primitives to be rebuilt
deprecated: Set the property directly

Args:
    value (Text):

<a id="unreal.Text3DComponent.set_scale_proportionally"></a>

#### set\_scale\_proportionally

```python
def set_scale_proportionally(value: bool) -> None
```

x.set_scale_proportionally(value) -> None
Set if the mesh should scale proportionally when Max Width/Height is set
deprecated: Set the property directly

Args:
    value (bool):

<a id="unreal.Text3DComponent.set_outline_expand"></a>

#### set\_outline\_expand

```python
def set_outline_expand(value: float) -> None
```

x.set_outline_expand(value) -> None
Set the outline width.
deprecated: Set the property directly

Args:
    value (float):

<a id="unreal.Text3DComponent.set_max_width_handling"></a>

#### set\_max\_width\_handling

```python
def set_max_width_handling(value: Text3DMaxWidthHandling) -> None
```

x.set_max_width_handling(value) -> None
Set the Maximum Width Handling - Whether to wrap before scaling when the text size reaches the max width
deprecated: Set the property directly

Args:
    value (Text3DMaxWidthHandling):

<a id="unreal.Text3DComponent.set_max_width"></a>

#### set\_max\_width

```python
def set_max_width(value: float) -> None
```

x.set_max_width(value) -> None
Set the Maximum Width - If width is larger, mesh will scale down to fit MaxWidth value
deprecated: Set the property directly

Args:
    value (float):

<a id="unreal.Text3DComponent.set_max_height"></a>

#### set\_max\_height

```python
def set_max_height(value: float) -> None
```

x.set_max_height(value) -> None
Set the Maximum Height - If height is larger, mesh will scale down to fit MaxHeight value
deprecated: Set the property directly

Args:
    value (float):

<a id="unreal.Text3DComponent.set_line_spacing"></a>

#### set\_line\_spacing

```python
def set_line_spacing(value: float) -> None
```

x.set_line_spacing(value) -> None
Set the line spacing value and signal the primitives to be rebuilt
deprecated: Set the property directly

Args:
    value (float):

<a id="unreal.Text3DComponent.set_kerning"></a>

#### set\_kerning

```python
def set_kerning(value: float) -> None
```

x.set_kerning(value) -> None
Set the kerning value and signal the primitives to be rebuilt
deprecated: Set the property directly

Args:
    value (float):

<a id="unreal.Text3DComponent.set_horizontal_alignment"></a>

#### set\_horizontal\_alignment

```python
def set_horizontal_alignment(value: Text3DHorizontalTextAlignment) -> None
```

x.set_horizontal_alignment(value) -> None
Set the horizontal alignment value and signal the primitives to be rebuilt
deprecated: Set the property directly

Args:
    value (Text3DHorizontalTextAlignment):

<a id="unreal.Text3DComponent.set_has_outline"></a>

#### set\_has\_outline

```python
def set_has_outline(value: bool) -> None
```

x.set_has_outline(value) -> None
Set whether an outline is applied.
deprecated: Set the property directly

Args:
    value (bool):

<a id="unreal.Text3DComponent.set_has_max_width"></a>

#### set\_has\_max\_width

```python
def set_has_max_width(value: bool) -> None
```

x.set_has_max_width(value) -> None
Enable / Disable a Maximum Width
deprecated: Set the property directly

Args:
    value (bool):

<a id="unreal.Text3DComponent.set_has_max_height"></a>

#### set\_has\_max\_height

```python
def set_has_max_height(value: bool) -> None
```

x.set_has_max_height(value) -> None
Enable / Disable a Maximum Height
deprecated: Set the property directly

Args:
    value (bool):

<a id="unreal.Text3DComponent.set_front_material"></a>

#### set\_front\_material

```python
def set_front_material(value: MaterialInterface) -> None
```

x.set_front_material(value) -> None
Set the text front material
deprecated: Set the property directly

Args:
    value (MaterialInterface):

<a id="unreal.Text3DComponent.set_freeze"></a>

#### set\_freeze

```python
def set_freeze(freeze: bool) -> None
```

x.set_freeze(freeze) -> None
Freeze mesh rebuild, to avoid unnecessary mesh rebuilds when setting a few properties together
deprecated: Set the property directly

Args:
    freeze (bool):

<a id="unreal.Text3DComponent.set_font"></a>

#### set\_font

```python
def set_font(font: Font) -> None
```

x.set_font(font) -> None
Set the text font and signal the primitives to be rebuilt
deprecated: Set the property directly

Args:
    font (Font):

<a id="unreal.Text3DComponent.set_extrude_material"></a>

#### set\_extrude\_material

```python
def set_extrude_material(value: MaterialInterface) -> None
```

x.set_extrude_material(value) -> None
Set the text extrude material
deprecated: Set the property directly

Args:
    value (MaterialInterface):

<a id="unreal.Text3DComponent.set_extrude"></a>

#### set\_extrude

```python
def set_extrude(value: float) -> None
```

x.set_extrude(value) -> None
Set the text extrusion size and signal the primitives to be rebuilt
deprecated: Set the property directly

Args:
    value (float):

<a id="unreal.Text3DComponent.set_cast_shadow"></a>

#### set\_cast\_shadow

```python
def set_cast_shadow(new_cast_shadow: bool) -> None
```

x.set_cast_shadow(new_cast_shadow) -> None
Set the value of CastShadow.
deprecated: Set the property directly

Args:
    new_cast_shadow (bool):

<a id="unreal.Text3DComponent.set_bevel_type"></a>

#### set\_bevel\_type

```python
def set_bevel_type(value: Text3DBevelType) -> None
```

x.set_bevel_type(value) -> None
Set the 3d bevel type
deprecated: Set the property directly

Args:
    value (Text3DBevelType):

<a id="unreal.Text3DComponent.set_bevel_segments"></a>

#### set\_bevel\_segments

```python
def set_bevel_segments(value: int) -> None
```

x.set_bevel_segments(value) -> None
Set the amount of segments that will be used to tessellate the Bevel
deprecated: Set the property directly

Args:
    value (int32):

<a id="unreal.Text3DComponent.set_bevel_material"></a>

#### set\_bevel\_material

```python
def set_bevel_material(value: MaterialInterface) -> None
```

x.set_bevel_material(value) -> None
Set the text bevel material
deprecated: Set the property directly

Args:
    value (MaterialInterface):

<a id="unreal.Text3DComponent.set_bevel"></a>

#### set\_bevel

```python
def set_bevel(value: float) -> None
```

x.set_bevel(value) -> None
Set the 3d bevel value
deprecated: Set the property directly

Args:
    value (float):

<a id="unreal.Text3DComponent.set_back_material"></a>

#### set\_back\_material

```python
def set_back_material(value: MaterialInterface) -> None
```

x.set_back_material(value) -> None
Set the text back material
deprecated: Set the property directly

Args:
    value (MaterialInterface):

<a id="unreal.Text3DComponent.get_text_scale"></a>

#### get\_text\_scale

```python
def get_text_scale() -> Vector
```

x.get_text_scale() -> Vector
Gets the scale of actual text geometry, taking into account MaxWidth and MaxHeight constraints. This function will NOT return the component scale

Returns:
    Vector:

<a id="unreal.Text3DComponent.get_glyph_mesh_components"></a>

#### get\_glyph\_mesh\_components

```python
def get_glyph_mesh_components() -> Array[StaticMeshComponent]
```

x.get_glyph_mesh_components() -> Array[StaticMeshComponent]
Gets all the glyph meshes

Returns:
    Array[StaticMeshComponent]:

<a id="unreal.Text3DComponent.get_glyph_mesh_component"></a>

#### get\_glyph\_mesh\_component

```python
def get_glyph_mesh_component(index: int) -> StaticMeshComponent
```

x.get_glyph_mesh_component(index) -> StaticMeshComponent
Gets the StaticMeshComponent of a glyph

Args:
    index (int32): 

Returns:
    StaticMeshComponent:

<a id="unreal.Text3DComponent.get_glyph_kerning_components"></a>

#### get\_glyph\_kerning\_components

```python
def get_glyph_kerning_components() -> Array[SceneComponent]
```

x.get_glyph_kerning_components() -> Array[SceneComponent]
Gets all the glyph kerning components

Returns:
    Array[SceneComponent]:

<a id="unreal.Text3DComponent.get_glyph_kerning_component"></a>

#### get\_glyph\_kerning\_component

```python
def get_glyph_kerning_component(index: int) -> SceneComponent
```

x.get_glyph_kerning_component(index) -> SceneComponent
Gets the USceneComponent that a glyph is attached to

Args:
    index (int32): 

Returns:
    SceneComponent:

<a id="unreal.Text3DComponent.get_glyph_count"></a>

#### get\_glyph\_count

```python
def get_glyph_count() -> int
```

x.get_glyph_count() -> int32
Gets the number of font glyphs that are currently used

Returns:
    int32:

<a id="unreal.Text3DComponent.get_formatted_text"></a>

#### get\_formatted\_text

```python
def get_formatted_text() -> Text
```

x.get_formatted_text() -> Text
Returns the Text property, after being formatted by the FormatText virtual function.
If FormatText is not overriden, the return FText will be the same as the Text property.

Returns:
    Text:

<a id="unreal.Text3DComponent.get_bounds"></a>

#### get\_bounds

```python
def get_bounds() -> Tuple[Vector, Vector]
```

x.get_bounds() -> (origin=Vector, box_extent=Vector)
Get Bounds

Returns:
    tuple: 

    origin (Vector): 

    box_extent (Vector):

<a id="unreal.LayersBlueprintLibrary"></a>