## SectionAPI Objects

```python
class SectionAPI(ApiClassBase)
```

Section API

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: SectionAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``section_entity_ptr`` (SectionEntity):  [Read-Only]

<a id="unreal.SectionAPI.start_section"></a>

#### start\_section

```python
def start_section(
        create_entity_params: CreateSectionParams) -> Optional[EidResult]
```

x.start_section(create_entity_params) -> EidResult or None
APIs

Args:
    create_entity_params (CreateSectionParams): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.SectionAPI.end_section"></a>

#### end\_section

```python
def end_section(params: ParamsBase) -> Optional[EidResult]
```

x.end_section(params) -> EidResult or None
End Section

Args:
    params (ParamsBase): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.SetSceneStyleAPI"></a>