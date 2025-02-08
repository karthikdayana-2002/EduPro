from type_form.models import FormFieldResponse

# if not FormFieldResponse.exists():
#     FormFieldResponse.create_table(
#         read_capacity_units=5,
#         write_capacity_units=5,
#         wait=True
#     )

# # Define all responses directly as model objects
# responses = [
#     FormFieldResponse(form_response_id="response_1", form_field_id="field_101", value="Karthik"),
#     FormFieldResponse(form_response_id="response_1", form_field_id="field_102", value="22"),
#     FormFieldResponse(form_response_id="response_1", form_field_id="field_103", value="Kovvur"),
#     FormFieldResponse(form_response_id="response_2", form_field_id="field_101", value="Sandeep"),
#     FormFieldResponse(form_response_id="response_2", form_field_id="field_102", value="22"),
#     FormFieldResponse(form_response_id="response_2", form_field_id="field_103", value="Rajahmundry"),
#     FormFieldResponse(form_response_id="response_3", form_field_id="field_101", value="Chaitanya"),
#     FormFieldResponse(form_response_id="response_3", form_field_id="field_102", value="23"),
#     FormFieldResponse(form_response_id="response_3", form_field_id="field_103", value="Hyderabad"),
# ]

# # Batch write without explicit looping
# with FormFieldResponse.batch_write() as batch:
#     list(map(batch.save, responses))

# print("Batch write completed without explicit loops!")

for response in FormFieldResponse.query("response_1", FormFieldResponse.form_field_id == "field_101"):
    print(response.value)