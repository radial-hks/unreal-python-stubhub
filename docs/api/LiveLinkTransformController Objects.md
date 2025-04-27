## LiveLinkTransformController Objects

```python
class LiveLinkTransformController(LiveLinkControllerBase)
```

Live Link Transform Controller

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLinkComponents
- **File**: LiveLinkTransformController.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_picker`` (ComponentReference):  [Read-Write] A component reference (customized) that allows the user to specify a component that this controller should control
- ``offset_transform`` (Transform):  [Read-Write] Offset transform applied in local space to the controlled scene component
- ``transform_data`` (LiveLinkTransformControllerData):  [Read-Write]

<a id="unreal.LiveLinkTransformController.transform_data"></a>

#### transform_data

```python
@property
def transform_data() -> LiveLinkTransformControllerData
```

(LiveLinkTransformControllerData):  [Read-Write]

<a id="unreal.LiveLinkTransformController.transform_data"></a>

#### transform_data

```python
@transform_data.setter
def transform_data(value: LiveLinkTransformControllerData) -> None
```

<a id="unreal.LiveLinkTransformController.offset_transform"></a>

#### offset_transform

```python
@property
def offset_transform() -> Transform
```

(Transform):  [Read-Write] Offset transform applied in local space to the controlled scene component

<a id="unreal.LiveLinkTransformController.offset_transform"></a>

#### offset_transform

```python
@offset_transform.setter
def offset_transform(value: Transform) -> None
```

<a id="unreal.LiveLinkComponentController"></a>