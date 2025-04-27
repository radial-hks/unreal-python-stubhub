## MaterialExpressionNeuralNetworkOutput Objects

```python
class MaterialExpressionNeuralNetworkOutput(MaterialExpression)
```

The input node that holds the output from the neural network to the post process material

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionNeuralPostProcessNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``neural_index_type`` (NeuralIndexType):  [Read-Write] Indexing type: read from the texture or buffer.
                 Texture index is valid only when the first 2 dimension of the input and output dimension matches.

<a id="unreal.MaterialExpressionNoise"></a>