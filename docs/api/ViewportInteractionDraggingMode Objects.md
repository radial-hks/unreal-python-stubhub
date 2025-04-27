## ViewportInteractionDraggingMode Objects

```python
class ViewportInteractionDraggingMode(EnumBase)
```

Methods of dragging objects around in VR

**C++ Source:**

- **Module**: ViewportInteraction
- **File**: ViewportInteractionTypes.h

<a id="unreal.ViewportInteractionDraggingMode.NOTHING"></a>

#### NOTHING

0: Not dragging right now with this hand

<a id="unreal.ViewportInteractionDraggingMode.TRANSFORMABLES_WITH_GIZMO"></a>

#### TRANSFORMABLES_WITH_GIZMO

1: Dragging transformables (e.g. actors, components, geometry elements) around using the transform gizmo

<a id="unreal.ViewportInteractionDraggingMode.TRANSFORMABLES_AT_LASER_IMPACT"></a>

#### TRANSFORMABLES_AT_LASER_IMPACT

2: Transformables locked to the impact point under the laser

<a id="unreal.ViewportInteractionDraggingMode.ASSISTING_DRAG"></a>

#### ASSISTING_DRAG

3: We're grabbing an object (or the world) that was already grabbed by the other hand

<a id="unreal.ViewportInteractionDraggingMode.TRANSFORMABLES_FREELY"></a>

#### TRANSFORMABLES_FREELY

4: Freely moving, rotating and scaling transformables with one or two hands

<a id="unreal.ViewportInteractionDraggingMode.WORLD"></a>

#### WORLD

5: Moving the world itself around (actually, moving the camera in such a way that it feels like you're moving the world)

<a id="unreal.ViewportInteractionDraggingMode.INTERACTABLE"></a>

#### INTERACTABLE

6: Moving a custom interactable

<a id="unreal.ViewportInteractionDraggingMode.MATERIAL"></a>

#### MATERIAL

7: Dragging a material

<a id="unreal.GizmoHandleTypes"></a>