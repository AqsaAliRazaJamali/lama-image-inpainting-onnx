import onnxruntime as ort

model_path = "inpainting_lama_2025jan.onnx"

session = ort.InferenceSession(model_path)

print("MODEL INPUTS")
print("----------------")

for input_info in session.get_inputs():
    print("Name:", input_info.name)
    print("Shape:", input_info.shape)
    print("Type:", input_info.type)

print("\nMODEL OUTPUTS")
print("----------------")

for output_info in session.get_outputs():
    print("Name:", output_info.name)
    print("Shape:", output_info.shape)
    print("Type:", output_info.type)