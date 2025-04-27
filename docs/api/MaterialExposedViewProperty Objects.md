## MaterialExposedViewProperty Objects

```python
class MaterialExposedViewProperty(EnumBase)
```

EMaterial Exposed View Property

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionViewProperty.h

<a id="unreal.MaterialExposedViewProperty.MEVP_BUFFER_SIZE"></a>

#### MEVP_BUFFER_SIZE

0: Horizontal and vertical size of the view's buffer in pixels

<a id="unreal.MaterialExposedViewProperty.MEVP_FIELD_OF_VIEW"></a>

#### MEVP_FIELD_OF_VIEW

1: Horizontal and vertical field of view angles in radian

<a id="unreal.MaterialExposedViewProperty.MEVP_TAN_HALF_FIELD_OF_VIEW"></a>

#### MEVP_TAN_HALF_FIELD_OF_VIEW

2: Tan(FieldOfView * 0.5)

<a id="unreal.MaterialExposedViewProperty.MEVP_VIEW_SIZE"></a>

#### MEVP_VIEW_SIZE

3: Horizontal and vertical size of the view in pixels

<a id="unreal.MaterialExposedViewProperty.MEVP_WORLD_SPACE_VIEW_POSITION"></a>

#### MEVP_WORLD_SPACE_VIEW_POSITION

4: Absolute world space view position (differs from the camera position in the shadow passes)

<a id="unreal.MaterialExposedViewProperty.MEVP_WORLD_SPACE_CAMERA_POSITION"></a>

#### MEVP_WORLD_SPACE_CAMERA_POSITION

5: Absolute world space camera position

<a id="unreal.MaterialExposedViewProperty.MEVP_VIEWPORT_OFFSET"></a>

#### MEVP_VIEWPORT_OFFSET

6: Horizontal and vertical position of the viewport in pixels within the buffer.

<a id="unreal.MaterialExposedViewProperty.MEVP_TEMPORAL_SAMPLE_COUNT"></a>

#### MEVP_TEMPORAL_SAMPLE_COUNT

7: Number of temporal AA sample used across multiple to converge to anti aliased output.

<a id="unreal.MaterialExposedViewProperty.MEVP_TEMPORAL_SAMPLE_INDEX"></a>

#### MEVP_TEMPORAL_SAMPLE_INDEX

8: Index of the Temporal AA jitter for this frame.

<a id="unreal.MaterialExposedViewProperty.MEVP_TEMPORAL_SAMPLE_OFFSET"></a>

#### MEVP_TEMPORAL_SAMPLE_OFFSET

9: Offset of the temporal sample for this frame in pixel size.

<a id="unreal.MaterialExposedViewProperty.MEVP_RUNTIME_VIRTUAL_TEXTURE_OUTPUT_LEVEL"></a>

#### MEVP_RUNTIME_VIRTUAL_TEXTURE_OUTPUT_LEVEL

10: Mip Level that Runtime Virtual Texture Output is rendering to.

<a id="unreal.MaterialExposedViewProperty.MEVP_RUNTIME_VIRTUAL_TEXTURE_OUTPUT_DERIVATIVE"></a>

#### MEVP_RUNTIME_VIRTUAL_TEXTURE_OUTPUT_DERIVATIVE

11: World space derivatives for Runtime Virtual Texture Output.

<a id="unreal.MaterialExposedViewProperty.MEVP_PRE_EXPOSURE"></a>

#### MEVP_PRE_EXPOSURE

12: Pre Exposure

<a id="unreal.MaterialExposedViewProperty.MEVP_RUNTIME_VIRTUAL_TEXTURE_MAX_LEVEL"></a>

#### MEVP_RUNTIME_VIRTUAL_TEXTURE_MAX_LEVEL

13: Maximum mip level of Runtime Virtual Texture that Runtime Virtual Texture Output is rendering to.

<a id="unreal.MaterialExposedViewProperty.MEVP_RESOLUTION_FRACTION"></a>

#### MEVP_RESOLUTION_FRACTION

14: Screen percentage at which the rendering resolution happens, to allow tech-art to remain consistent with dynamic resolution.

<a id="unreal.MaterialExposedViewProperty.MEVP_POST_VOLUME_USER_FLAGS"></a>

#### MEVP_POST_VOLUME_USER_FLAGS

15: Post process volume user flags, useful for varying the behavior of a material per view

<a id="unreal.WorldPositionIncludedOffsets"></a>